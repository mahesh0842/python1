def pangram(pharse):
    letters={'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}
    pharse = set(pharse.lower())

    if pharse >= letters:
        return True
    else :
        return False

if pangram(pharse==True):
    print("true")
print(pangram('the quick brown fox jumps over the lazy dog'))   