def replace_vowels_with_index(s: str):
    result = []

    for index,char in enumerate(s):
        if char.lower() in "aeiou":
            result.append(str(index))
        else:
            result.append(char)
    return " ".join(result)

print(replace_vowels_with_index("Hello"))