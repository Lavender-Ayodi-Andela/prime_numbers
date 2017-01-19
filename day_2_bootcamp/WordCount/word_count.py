def words(x):
    #split words in x into list
    #empty dictionary
    #counts no. of word occurence and prints it alongside word in dictionary
    wlist = x.split()  
     
    diction = {}
    for word in wlist:     
        if word in diction:  
            diction[word] += 1
        else:
            diction[word] = 1
     
    for word in sorted(diction, key = diction.get):
        print ("%s:'%d'" % (word, diction[word]))
        print diction