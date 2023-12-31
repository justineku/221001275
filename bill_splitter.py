#KUBWIMANA Justine
#221001275
#Computer Science
import random

x = input("Enter the number of friends joining (including you):\n")
num = int(x)
users_dict = {}

if num > 0:
    print("Enter the name of every friend (including you), each on a new line:")
    for i in range(num):
        name = input()
        users_dict.update({name: 0})
    
print("Enter the total bill value:")
b = input()
bill = int(b)
for_each = int(bill) / num
for key, value in users_dict.items():
    users_dict[key] = round(for_each, 2)

print("Do you want to use the \"Who is lucky?\" feature? Write Yes/No:")
choice = input()
if choice == "yes":
    lucky_one = random.choice(list(users_dict))
    print(lucky_one, " is the lucky one!")

    for_remaining = bill / (num - 1)

    for key, value in users_dict.items():
        if key == lucky_one:
            users_dict[lucky_one] = 0
        else:
            users_dict[key] = round(for_remaining, 2)
else:
    print("No one is going to be lucky")

print(users_dict)
