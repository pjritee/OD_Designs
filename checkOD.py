# checkOD.py
# Check orthogonal design from file in JSON format

import json
import argparse
import numpy as np


"""Check orthogonal design from JSON file."""
def checkOD(filename):
    with open(filename, 'r') as fd:
        text = fd.read()

    design = json.loads(text)
    size = len(design[0]) 
    identity = np.identity(size, dtype=int)
 

    num = max(abs(c) for c in design[0]) # number of indeterminants

    # Create variable matrices (the A_i matrices)
    # vars[i] corresponds to indeterminant i+1
    # Initialize to zero matrices
    vars = [np.zeros((size,size), dtype=int) for _ in range(num)]

    # Fill in the variable matrices
    for i in range(num):
        v = vars[i]
        for r in range(size):
            for c in range(size):
                if abs(design[r][c]) == (i+1):
                    v[r][c] = design[r][c]//(i+1)

    # Check the orthogonality conditions
    for  i in range(num):
        p = vars[i]@np.transpose(vars[i])
        n = p[0][0]
        if not np.array_equal(p, n*identity):
            print("Failed self product for variable ", i+1)
            return

    # Check cross products
    for i in range(num):
        for j in range(i+1, num):
            if not np.array_equal(vars[i]@np.transpose(vars[j]), -1*vars[j]@np.transpose(vars[i])):
                print("Failed cross product for variables ", i+1, " and ", j+1)
                return
            
    print("Design is orthogonal.")


def main():
    parser = argparse.ArgumentParser(description="Check OD design from JSON file")
    parser.add_argument("filename", help="The JSON file to check")
    args = parser.parse_args()
    checkOD(args.filename)

if __name__ == "__main__":
    main()
