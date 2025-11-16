"""
This is an Adventure Game created by Jani Hari
To comment Ctrl+K+C 
To Uncomment Ctrl+K+U
Multi line comment Alt+Shift+A
"""

from time import sleep
# from stqdm import stqdm
from playsound import playsound
from time import time, ctime
from json import dumps
from sys import stdout
from os import system,name,remove
#import pyttsx3
#import string


#from class_Question import Questions
#from profanity

def str_fly(word,time=0.2,indent=0,sep=' '):
    word=word.replace('',sep)
    indent*=' '
    word=indent+word
    for char in word:
        stdout.write(char)
        #stdout.flush()
        sleep(time)
    #Alternative_Method is given below
    # word=word.replace('',sep)
    # indent*=' '
    # if indent!=0:
    #     print(indent,end='')
    # for a in word:
    #     print(a,end='')
    #     sleep(time)
    # print('') 

def clrmanpult(text,tc='white',tbg='black'):
    text_color=('black','red','green','yellow','blue','purple','cyan','white')
    text_color=enumerate(text_color,30)
    #style=enumerate(('nil','bold','under','-ve1','-ve2'),0)
    back_color=('black','red','green','yellow','blue','purple','cyan','white')
    back_color=enumerate(back_color,40)
    
    for search in text_color:
        if search[1]==tc:
            txt_color=search[0]
        else:
            continue
    #for c,d in style:
        #if tstyle==c:
            #return d
    for item in back_color:
        if item[1]==tbg:
            txt_back=item[0] 
        else:
            continue

    text=f'\033[{txt_color};{txt_back}m {text}'
    print(text+f"\033[{37};{40}m {''}")

def notify_clear():
    if name=='nt':     #Displays for windows Users
        system('cls')
    else:
        name=='posix'  #Displays for Mac and Linux Users
        system('clear')

t = time()
print('\n\n');print(ctime(t))


print('Disclaimer Before Beginning Anytime You Want to End Press Ctrl + C on your Keyboard')
sleep(3)
notify_clear()

def user_info():

    try:
        global user,newuser
        newuser=''
        user=input("\nEnter your name>> ")

        for search in user:
            if search.isalpha():
                newuser+=search
            else:
                continue 
        clrmanpult(f"\n>>>Welcome {newuser.title()}",tc='green')

    except Exception:
        str_fly("Please Enter your name To proceed>>")
        user_info()

def game_intro():
    
    playsound("Bertysolo.mp3", True)
    sleep(2)

    name='This_is_an_Adventure_game_designed_by_Jishnu\n'
    wait="Loading_the_game......\n"
    print('\n\n')
    str_fly(name,0.11,15)
    sleep(0.5);print()
    str_fly(wait,0.1,sep='')
    sleep(0.5)

    # for load in stqdm(range(100)):
    #     res=load+1  #Loading the banner
    #     sleep(0.25)  #time delay

def user_choice():

    try:
        sleep(3)
        what="\nThere are 3 Adventures in this game viz Adventure 1,2 and 3\n"
        str_fly(what,time=0.05,sep='')
        Adventures={
                    "Adventure_1":"In an Abandoned Castle",
                    "Adventure_2":"Jumanji 2.0",
                    "Adventure_3": "Mysterious Quest for Tresure"
                    }
        str_fly(dumps(Adventures,indent=4,separators=(' ','   ==>>   ')),time=0.02,sep='',indent=10)
        user_input=int(input("\mEnter Your Choice [1 or 2 or 3]>>> "))
        if user_input in (1,2,3):
            clrmanpult(f"\n\tAdventure {user_input} chosen",tc='yellow')
            sleep(1); Adventure(user_input)
        else:
            print(clrmanpult("\nThis Number is not Accepted!!!",tc='cyan'))
            while user_input not in [1,2,3]:
                user_input=int(input("Enter a Number>"))
            else:
                pass

    except ValueError:
        print(clrmanpult("\nEither enter 1 or 2 or 3",tc='green'))
        sleep(1)
        notify_clear()
        user_choice()

def Adventure(user_input):
    if user_input==1:
        Adventure_1()

    elif user_input==2:
        Adventure_2()
    else:
        Adventure_3()

def Adventure_1():
    print("Thank U Jani")

def Adventure_2():
    print("Thank U Jani")

def Adventure_3():
    print("Thank U Jani")

notify_clear()
user_info()
game_intro()
user_choice()


