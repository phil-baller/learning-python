romeo = open('romeo.txt', 'r')
decoding = romeo.read()  
general = decoding.strip()
unique_words = []
count = 0

for v in general:
    all_words = v.split()
    if all_words not in unique_words:
        unique_words.append(all_words)  
    count += 1

print(unique_words)
print(count)
'''unique_words.sort()
for x in unique_words:
    print(x)    
'''