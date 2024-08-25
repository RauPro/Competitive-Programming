n = input()
s = input()

while s.count("()"):
    s = s.replace("()", "(1)")

while s.count("))"):
    s = s.replace("))", ")+1)")

while s.count(")("):
    s = s.replace(")(", ")*(")
#print(s)
print(eval(s))
