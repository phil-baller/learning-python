'''
index = 0
while index < len(letter):
    print(letter[index])
    index = index + 1
'''
def count_letter(text, find):
    count = 0
    for v in text:
        if find in v:
            count = count + 1
    print(v ,'has been found', count, 'times')

sentence = input('Enter some text here: ')
find_word = input('Enter letter you want to find: ')

count_letter(sentence, find_word)