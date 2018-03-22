# Problem 2
# 10.0/10.0 points (graded)
# Assume s is a string of lower case characters.

# Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print
# ----------------Under line Code --------------------------------#
counter = 0
for i in range(len(s) - 2):
    if s[i] == 'b' and s[i + 1] == 'o' and s[i + 2] == 'b':
        counter += 1

print ('Number of times bob occurs is:', counter)

# ---------------------Under line result --------------------------#
# CORRECT