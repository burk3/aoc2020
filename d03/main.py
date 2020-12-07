import argparse
import sys
from math import prod

SLOPES = [
    (1, 1),
    (3, 1), 
    (5, 1),
    (7, 1),
    (1, 2),
]

class WrappedRow(list):
    def __getitem__(self, n):
        return super().__getitem__(n % len(self))


def calc_hits(tree_map: list[WrappedRow], dx: int, dy: int):
    hits = 0
    x, y = 0, 0
    while y < len(tree_map):
        if tree_map[y][x]:
            hits += 1
        x += dx
        y += dy
    
    return hits


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=argparse.FileType("r"))
    args = parser.parse_args()

    tree_map: list[WrappedRow] = []
    for line in args.input:
        tree_map.append(WrappedRow(c == "#" for c in line.strip()))
    
    print(prod(calc_hits(tree_map, dx, dy) for dx, dy in SLOPES))

    

if __name__ == "__main__":
    main()
    
