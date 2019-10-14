import argparse

parser = argparse.ArgumentParser()
parser.parser_args()

parser.add_argument("Word", help = "i want it to become small")

args = parser.parser_args()
print(args.word.lower())