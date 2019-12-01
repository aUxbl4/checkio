# pawn-brotherhood
# https://py.checkio.org/en/mission/pawn-brotherhood/


def safe_pawns(x):
    c = 'abcdefghj'
    x = list(x)
    z = 0
    # diagonal element search b4 = {a3 : c3} in [b4,d4,f4,c3,e3] then safe
    for i in range(len(x)):
        y = str(int(x[i][1])-1)
        if (c[c.index(x[i][0])+1] + y) in x or (c[c.index(x[i][0])-1] + y) in x:
            z += 1
    return z

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
