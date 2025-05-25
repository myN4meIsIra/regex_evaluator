# main
"""
main script
"""

from analyze import Analyze

def main():
    while True:
        regex = "\'/.*\'" #input("Insert Regex Operation")

        # instantiate Analyze class
        analyze = Analyze()

        analyze.analyzeRegex(regex)

        break


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

