id,height,species,age
0,107,Beech,54
1,726,Elder,67
2,378,Willow,42
3,475,Hawthorn,59
4,599,Maple,89
5,511,Holly,84
6,874,Oak,49
7,296,Elder,13
8,527,Hazel,34
9,624,Alder,11
10,621,Holly,49
11,304,Poplar,98
12,531,Ash,88
13,260,Poplar,69
14,873,Birch,25
15,916,Ash,46
16,298,Alder,47
17,785,Birch,94
18,994,Hazel,12
19,481,Elm,70
20,596,Cherry,35
21,359,Birch,56
22,932,Elm,28
23,672,Beech,33
24,757,Elder,60
25,389,Beech,39
26,408,Hazel,15
27,887,Beech,18
28,477,Holly,13
29,586,Maple,56
30,556,Elder,49
31,496,Maple,15
32,554,Ash,17
33,391,Beech,11
34,109,Oak,33
35,707,Willow,38
36,581,Cherry,42
37,734,Hawthorn,34
38,235,Cherry,100
39,564,Cherry,94
40,274,Elm,80
41,634,Ash,18
42,395,Holly,46
43,517,Elder,17
44,654,Ash,63
45,599,Birch,30
46,436,Elm,29
47,522,Maple,24
48,607,Oak,51
49,309,Holly,16
50,610,Oak,93
51,848,Poplar,38
52,801,Holly,60
53,433,Hazel,60
54,372,Elder,34
55,761,Elm,50
56,590,Elder,31
57,215,Cherry,75
58,709,Cherry,84
59,239,Ash,64
60,895,Birch,46
61,482,Ash,57
62,543,Maple,21
63,883,Birch,16
64,453,Ash,87
65,814,Willow,92
66,826,Ash,49
67,676,Hazel,47
68,696,Elder,45
69,776,Ash,35
70,855,Elm,23
71,292,Birch,38
72,347,Elder,74
73,343,Elder,99
74,693,Hawthorn,58
75,645,Maple,38
76,986,Oak,92
77,878,Elm,20
78,974,Holly,37
79,998,Hazel,80
80,183,Oak,66
81,192,Maple,43
82,486,Birch,80
83,549,Oak,13
84,405,Ash,43
85,129,Elder,73
86,610,Oak,91
87,536,Elder,58
88,858,Birch,40
89,962,Oak,62
90,129,Birch,23
91,954,Oak,80
92,697,Beech,98
93,691,Willow,67
94,162,Oak,98
95,848,Holly,96
96,883,Willow,57
97,732,Hazel,22
98,286,Hawthorn,31
99,995,Birch,52
100,904,Maple,83
101,678,Oak,33
102,243,Maple,43
103,876,Maple,63
104,649,Alder,90
105,729,Elm,95
106,261,Ash,23
107,620,Elm,62
108,452,Holly,23
109,594,Maple,66
110,979,Elm,12
111,931,Oak,32
112,802,Birch,100
113,935,Oak,60
114,776,Elder,57
115,510,Poplar,89
116,569,Hawthorn,54
117,270,Ash,98
118,225,Willow,37
119,726,Holly,71
120,377,Elm,36
121,887,Maple,19
122,521,Poplar,82
123,955,Birch,26
124,140,Elm,46
125,249,Beech,74
126,763,Holly,27
127,691,Poplar,22
128,203,Alder,33
129,349,Alder,83
130,462,Oak,51
131,260,Alder,67
132,766,Poplar,14
133,209,Hawthorn,69
134,807,Hazel,77
135,484,Elder,79
136,898,Poplar,36
137,237,Poplar,83
138,919,Willow,15
139,974,Hazel,45
140,929,Willow,77
141,261,Birch,90
142,697,Alder,79
143,681,Birch,42
144,863,Alder,40
145,198,Holly,29
146,836,Maple,38
147,475,Alder,95
148,355,Beech,58
149,824,Birch,100

animals = [
    {'species': 'zebra', 'name': 'Penelope'},
    {'species': 'penguin', 'name': 'Jenn'},
    {'species': 'elephant', 'name': 'Harris'},
    {'species': 'flamingo', 'name': 'Florence'},
]
for beast in animals:
    print(beast['species'])


with open('people.txt', 'w+') as text_file:
    chocolates = 'White \nMilk \nDark'
    text_file.write(chocolates)


   with open('people.txt', 'r') as text_file:
    contents = text_file.read()
print(contents)

user_input = input('What do you need to do? ')
with open('todo.txt', 'r') as text_file:
    contents = text_file.read()
print(contents)
contents = contents + '\n' + user_input
with open('todo.txt', 'w+') as text_file:
    text_file.write(contents)


   import csv
field_names = ['name', 'age']
data = [
    {'name': 'Jill', 'age': 32},
    {'name': 'Sara', 'age': 28},
]
with open('team.csv', 'w+') as csv_file:
    spreadsheet = csv.DictWriter(csv_file, fieldnames=field_names)
    spreadsheet.writeheader()
    spreadsheet.writerows(data)


import csv
name = input('name: ')
age = input('age: ')
field_name = ['name', 'age']
data = [
    {'name': name, 'age': age},
    {'name': name, 'age': age},
    {'name': name, 'age': age}
]
with open('names_and_ages.csv', 'w+') as csv_file:
    spreadsheet = csv.DictWriter(csv_file, fieldnames=field_name)
    spreadsheet.writeheader()
    spreadsheet.writerows(data)

import csv
with open('team.csv', 'r') as csv_file:
    spreadsheet = csv.DictReader(csv_file)
    for row in spreadsheet:
        print(dict(row))
7:50
**Exercise 5.2:** This program is supposed to read data about trees from a file to find the shortest tree. Complete the program adding code to open `trees.csv`.
The `trees.csv` file included with your student guides. Save the csv file in the same folder as your Python program.
spreadsheet = # Add code to open the csv file
heights = []
for row in spreadsheet:
    tree_height = row['height']
    heights.append(tree_height)
shortest_height = min(heights)
print(shortest_height) (edited)


import csv
with open('trees.csv', 'r') as csv_file:
    spreadsheet = csv.DictReader(csv_file)
    heights = []
    for row in spreadsheet:
        print(row)
        tree_height = row['height']
        heights.append(tree_height)
shortest_height = min(heights)
print(shortest_height)

import requests
from pprint import pprint
pokemon_number = input("What is the Pokemon's ID? ")
url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
response = requests.get(url)
print(response)
pokemon = response.json()
pprint(pokemon)

#Exercise 5.3: Get the height and weight of a specific Pokemon and print the output
Extension: Print the names of all of a specific Pokemon's moves

import requests
from pprint import pprint
pokemon_number = input("What is the Pokemon's ID? ")
url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
response = requests.get(url)
#print(response)
pokemon = response.json()
#pprint(pokemon)
print(pokemon['name'])
print(pokemon['height'])
print(pokemon['weight'])
moves = pokemon['moves']
for move in moves:
    print(move)




































































































    






















    