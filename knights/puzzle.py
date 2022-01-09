from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    # TODO
    Or(Not(AKnight), And(AKnight, AKnave)),
    Or(Not(AKnave), Not(And(AKnight, AKnave))),
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    # TODO
    Or(Not(AKnight), And(AKnave, BKnave)),
    Or(Not(AKnave), Not(And(AKnave, BKnave))),
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    # TODO
    Or(Not(AKnight), Or(And(AKnave, BKnave), And(AKnight, BKnight))),
    Or(Not(AKnave), Not(Or(And(AKnave, BKnave), And(AKnight, BKnight)))),
    Or(Not(BKnight), Or(And(AKnave, BKnight), And(AKnight, BKnave))),
    Or(Not(BKnave), Not(Or(And(AKnave, BKnight), And(AKnight, BKnave)))),
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave))
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    # TODO
    Or(Not(CKnight), AKnight),
    Or(Not(CKnave), Not(AKnight)),
    Or(Not(BKnight), CKnave),
    Or(Not(BKnave), Not(CKnave)),
    Or(Not(BKnight), And(Or(Not(AKnight), AKnave), Or(Not(AKnave), Not(AKnave)))),
    Or(Not(BKnave), Not(And(Or(Not(AKnight), AKnave), Or(Not(AKnave), Not(AKnave))))),
    Or(And(Or(Not(AKnight), AKnight), Or(Not(AKnave), Not(AKnight))), And(Or(Not(AKnight), AKnave), Or(Not(AKnave), Not(AKnave)))),
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),
    Or(CKnight, CKnave),
    Not(And(CKnight, CKnave))
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
