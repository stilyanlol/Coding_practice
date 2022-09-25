new_word = []

while True:
    word = input()
    if word == "End":
        break
    if word == "SoftUni":
        continue
    for char in word:
        new_word.append(char * 2)
    print("".join(new_word))
    new_word = []
