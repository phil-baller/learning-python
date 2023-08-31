words = "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"
start = words.find('@')
print(start)
end = words.find(' ', start)
print(end)

final = words[start + 1:end]
print('The domain is called: ',final)