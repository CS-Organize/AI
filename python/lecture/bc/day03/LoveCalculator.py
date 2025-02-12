name1 = input("What is your name?\n").lower()
name2 = input("What is their name?\n").lower()

combined_name = name1 + name2

# t = r = u = e = l = o = v = 0

# for i in name1 + name2:
#   if (i == 't'):
#     t += 1
#   elif (i == 'r'):
#     r += 1
#   elif (i == 'u'):
#     u += 1
#   elif (i == 'e'):
#     e += 1
#   elif (i == 'l'):
#     l += 1
#   elif (i == 'o'):
#     o += 1
#   elif (i == 'v'):
#     v += 1

t = combined_name.count("t")
r = combined_name.count("r")
u = combined_name.count("u")
e = combined_name.count("e")
l = combined_name.count("l")
o = combined_name.count("o")
v = combined_name.count("v")

print(f"t: {t}, r: {r}, u: {u}, e: {e}, l: {l}, o: {o}, v: {v}")

score = (int(t) + int(r) + int(u) + int(e)) * 10 + (int(l) + int(o) + int(v) + int(e))

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
