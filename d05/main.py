import argparse

def to_n(s: str) -> int:
    s = s.replace("F", "0").replace("B", "1")
    s = s.replace("L", "0").replace("R", "1")
    return int(s, base=2)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=argparse.FileType("r"))
    args = parser.parse_args()

    r = 0
    for line in args.input:
        r = max(r, to_n(line.strip()))
    
    print(r)



if __name__ == "__main__":
    main()