import argparse
from functools import reduce


def gen_groups(f):
    g = []
    for line in f:
        line = line.strip()
        if line == "":
            yield g
            g = []
            continue

        g.append(line)
    if g:
        yield g


def num_yes(group: list[str]) -> int:
    qs = set("".join(group))
    return len(qs)


def num_common(group: list[str]) -> int:
    x, *xs = map(set, group)
    rs = x.intersection(*xs)
#    print(x, xs, rs, len(rs))
    return len(rs)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=argparse.FileType("r"))
    args = parser.parse_args()

    groups = list(gen_groups(args.input))
    print(sum(num_yes(group) for group in groups))
    print(sum(num_common(group) for group in groups))



if __name__ == "__main__":
    main()