import argparse
import re


REQ_FIELDS = {
    "byr": re.compile(r"19[2-9][0-9]|200[0-2]$"),
    "iyr": re.compile(r"20(1[0-9]|20)$"),
    "eyr": re.compile(r"20(2[0-9]|30)$"),
    "hgt": re.compile(r"1([5-8][0-9]|9[0-3])cm|(59|6\d|7[0-6])in$"),
    "hcl": re.compile(r"#[0-9a-f]{6}$"),
    "ecl": re.compile(r"amb|blu|brn|gry|grn|hzl|oth$"),
    "pid": re.compile(r"\d{9}$"),
    #"cid",
}


def gen_passports(f):
    cur = {}
    for line in f:
        line = line.strip()
        if line == "":
            yield cur
            cur = {}
            continue

        fields = line.split()
        for field in fields:
            k, v = field.split(":", 2)
            cur[k] = v

    if cur:
        yield cur

def valid_passport(p):
    if len(REQ_FIELDS.keys() - p.keys()) > 0:
        return False

    for k, r in REQ_FIELDS.items():
        if r.fullmatch(p[k]) is None:
            return False
    
    return True


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=argparse.FileType("r"))
    args = parser.parse_args()

    n = 0
    for passport in gen_passports(args.input):
        if valid_passport(passport):
            n += 1
    
    print(n)


if __name__ == "__main__":
    main()