import string
import random
if __name__ =="__main__":
    s1= string.ascii_uppercase
    s2= string.digits
    s3= string.punctuation
    s4= string.ascii_lowercase
    pl = input("Enter length of password:")
    plu = input("Enter no of upper letters:")
    pll = input("Enter no of lower letters:")
    pld = input("Enter no of digits:")
    plp = input("Enter no of punctuations:")


    try:
        pl = int(pl)
        plu = int(plu)
        pld = int(pld)
        plp = int(plp)
        pll = int(pll)
    except ValueError:
        print("Invalid! Please enter a valid number.")
        exit()
    s=[]
    if((plu+pld+plp+pll)==pl):

        for i in range(1,plu+1):
            a=random.choice(s1)
            s+=a
        for i in range(1,pld+1):
            a=random.choice(s2)
            s+=a
        for i in range(1,plp+1):
            a=random.choice(s3)
            s+=a
        for i in range(1,pll+1):
            a=random.choice(s4)
            s+=a
        print("your password is:\n")
        print("".join(s[0:pl]))
    else:
        print("Please match the entered password length")


