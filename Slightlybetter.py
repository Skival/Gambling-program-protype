# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import random
print("Ok bud heres the deal");
print("The time is now to gamble");
totalbalance = int(input("How much money is in your wallet? "))
while True: 

    
    balance = int(input("How much money do you want to put in? "));
    
    multiplier = (int(input("What would you like to multiply it by? chances decrease with every number Ex: 2 = 50% 3 = 33.3% 4 = 25% 5 = 20% (5 is the max)")));
    if multiplier == (2):
        one = random.randint(1,100)
        two = random.randint(50,100)
        if two >= one:
            print("Congratulations, Your money has been doubled!")
            totalbalance = totalbalance + balance
            print("Here is what your finances look like")
            print("Whats in your wallet: " + str(totalbalance))
            print("What you have gained: " + str(balance*2))
            Ccontinue = input("Continue? (y/n)")
            if Ccontinue == "y" :
                continue
            else:
                break
        else:
            print("You have lost.")
            totalbalance = totalbalance - balance
            print("Here is what your finances look like")
            print("Whats in your wallet: " + str(totalbalance))
            print("What you have lost: " + str(balance))
            Ccontinue = input("Continue? (y/n)")
        if Ccontinue == "y" :
            continue
        else:
            break
    if multiplier == (3):
        one = random.randint(1,100)
        two = random.randint(1,33)
        if two <= one:
                print("Congratulations, Your money has been tripled!")
                totalbalance = totalbalance + balance
                print("Here is what your finances look like")
                print("Whats in your wallet: " + str(totalbalance))
                print("What you have gained: " + str(balance*3))
                Ccontinue = input("Continue? (y/n)")
                if Ccontinue == "y" :
                    continue
                else:
                    break
        else:
                print("You have lost.")
                totalbalance = totalbalance - balance
                print("Here is what your finances look like")
                print("Whats in your wallet: " + str(totalbalance))
                print("What you have lost: " + str(balance))
                Ccontinue = input("Continue? (y/n)")
                if Ccontinue == "y" :
                    continue
                else: 
                    break
    if multiplier == (4):
        one = random.randint(1,100)
        two = random.randint(1,25)
        if two <= one:
                print("Congratulations, Your money has been quadoupled!")
                totalbalance = totalbalance + balance
                print("Here is what your finances look like")
                print("Whats in your wallet: " + str(totalbalance))
                print("What you have gained: " + str(balance*4))
                Ccontinue = input("Continue? (y/n)")
                if Ccontinue == "y" :
                    continue
                else:
                    break
        else: 
                print("You have lost.")
                totalbalance = totalbalance - balance
                print("Here is what your finances look like")
                print("Whats in your wallet: " + str(totalbalance))
                print("What you have lost: " + str(balance))
                Ccontinue = input("Continue? (y/n)")
                if Ccontinue == "y" :
                    continue
                else:
                    break
    if multiplier == (5):
        one = random.randint(1,100)
        two = random.randint(1,20)
        if two <= one:
                print("Congratulations, Your money has been Quintupled!")
                totalbalance = totalbalance + balance
                print("Here is what your finances look like")
                print("Whats in your wallet: " + str(totalbalance))
                print("What you have gained: " + str(balance*5))
                Ccontinue = input("Continue? (y/n)")
                if Ccontinue == "y" :
                    continue
                else:
                    break
        else:
                print("You have lost.")
                totalbalance = totalbalance - balance
                print("Here is what your finances look like")
                print("Whats in your wallet: " + str(totalbalance))
                print("What you have lost: " + str(balance))
                Ccontinue = input("Continue? (y/n)")
                if Ccontinue == "y" :
                    continue
                else:
                    break