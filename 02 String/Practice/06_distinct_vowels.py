

def countVowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for ele in vowels:
        count += 1 if s.find(ele) != -1 else 0

    return count
