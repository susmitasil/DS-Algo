def anagram (string1, string2):
    # s1 = list(string1)
    s2 = list(string2)

    i = 0
    j = 0
    while i < len(string1):
        # print(string1[i])
        
        if j <len(s2):
            # print(string1[i], s2[j])
            if string1[i] == s2[j]:
                s2.pop(j)
                continue
            j+=1
        elif j >=len(s2):
            j=0
            i+=1
        

    # print(s2)
    common = len(string2) - len(s2)
    result = (len(string1) - common) +len(s2)
    print(result)
    return result
            
anagram('apple', 'pear')
# anagram('rather', 'harder')
# anagram('married', 'admirer')
