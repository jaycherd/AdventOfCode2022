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
    sack1,sack2,sack3 = None,None,None #for a sliding window approach
    line1,line2,line3 = None,None,None
    
    try:
        with open(f_name,'r') as file:
            for line in file:
                line = line.strip()
                if not sack1:
                    sack1 = set(line)
                    line1 = line
                elif not sack2:
                    sack2 = set(line)
                    line2 = line
                else:
                    sack3 = set(line)
                    line3 = line
                    for char1,char2,char3 in zip(line1,line2,line3):
                        if char1 in sack2 and char1 in sack3:
                            pri_total += calc_char_value(char1)
                            ic(char1)
                            break
                        elif char2 in sack1 and char2 in sack3:
                            pri_total += calc_char_value(char2)
                            ic(char2)
                            break
                        elif char3 in sack1 and char3 in sack2:
                            pri_total += calc_char_value(char3)
                            ic(char3)
                            break
                    sack1,sack2,sack3 = None,None,None
                    line1,line2,line3 = None,None,None
                    
    
    except FileNotFoundError:
        print(f"file {f_name} not found")

    ic(pri_total)




"""
XXX CHANGES XXX
each group of three lines corresponds to a group of three elves, where the three elves share some symbol


XXX GOAL XXX
find which item type shared by all three elves in each group, return the sum of the priorities of those item types
"""