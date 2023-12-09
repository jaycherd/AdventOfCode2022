from typing import List,Dict,Tuple
from icecream import ic





if __name__ == "__main__":
    f_name = "../in.txt"
    max_cals_held1 = 0
    max_cals_held2 = 0
    max_cals_held3 = 0
    curr_elf_hold = 0


    try:
        with open(f_name,'r') as file:
            for line in file:
                line = line.strip()
                if line == '':
                    if curr_elf_hold > max_cals_held1:
                        max_cals_held3 = max_cals_held2
                        max_cals_held2 = max_cals_held1
                        max_cals_held1 = curr_elf_hold
                    elif curr_elf_hold > max_cals_held2:
                        max_cals_held3 = max_cals_held2
                        max_cals_held2 = curr_elf_hold
                    elif curr_elf_hold > max_cals_held1:
                        max_cals_held3 = curr_elf_hold
                    curr_elf_hold = 0
                else:
                    curr_elf_hold += int(line)

    except FileNotFoundError:
        print(f"file {f_name} not found")

    ic(max_cals_held1,max_cals_held2,max_cals_held3)
    ic(max_cals_held1+max_cals_held2+max_cals_held3)