def match_words(words):
    ctr = 0
    list = []
    for word in words:
        if len(word)>1 and word[0] == word[-1]:
            ctr +=1
            list.append(word)
    print("List of words which has first and last character same is, /n",list)
    return(ctr)
count = match_words(['abc','cfc','xyz','aha','1221'])
print("List of words which has first and last character same is, ",count)
