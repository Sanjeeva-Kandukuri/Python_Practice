# Writing a Basic Regular Expression

# Example: Extracting Numbers from Text

import re

pattern = r"\d+"
text = "My phone number is 9392039661"
match = re.search(pattern, text)

if match:
    print("Match found:", match.group())
else:
    print("No match found.")


# Detailed Examples of Each RegEx Function

# 1. re.match() → Matches at the Start

import re

result = re.match(r"Hello", "Hello, World!")
print(result.group() if result else "No match.")


# 2. re.search() → Finds First Match Anywhere

import re

result = re.search(r"\d+", "My age is 25 and my ID is 1001")
print(result.group() if result else "No match.")


# 3. re.findall() → Finds All Matches

import re

result = re.findall(r"\d+", "I have 2 cats, 3 dogs, and 5 birds")
print(result)

# 4. re.finditer() → Finds Matches as Objects

import re

text = "Product IDS: 123, 456 789"

matches = re.finditer(r"\d+", text)

for match in matches:
    print(f"Match: {match.group()} at position {match.start()}")



# 5. re.fullmatch() → Checks Entire String

import re

result = re.fullmatch(r"\d{10}", "9392039661")

print("Valid" if result else "Invalid")


# 6. re.sub() → Replace Matches

# import re

text = "I love my cats"
result = re.sub(r"cats", "dogs", text)
print(result)

# 7. re.split() → Split String at Matches


import re

text = "apple, banana; orange  - grape"
result = re.split(r"[,;-]", text)
print(result)
