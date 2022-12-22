#Algorithm
This algorithm works by first converting the input string
to a binary string. Each character is given a unique
binary representation according to its order in the set
of characters in the string. The length of each unique
representation is constant given by the length of the binary
value corresponding to the last char in the set. Then the locations
of 1s in the binary string are recorded and joined together, padding
with 0s where needed. For example, the indices:

0,13,28,42,1856

are recorded as:

00000013002800421856

The length of each integer plus any needed padding is represented
by variable name 'm'

This digit string is then broken up in pieces by size 4300
(max string to int conversion length in Python). Each piece
is converted to an integer. The length of the last piece
is record as 'k' in case it starts with 0(s). The list of integers,
represented by variable name 'y', the variable 'm', and the length of
the binary string 'n' is returned by the compressor.

To decompress, each integer in 'y' is converted to string and padded
to set each length as 4300. The last integer takes into account 'k'
when deciding how many 0s to pad. Each integer string is then joined into
one string and broken down into 'm' length pieces and converted to
integers, representing the original indices of 1s in the binary string.
The binary string can then be recomposed from the length of the binary
string 'n' and the indices of 1s.

To reform the original string, each unique binary value is remapped
to its original character.
