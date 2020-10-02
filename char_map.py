"""
Defines two dictionaries for converting 
between text and integer sequences.
"""


char_map_str = """
' 0
<SPACE> 1
ব 2
া 3
ং 4
ল 5
দ 6
ে 7
শ 8
য 9
় 10
ি 11
ত 12
্ 13
ন 14
এ 15
ধ 16
র 17
ণ 18
ক 19
ড 20
হ 21
উ 22
প 23
জ 24
অ 25
থ 26
স 27
ষ 28
ই 29
আ 30
ছ 31
গ 32
ু 33
ো 34
ও 35
ভ 36
ী 37
ট 38
ূ 39
ম 40
ৈ 41
ৃ 42
ঙ 43
খ 44
ঃ 45
১ 46
৯ 47
৬ 48
০ 49
২ 50
চ 51
ঘ 52
ৎ 53
৫ 54
৪ 55
ফ 56
ৌ 57
৮ 58
ঁ 59
য় 60
৩ 61
ঢ 62
ঠ 63
৭ 64
ড় 65
ঝ 66
ঞ 67
ঔ 68
ঈ 69
v 70
b 71
s 72
ঐ 73
2 74
0 75
1 76
4 77
f 78
o 79
t 80
a 81
l 82
w 83
r 84
d 85
c 86
u 87
p 88
n 89
g 90
ঋ 91
i 92
z 93
m 94
e 95
ঊ 96
h 97
x 98
3 99
5 100
y 101
9 102
ৗ 103
j 104
œ 105
8 106
ঢ় 107
k 108
ৰ 109
"""
# the "blank" character is mapped to 28

char_map = {}
index_map = {}
for line in char_map_str.strip().split('\n'):
    ch, index = line.split()
    char_map[ch] = int(index)
    index_map[int(index)+1] = ch
index_map[2] = ' '