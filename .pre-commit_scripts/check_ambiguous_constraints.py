#!/usr/bin/env python3
import sys

if __name__ == '__main__':
    arguments = sys.argv
    # The first parameter is always the call to this executable "python3 check-ambiguous-references" which we can drop
    arguments.pop(0)

    ambiguous_constraints_found = False

    # Searches through all of the modified files looking for the introduction of ambiguous constraints
    for argument in arguments:
        file = open(argument,  "r")
        if "ambiguous=\"YES\"" in file.read():
            sys.stdout.write("Ambiguous constraints found in " + file.name + "\n")
            ambiguous_constraints_found = True

    exit(1) if ambiguous_constraints_found else exit(0)
