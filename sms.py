import http.client
import sys
import os
import sqlite3

admins = { 'Ras':'Bere',
           'Py':'6666',
           'Emmuel':'1592'}

def clear_screen():
	os.system("cls" if os.name == "nt" else "clear")


def msg():
    conn = http.client.HTTPConnection("api.msg91.com")
    msg = input("MESSAGE TO BE SENT: ")
    my_list = msg.split()
    message = "%20".join(my_list)
    return message

def send():
    clear_screen()
    print("""
          *********************************************************
          +           WELCOME TO SUPER TEXT BOT                   +
          +    SEND TEXT MESSAG TO OVER A THOUSAND CLIENTS        +
          +                                                       +
          +   made  by: BrainyITSolutions                         +
          ********************************************************
          """)
    final_text = msg()

    conn = http.client.HTTPConnection("api.msg91.com")

    conn.request("GET", "/api/sendhttp.php?sender=ELISHA&route=4&mobiles=263776484278&authkey=API AUTH KEY&encrypt=&country=263&message={}".format(final_text))

    res = conn.getresponse()
    data = res.read()

    data.decode("utf-8")
    print("message sent succesfully!!")
    print()

    buda = input("Would you like to send another message? (Y/N): ")
    if buda != 'n':
        send()
    else:
        clear_screen()
        print()
        print()
        print("##############################################")
        print("# Thank you For Using SUPER TEXT BOT         #")
        print("# software developed by brainy IT solutions  #")
        print("# Visit our website for more services        #")
        print("#         WWW.BRAINYSOLUTIONS.CF             #")
        print("##############################################")
        exit()

def login():
    clear_screen()
    print("""
          *************************************************
          +                 SUPER TEXT                    +
          +    "No.1 DIGITAL MARKETING SOLUTION"          +
          +                                               +
          + developed  by: Brainy IT Solutions            +
          *************************************************

          """)
    print()
    login = input('Username: ').title()
    passwd = input('Password: ')

    if login in admins:                               #chex to see if login input == one in list admins
        if admins[login]== passwd:                   #chex if login name in admin == pwd entered
            print('Succesfully Logged in ,',login)
            while True:
                send()
        elif admins[login] != passwd:
            #failed
            failed()

    elif login not in admins :
        #failed func
        failed()


def failed():
        clear_screen()
        print()
        print("##############################################")
        print('   username and password is incorrect   ')
        print("##############################################")
        print()

        buda = input("Would you like to send another message? (Y/N): ")

        if buda != "n":
            login()
        else:
            clear_screen()
            print()
            print()
            print("##############################################")
            print("# Thank you For Using SUPER TEXT BOT         #")
            print("# software developed by brainy IT solutions  #")
            print("# Visit our website for more services        #")
            print("#         WWW.BRAINYSOLUTIONS.CF             #")
            print("#         ZIM'S NO.1 ICT CONSULTANTS         #")
            print("##############################################")
            exit()

login()
