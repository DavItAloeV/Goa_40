#   /\/\  1  /\/\   #

num = []
for i in range(1,101):
    num.append(i + 5)
print(sum(num))

#   /\/\  2  /\/\   #

even = []
odd = []

for i in range(1, 101):
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print(even)
print(odd)

#   /\/\  3  /\/\   #

num = []

for i in range(1, 101):
    if i % 5 == 0:
        num.append(i)

print(num)

#   /\/\  done!  /\/\   #