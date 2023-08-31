words = 'X-DSPAM-Confidence:0.8475'

start = words.find(':')
print(start)

end = words.find('5',start)

final = words[start + 1:end + 1]

print('Our Extracted word here is: ', final)
print("The conversion above to float gives the output: ", final)