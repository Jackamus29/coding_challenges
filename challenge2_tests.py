"""This module tests the solution to the second challenge."""

from challenge2 import chessercise


def test_chessercise(test_input, expected_output):
    """Helper function that tests the solution against the expected."""
    result = chessercise(*test_input)
    if set(result) == set(expected_output.split(", ")):
        print "PASS\n"
    else:
        print "FAIL\n"
        print "\tINPUT:\t\t\t%s" % str(test_input)
        print "\tEXPECTED OUTPUT:\t%s" % expected_output
        print "\tACTUAL OUTPUT:\t\t%s\n" % ", ".join(result)

# KNIGHT TESTING #
print "KNIGHT TESTING"
# Test Case 1 (test given in description of problem)
print "Test Case #1:",
test_chessercise(("KNIGHT", "d2"), "b1, f1, b3, f3, c4, e4")

# Test Case 2 (test knight position in bottom left)
print "Test Case #2:",
test_chessercise(("KNIGHT", "a1"), "b3, c2")

# Test Case 3 (test knight position in center)
print "Test Case #3:",
test_chessercise(("KNIGHT", "e4"), "d2, f2, c3, c5, d6, f6, g5, g3")

# Test Case 4 (test knight position in top right)
print "Test Case #4:",
test_chessercise(("KNIGHT", "h8"), "f7, g6")

# Test Case 5 (test knight move to bottom left)
print "Test Case #5:",
test_chessercise(("KNIGHT", "b3"), "c1, a1, a5, c5, d4, d2")

# Test Case 6 (test knight move to top right)
print "Test Case #6:",
test_chessercise(("KNIGHT", "f7"), "d8, h8, h6, g5, e5, d6")

# ROOK TESTING #
print "ROOK TESTING"
# Test Case 7 (test rook position in bottom left)
print "Test Case #7:",
test_chessercise(
    ("ROOK", "a1"),
    "a2, a3, a4, a5, a6, a7, a8, b1, c1, d1, e1, f1, g1, h1"
)

# Test Case 8 (test rook position in center)
print "Test Case #8:",
test_chessercise(
    ("ROOK", "d5"),
    "d1, d2, d3, d4, d6, d7, d8, a5, b5, c5, e5, f5, g5, h5"
)

# Test Case 9 (test rook position in top right)
print "Test Case #9:",
test_chessercise(
    ("ROOK", "h8"),
    "h1, h2, h3, h4, h5, h6, h7, a8, b8, c8, d8, e8, f8, g8"
)

# BISHOP TESTING #
print "BISHOP TESTING"
# Test Case 10 (test bishop position in bottom left)
print "Test Case #10:",
test_chessercise(
    ("BISHOP", "a1"),
    "b2, c3, d4, e5, f6, g7, h8"
)

# Test Case 11 (test bishop position in center)
print "Test Case #11:",
test_chessercise(
    ("BISHOP", "d5"),
    "a8, b7, c6, e4, f3, g2, h1, a2, b3, c4, e6, f7, g8"
)

# Test Case 12 (test bishop position in top right)
print "Test Case #12:",
test_chessercise(
    ("BISHOP", "h8"),
    "a1, b2, c3, d4, e5, f6, g7"
)

# QUEEN TESTING #
print "QUEEN TESTING"
# Test Case 13 (test queen position in bottom left)
print "Test Case #13:",
test_chessercise(
    ("QUEEN", "a1"),
    ("b2, c3, d4, e5, f6, g7, h8, " +
     "a2, a3, a4, a5, a6, a7, a8, b1, c1, d1, e1, f1, g1, h1")
)

# Test Case 14 (test queen position in center)
print "Test Case #14:",
test_chessercise(
    ("QUEEN", "d5"),
    ("a8, b7, c6, e4, f3, g2, h1, a2, b3, c4, e6, f7, g8, " +
     "d1, d2, d3, d4, d6, d7, d8, a5, b5, c5, e5, f5, g5, h5")
)

# Test Case 15 (test queen position in top right)
print "Test Case #15:",
test_chessercise(
    ("QUEEN", "h8"),
    ("a1, b2, c3, d4, e5, f6, g7, " +
     "h1, h2, h3, h4, h5, h6, h7, a8, b8, c8, d8, e8, f8, g8")
)

print "Done Testing."
