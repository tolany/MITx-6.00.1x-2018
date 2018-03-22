#Problem 1
#10.0/10.0 points (graded)
#Assume s is a string of lower case characters.
#
#Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:

# ----------------Under line Code --------------------------------#
counter = 0

for i in s:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        counter += 1

print('Number of vowels:', counter)

# ---------------------Under line result --------------------------#
# CORRECT