"""
Given a seven-digit phone number, return all the character combinations
that can be generated according to the following mapping:

Graph

Return the combinations in the lexicographical order.

Example One

{
"phone_number": "1234567"
}
Output:

[
"adgjmp",
"adgjmq",
"adgjmr",
"adgjms",
"adgjnp",
...
"cfilns",
"cfilop",
"cfiloq",
"cfilor",
"cfilos"
]
First string "adgjmp" in the first line comes from the first characters mapped
to digits 2, 3, 4, 5, 6 and 7 respectively. Since digit 1 maps to nothing,
nothing is appended before 'a'. Similarly, the fifth string "adgjnp" generated
from first characters of 2, 3, 4, 5 second character of 6 and first character of 7.
All combinations generated in such a way must be returned in the lexicographical order.


"""