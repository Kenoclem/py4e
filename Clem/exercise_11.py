def count(word, char):
    l = len(word)

    i = 0
    occ = 0
    while i < l:
        if word[i] == char:
            occ +=1
        i += 1
    return occ

w = input('Enter a string: ')
c = input('Enter a character:')

print('Number of occurences:', count(w, c))