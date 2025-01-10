print("Welcome to Your Fairy Name 2000")
print("Answer the questions to find out your fairy name")
ans = input("black (b) or green (g)")
if ans == "b":
    ans = input("breakfast (bf) or brunch (br) ?")
    if ans == "bf":
        ans = input("apples (a) or bananas (b)?")
        if ans == "a":
            print("Your first name is Ping")
        else:
            print("Your first name is Laurel")
    else:
        ans = input("Gold (g) or silver (s)?")
        if ans == "g":
            print("Your first name is Shiny")
        else:
            print("Your first name is Sterling")
else:
    ans = input("lunch (l) or dinner (d) ?")
    if ans == "l":
        ans = input("trees (t) or bushes (b)?")
        if ans == "t":
            print("Your first name is Leaf")
        else:
            print("Your first name is Branch")
    else:
        ans = input ("Watches (w) or bracelets (b)?")
        if ans == "w":
            print("Your first name is Chrono")
        else:
            print("Your first name is Van")
