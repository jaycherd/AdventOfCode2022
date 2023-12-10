from typing import List,Dict,Tuple
from icecream import ic






if __name__ == "__main__":
    f_name = "../in.txt"
    result_map = {"AX":4,"AY":8,"AZ":3,
                  "BX":1,"BY":5,"BZ":9,
                  "CX":7,"CY":2,"CZ":6}
    total_score = 0
    

    try:
        with open(f_name,'r') as file:
            for line in file:
                line = "".join(line.strip().split())
                total_score += result_map[line]
    
    except FileNotFoundError:
        print(f"file {f_name} not found")

    ic(total_score)


"""
XXX DESCRIPTION XXX
 The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors) 
 plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won)
"""