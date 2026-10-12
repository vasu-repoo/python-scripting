def reverse_even_word(sentence : str):
    words=sentence.split()
    result =[]
    for word in words :
        if len(word)%2!=0:
            rev = word[::-1]
            result.append(rev)
        else:
            result.append(word)

    return " ".join(result)

print(reverse_even_word("AI CAN CHANGE THE WORLD"))