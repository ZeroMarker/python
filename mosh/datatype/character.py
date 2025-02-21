from pprint import pprint

sentence = "Nobody care about what we live well or bad."
chars = {}

for i in sentence:
    if i in chars:
        chars[i] += 1
    else:
        chars[i] = 1

pprint(chars, width=1)

char_sorted = sorted(chars.items(),
                     key=lambda kv: kv[1],
                     reverse=True)

print(char_sorted[0])
