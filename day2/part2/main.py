from typing import List,Dict,Tuple
from icecream import ic






if __name__ == "__main__":
    f_name = "../in.txt"
    result_map = {"AX":4,"AY":8,"AZ":3,
                  "BX":1,"BY":5,"BZ":9,
                  "CX":7,"CY":2,"CZ":6}
    transform_map = {"AX":"AZ","AY":"AX","AZ":"AY",
                  "BX":"BX","BY":"BY","BZ":"BZ",
                  "CX":"CY","CY":"CZ","CZ":"CX"}
    total_score = 0
    

    try:
        with open(f_name,'r') as file:
            for line in file:
                line = "".join(line.strip().split())
                transformed_line = transform_map[line]
                total_score += result_map[transformed_line]
    
    except FileNotFoundError:
        print(f"file {f_name} not found")

    ic(total_score)


"""
XXX CHANGES XXX
X,Y,Z meanings have changed to --> Lose, Draw, Win; and we need to figure out based on what the opponent through
A(rock), B(paper), C(scissors) what we need to throw to get the result indicated by xyz, after changing to the 
correct thing calculate the score in same way and add up the score
"""