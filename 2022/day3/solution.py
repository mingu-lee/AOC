'''
--- Day 3: Rucksack Reorganization ---
One Elf has the important job of loading all of the rucksacks with supplies for the jungle journey. Unfortunately, that Elf didn't quite follow the packing instructions, and so a few items now need to be rearranged.

Each rucksack has two large compartments. All items of a given type are meant to go into exactly one of the two compartments. The Elf that did the packing failed to follow this rule for exactly one item type per rucksack.

The Elves have made a list of all of the items currently in each rucksack (your puzzle input), but they need your help finding the errors. Every item type is identified by a single lowercase or uppercase letter (that is, a and A refer to different types of items).

The list of items for each rucksack is given as characters all on a single line. A given rucksack always has the same number of items in each of its two compartments, so the first half of the characters represent items in the first compartment, while the second half of the characters represent items in the second compartment.

For example, suppose you have the following list of contents from six rucksacks:

vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
The first rucksack contains the items vJrwpWtwJgWrhcsFMMfFFhFp, which means its first compartment contains the items vJrwpWtwJgWr, while the second compartment contains the items hcsFMMfFFhFp. The only item type that appears in both compartments is lowercase p.
The second rucksack's compartments contain jqHRNqRjqzjGDLGL and rsFMfFZSrLrFZsSL. The only item type that appears in both compartments is uppercase L.
The third rucksack's compartments contain PmmdzqPrV and vPwwTWBwg; the only common item type is uppercase P.
The fourth rucksack's compartments only share item type v.
The fifth rucksack's compartments only share item type t.
The sixth rucksack's compartments only share item type s.
To help prioritize item rearrangement, every item type can be converted to a priority:

Lowercase item types a through z have priorities 1 through 26.
Uppercase item types A through Z have priorities 27 through 52.
In the above example, the priority of the item type that appears in both compartments of each rucksack is 16 (p), 38 (L), 42 (P), 22 (v), 20 (t), and 19 (s); the sum of these is 157.

Find the item type that appears in both compartments of each rucksack. What is the sum of the priorities of those item types?

'''

#가져와서 반으로 나눈다
#하나를 for 돌동안 나머지 반 리스트에 같은게 있는지 체크
#
def atoz():
    _KEY = []
    _key = {}
    a = 1
    for x in range(ord('a'), ord('z')+1):
        _KEY.append(chr(x))
    for x in range(ord('A'), ord('Z')+1):
        _KEY.append(chr(x))
    for k in _KEY:
        _key[k] = a
        a += 1
    return _key

def openfile():
    with open("./2022/day3/input.txt") as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
    return lines

def part1solution():
    answer = 0
    strategy = openfile()
    _key = atoz()

    for i in strategy:
        for j in i[:int(len(i)/2)]:
            if j in i[int(len(i)/2):]:
                for ke,va in _key.items():
                    if j in ke:
                        answer += va
                break
    return answer

def part2solution():
    answer = 0
    strategy = openfile()
    _key = atoz()
    new_list = []
    a = int(len(strategy)/3)
    #print(''.join(strategy))
    for i in range(0,a):
        s = i*3
        new_list.append(''.join(strategy[s:s+3]))
    return new_list 

if __name__ == "__main__":
    #ret = part1solution()
    ret = part2solution()
    print(ret)
    a = ["a","b","c"]
    print(''.join(a[0:2]))

    
