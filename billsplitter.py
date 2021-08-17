# write your code here
import random
result = {}


def create():
    friend = int(input("Enter the number of friends joining (including you):\n"))
    if friend <= 0:
        print("\nNo one is joining for the party")
    else:
        print("\nEnter the name of every friend (including you), each on a new line:")
        for i in range(friend):
            i = input("")
            result[i] = 0
        money = int(input("\nEnter the total bill value:\n"))
        lucky = input('\nDo you want to use the "Who is lucky?" feature? Write Yes/No:\n')
        if lucky == "No":
            print("\nNo one is going to be lucky\n")
            money_split = round(money / friend, 2)
            if str(money_split)[-1:] == "0":
                money_split = int(money_split)
            for i in result.keys():
                result[i] = money_split
            print()
            print(result)
        elif lucky == "Yes":
            lucky_list = [i for i in result.keys()]
            lucky_jj = random.choice(lucky_list)
            print(f"\n{lucky_jj} is the lucky one!")
            money_split = round(money / (friend - 1), 2)
            if str(money_split)[-1:] == "0":
                money_split = int(money_split)
            for i in result.keys():
                result[i] = money_split
            result[lucky_jj] = 0
            print()
            print(result)


create()
