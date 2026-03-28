"""
DocStrings:
Dictinoaries store connections between pieces of information.
Each item in a dictonary is a key-value pair.
"""

"""A simples dictionay"""

alien = {"color": "green", "points": 5}

"""Accessing a value"""
print(f"The alien's color is {alien['color']}.")

"""Adiing a new key-value pair"""
alien["x_position"] = 0

"""Looping through all key-value pairs"""
fav_numbers = {"eric": 7, "ever": 4, "erin": 47}

for name, number in fav_numbers.items():
    print(f"{name} loves {number}")

"""Looping through all key"""
fav_numbers = {"eric": 7, "ever": 4, "erin": 47}

for name in fav_numbers.keys():
    print(f"{name} loves")

"""Looping through all values"""
fav_numbers = {"eric": 7, "ever": 4, "erin": 47}

for number in fav_numbers.values():
    print(f"loves {number}")

"""--------------------------------------------------------------------"""

eempty_dict = {}
a = {"one": 1, "two": 2, "three": 3}

# Para ver o valor de uma chave
print(a["one"])

# Para ver as chaves
print(a.keys())

# Para ver os valores
print(a.values())

# Para atualizar e ver o novo estado
a.update({"four": 4})
print(a.keys())
print(a["four"])

"""-------------------------------------------------------------------"""

johndict = {"fisthname": "Tiago", "lastname": "Rodrigues", "age": 39}

x = johndict.items()
print(x)

for key, value in johndict.items():
    print(f"{key}, {value}")


"""Is or not is"""
languages = ["html", "go", "rust", "javascript", "python"]

language_dict = {lang: ("l" not in lang) for lang in languages}
# key is the language & bool is value (no offense for html...)

print(language_dict)

# Dictionary comprehension avoid this:

language_dict2 = {}

for e in languages:
    if "l" not in e:
        language_dict2[e] = True
    else:
        language_dict2[e] = False

print(language_dict2)

"""Create a dictionary with if but faster"""
language_dict3 = {lang: True for lang in languages if "l" not in lang}

print(language_dict3)
