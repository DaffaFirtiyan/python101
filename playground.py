import string
# x = range(7)
# for i in x:
#     print(i)

# print()

# for i in range(6, 11, 1):
#     print(i)

alphabet = list(string.ascii_lowercase)
word = ["t","o","m","a","t","o"]
known = []
for i in word:
    known.append("_")
print(known)

for i in range(0, len(word), 1):
    print(word[i] == "t")
    print(word.index("t"))
    # word.insert(1, "l")
    # ind = word.index("t")
    # print(f"{ind} {i}")
print(word)

# letter = "o"
# for i in word:
#     if letter in word:
#         print(word.index(letter))
#         word.remove(letter)
#         print("removed")

# list = ["_" , "_"]
# print("_" in list)

print(type(alphabet))
print(alphabet)