from typing import List,Dict,Tuple
from icecream import ic
from collections import Counter

def range_contains_other(range1: Tuple[int,int], range2: Tuple[int,int]) -> bool:
    start1,end1 = range1
    start2,end2 = range2
    if start1 >= start2 and end1 <= end2:
        return True
    if start2 >= start1 and end2 <= end1:
        return True
    return False


if __name__ == "__main__":
    f_name = "../in.txt"
    res = 0
    
    
    try:
        with open(f_name,'r') as file:
            for line in file:
                elf1,elf2 = line.strip().split(',')
                elf1_interval,elf2_interval = tuple([int(x) for x in elf1.split('-')]),tuple([int(x) for x in elf2.split('-')])
                if range_contains_other(elf1_interval,elf2_interval):
                    res += 1
                    # ic(elf1_interval,elf2_interval)
                    # ic(res)
    
    except FileNotFoundError:
        print(f"file {f_name} not found")

    ic(res)




"""
XXX DESCRIP XXX


XXX GOAL XXX

"""