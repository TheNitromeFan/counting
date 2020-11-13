# encoding=utf8    

import config
import csv
import glob
import os
import itertools
import praw
import json
from string import Template
import time
import datetime

post = False
use = 'HOC'
lastK = ''




def read_pLog():
    global lastK
    filtered_data = []
    for pLOG_file in glob.glob('./input/pLOG/*.csv'):
        with open(pLOG_file, 'r', newline='') as csvfile:
            commentreader = csv.reader(csvfile)
            for comment in commentreader:
                if comment[0]!="number": #skip header
                    filtered_data.append(comment)
                    lastK = str( int( int(comment[0])/1000) )  # If the user that had the last k was banned or deleted this might be inaccurate
    return filtered_data





def fill_dict(filtered_data):
    dict_count = {}
    for comment in filtered_data:
        if comment[1] not in dict_count:
            dict_count[comment[1]] = 1
        else:
            dict_count[comment[1]] += 1
    return dict_count


def sort_dict(dict_count):
    
    sorted_list = []
    for key, value in sorted(dict_count.items(), key=lambda kv: (kv[1], kv[0]), reverse=True):
        sorted_list.append((key, value))
    return sorted_list




def get_header():
    my_path = os.path.abspath(os.path.dirname(__file__))
    completeName = os.path.join(my_path, "input", "header.txt")
    with open(completeName) as header_file:
        src = Template(header_file.read())
        header = src.substitute({'k':lastK})
    return header


def get_rankings_for_tuples(sorted_tuples):
    rankings = []
    rank = 1
    for _, tuples in itertools.groupby(sorted_tuples, lambda kv: kv[1]):
        group = [(rank, tuple_uc[0], tuple_uc[1]) for tuple_uc in tuples]
        group.sort(key=lambda x: x[1].lower())
        rankings += group
        rank += len(group)
    return rankings


def write_table(sorted_list):
    fileName = "{}UpTo{}k".format(use,lastK)
    my_path = os.path.abspath(os.path.dirname(__file__))
    complete_name = os.path.join(my_path, "results", fileName + ".txt")
    filetable = open(complete_name, "w")

    for rank, counter, counts in get_rankings_for_tuples(sorted_list):
        filetable.write("{}|/u/{}|{}\n".format(rank, counter, counts))



def get_data():
    fileName = "{}UpTo{}k".format(use,lastK)
    my_path = os.path.abspath(os.path.dirname(__file__))
    complete_name = os.path.join(my_path, "results", fileName + ".txt")
    with open(complete_name) as hoc:
        data = hoc.readlines()
    return data

    
def get_hoc_by_size(data, size):
    data_size_list = data[:size]
    data_size = "".join(data_size_list)
    return data_size


def bot_login():
    print("Logging In...")
    login = praw.Reddit(username = config.username,
			password = config.password,
			client_id = config.client_id,
			client_secret = config.client_secret,
			user_agent = config.user_agent)
    print("Logged in!")
    return login


def update_wiki(data, reddit, wiki_name):
    wiki_page = reddit.subreddit('SomeCountingStuff').wiki[wiki_name]
    for i in range(10):
        try:
            wiki_page.edit(data, "Updated to: {}k".format(lastK) )
            print("Updated {}".format(wiki_name))
            break
        except:
            print("Attempt {}".format(i) )
    

    

    
    

def post_tables(data, reddit):
    header = get_header()
    sizes = [100,250,500,1000]
    default_size = 250

    # post full HoC
    hoc = header + "".join(data)
    fileName = "{}UpTo{}k".format(use,lastK)
    my_path = os.path.abspath(os.path.dirname(__file__))
    complete_name = os.path.join(my_path, "results", fileName + ".txt")
    filetable = open(complete_name, "w")
    filetable.write(hoc)
    # update_wiki(hoc, reddit, "rc_hoc")

    # post various sizes
    for size in sizes:
        wiki_name = "rc_hoc_{}".format(size)
        hoc = header + "".join( get_hoc_by_size(data, size) )
        update_wiki(hoc, reddit, wiki_name)
    print("Updated tables on r/SomeCountingStuff ")

    # post default HoC
    default_hoc = header + get_hoc_by_size(data, default_size)
    wiki_page = reddit.subreddit('counting').wiki['hoc']
    wiki_page.edit(default_hoc, "Updated to: {}k".format(lastK) )
    print("Updated /r/counting hoc")

def main():
    filtered_data = read_pLog()
    dict_count = fill_dict(filtered_data)
    sorted_list = sort_dict(dict_count)
    write_table(sorted_list)
    if post==True:
        data = get_data()
        reddit = bot_login()
        post_tables(data, reddit)


if __name__ == "__main__":
    main()



