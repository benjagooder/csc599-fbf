import sys

#sys.tracebacklimit=0

from antlr4 import *
from RomeLexer import RomeLexer
from RomeParser import RomeParser
from MercuryVisitor import MercuryVisitor


def main(argv):
    # Common Part
    input = FileStream(argv[1])
    lexer = RomeLexer(input)
    stream = CommonTokenStream(lexer)
    parser = RomeParser(stream)
    tree = parser.rome()


    sys.stdout = open("C:/Users/user/Rome/romeOutput.txt", "a+")

    visitor = MercuryVisitor()

    myMessages = visitor.getMessages(tree)

    print(str(myMessages))


if __name__ == '__main__':
    main(sys.argv)