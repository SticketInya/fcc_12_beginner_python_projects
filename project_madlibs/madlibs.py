import random

noun = input("Noun: ")
adjective = input("Adjective: ")
madlibs = [
    f"Today I went to the zoo. I saw a(n) {adjective} {noun} jumping up and down in its tree.",
    f"I got some peanuts and passed them through the cage to a {adjective} grey {noun}.",
    f"Feeding the {noun} made me hungry. I went to get a {adjective} scoop of ice cream.",
    f"Today, my fabulous {noun} went to a(n) {adjective} amusement park."
]

print(madlibs[random.randint(0, 3)])