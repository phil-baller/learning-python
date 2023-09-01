romeo = open('romeo.txt')
    
def decoding(reading, words):
    delimiter = ' '
    count = 0
    for v in reading:
        decoding = v.split(delimiter)
        for x in decoding:
            if x not in words:
                words.append(x)
                count += 1
    words.sort()
    print(words)
    print(count)


unique_words = []

decoding(romeo, unique_words)