from random import *
actualpwd = input("Hello User! Enter your exisiting password : ")
password = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
            'w', 'x', 'y', 'z',0,1,2,3,4,5,6,7,8,9,'!','@','#','$','%','&','*','-','_','=','+','/','A','B','C','D','E','F','G','H','I'
            ,'J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',' ']
myguesspass = ""
while (myguesspass != actualpwd):
    myguesspass = ""
    for i in range(len(actualpwd)):
        guessletter = password[randint(0, 73)]
        myguesspass = str(guessletter) + str(myguesspass)
    print(myguesspass)
print("We have guessed your password, it is :  ",myguesspass)
