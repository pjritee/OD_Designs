
# OD2tex.py
# Convert OD in JSON format to LaTeX representation

import json
import argparse

begin_array = "$\n\\left[{\\begin{array}"
end_array = "\\end{array} } \\right]\n$"

"""Convert integer to LaTeX representation of the corresponding indeterminant."""
def n2tex(n, use_bar=False):
    n = int(n)
    if n == 0:
        return "0"
    if n > 0:
        return "x_"+str(n)
    
    # n < 0
    if use_bar:
        return "\\overline{x_"+str(-n)+"}"
    else:
        return "-x_"+str(-n)

"""Generate LaTeX array from 2D list."""
def generate_tex(a, use_bar=False):
    text = begin_array + "{" + len(a)*"r" + "}\n"
    for r in a:
        text +=' & '.join(n2tex(c, use_bar) for c in r) + "\\\\\n"
    return text+end_array

"""Convert OD in JSON format to LaTeX representation."""
def OD2tex(filename, use_bar=False):
    with open(filename, 'r') as fd:
        text = fd.read()
        
    d = json.loads(text)
    print(generate_tex(d, use_bar))


def main():
    parser = argparse.ArgumentParser(description="Convert OD in JSON format to LaTeX")
    parser.add_argument("filename", help="The JSON file to convert")
    parser.add_argument("--use_bar", action="store_true", help="Use bar notation for negative numbers")
    args = parser.parse_args()
    OD2tex(args.filename, args.use_bar)

if __name__ == "__main__":
    main()
