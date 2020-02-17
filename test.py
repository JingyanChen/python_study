"""Count words."""

def count_words(s, n):
    """Return the n most frequently occuring words in s."""
    
    # TODO: Count the number of occurences of each word in s
    wordlist = s.split(' ')
    #print(wordlist)

    wordlistNorepeat = list(set(wordlist))
    #print(wordlistNorepeat)

    worddict = {}
    norepeat_num = 0
    for j in range(0,len(wordlistNorepeat)):
        for i in range(0,len(wordlist)):
            if(wordlistNorepeat[j] == wordlist[i]):
                norepeat_num += 1
        worddict[wordlistNorepeat[j]] = norepeat_num
        norepeat_num = 0

    #print("dict:\r\n")
    #print(worddict)
    
    # TODO: Sort the occurences in descending order (alphabetically in case of ties)
    
    worddict_sorted = sorted(worddict.items(), key=lambda item:item[1] , reverse=True) # using lambda 
    print(worddict_sorted)

    # TODO: Return the top n most frequent words.
    
    top_n = worddict_sorted[:n]

    return top_n


def test_run():
    """Test count_words() with some inputs."""
    #print(count_words("betty bought a bit of butter but the butter was bitter", 3))
    print(count_words("betty bought a bit of butter but the butter was bitter", 3))


if __name__ == '__main__':
    test_run()
