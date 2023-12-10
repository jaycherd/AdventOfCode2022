from typing import List,Dict,Tuple
from icecream import ic
from collections import Counter

def cut_in_half(line: str) -> Tuple[str,str]:
    return (line[0:len(line)//2],line[len(line)//2:])

def calc_char_value(letter: str) -> int:
    if letter.islower():
        return ord(letter)-offset_lower
    return ord(letter)-offset_upper


if __name__ == "__main__":
    f_name = "../in.txt"
    offset_lower = 96 #ord 'a' - offset = 1
    offset_upper = 38 #ord 'A' - offset = 27
    pri_total = 0
    
    try:
        with open(f_name,'r') as file:
            for line in file:
                left,right = cut_in_half(line.strip())
                l_counter,r_counter = Counter(),Counter()
                for lchar,rchar in zip(left,right):
                    l_counter[lchar] += 1
                    r_counter[rchar] += 1
                    if l_counter[lchar] != 0 and r_counter[lchar] != 0:
                        pri_total += calc_char_value(lchar)
                        break
                    if l_counter[rchar] != 0 and r_counter[rchar] != 0:
                        pri_total += calc_char_value(rchar)
                        break
    
    except FileNotFoundError:
        print(f"file {f_name} not found")

    ic(pri_total)




"""
XXX DESCRIP XXX
ea/line is a rucksack of stuff, with two parts, left and right, which both have exact same num of items, so can split in half
a-z = priority (1-26)
A-Z = priority (27-52)

XXX GOAL XXX
find which items are in BOTH sides, then add up all those priorities
"""