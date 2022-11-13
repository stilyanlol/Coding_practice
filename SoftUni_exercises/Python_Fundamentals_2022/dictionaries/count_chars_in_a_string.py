new_dict = {}
sample_text = input()
for char in sample_text:
    if char != ' ':
        new_dict[char] = sample_text.count(char)
for key, value in new_dict.items():
    print(f'{key} -> {value}')
