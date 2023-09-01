romeo = open('romeo.txt')

unique_words = list()
count = 0

for v in romeo:
    main_words = v.rstrip()
    if v in main_words:
        all_words = v.split()
        print(all_words)
    count += 1

print(count)
'''unique_words.sort()
for x in unique_words:
    print(x)    
'''