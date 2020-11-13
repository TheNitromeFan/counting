def number_in_base(n, b, digits):
    ret = ""
    for _ in range(digits):
        ret = str(n % b) + ret
        n //= b
    return ret


def main():
    lines = ["Quaternary | Octal", ":-: | :-:"]
    for i in range(64):
        lines.append("{} | {}".format(number_in_base(i, 4, 3), number_in_base(i, 8, 2)))
    with open("quaternary-octal.txt", "w") as f:
        f.write("\n".join(lines))


if __name__ == "__main__":
    main()
