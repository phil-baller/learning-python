import re

"""phone_number = "John: 1-966-847-3131 Michelle: 54-908-42-42424"

all_numbers = re.findall(b'\d{1,2}-\d{3}-\d{2,3}-\d{4,}', phone_number)

print(all_numbers)"""

my_links = "Just check out this link: www.amazingpics.com. It has amazing photos!"
my_string = "My&name&is#John Smith. I%live$in#London."
data = re.sub(r"[&$#%]", ' ', my_string)

print(data)