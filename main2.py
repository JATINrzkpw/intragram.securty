from random import *
user_pass=input("inter you password:")
password=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'],['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'], ['1','2','3','4','5','6','7','8','9','0']
while(guess!=user_pass):
    guess=""
    for letter in range (len(user_pass)):
        guess_letter=password[(0,25)]
        guess=str(guess_letter)+str(guess)
        print(guess)
print("your password is",guess)
 