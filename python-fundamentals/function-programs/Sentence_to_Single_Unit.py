#input =tHis IS gOING To bE eaSY
#output =ThisIsGoingToBeEasy

def sentence_to_word(s):
    word=s.split()
    result=[]

    for words in word:
        result.append(words.capitalize())

    return "".join(result)

print(sentence_to_word("tHis IS gOING To bE eaSY"))