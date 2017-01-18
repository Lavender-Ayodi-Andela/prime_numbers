def words(x):
    #split words in x into list
    wlist = x.split()  
    #empty dictionary 
    diction = {}
    for word in wlist:     
        if word in diction:  
            diction[word] += 1
        else:
            diction[word] = 1
     
    for word in sorted(diction, key = diction.get):
        print ("%s:'%d'" % (word, diction[word]))
        print diction