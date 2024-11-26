data = "なまむぎなまごめなまたまご"
counter = {}
for character in data:
    if character not in counter:
        counter[character] = 0
    counter[character] += 1    
for character, number in counter.items():
    print(f'{character}: {number}')
    
    