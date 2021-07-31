import random

from requests import get

import argparse

import os

import time

from api import Api

from datetime import datetime

import sys

def check():

    try:

        

        internet = True

        print("Started to Bomb On "+str(target)+" With "+str(msgs)+" Messages\n\n")

    except:

        print(color)

        print("\tYou are not Conected to Internet. Please Turn on your Mobile Data")

        exit()

def banner():

    os.system('''

	toilet --gay Crunch	print()

printf "------------------------------------------------------------------\n\n"

	printf "\e[1;101m\tCrunch is Developed to Tackle\n\tOnline Bullying & Harrasment \e[0m\e[1;101m\e[0m\n"

	printf "\n\e[1;32m\tThis Tool is Developed to Slow Down the Phone\n\tBy Bombing Thousands of CALLS & SMSs \e[0m \e[0m\e[1;32m\e[0m\n\n"

	printf "\tCrunch is Developed By Sahaja Verma\n\tEspecially to Fight Cyber-Bullying & Harrasment\n\n"

	printf "\n"

	printf "\e[101m\e[1;77m\t Disclaimer: Dont Use to Bully or Tease,\n\tthe Developer of this Tool is \e[0m\n\t"

	printf "\e[101m\e[1;77m Monitoring the Statistics & Frequencies \e[0m\n"

	printf "\n"

	printf "------------------------------------------------------------------\n"

	printf "\n"

	''')

colors=['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;34m','\033[1;35m','\033[1;36m']

color = random.choice(colors)

print('\n\n')

parser = argparse.ArgumentParser()

parser.add_argument('-t', type=str, default=0, help="-t = Targets Phone Number ")

parser.add_argument('-m', type=int, default=650, help="-m = Number of Messages")

args = parser.parse_args()

target = str(args.t)

msgs = args.m

now = datetime.now()

dt_string = now.strftime("%d/%m/%Y %H:%M")

#print("date and time =", dt_string)	

if  target == '':

    banner()

    print("Please Enter the Number of Target with -t Argument.")

elif msgs == 0:

    banner()

    print("Please Enter the Number of Messages with -m Argument")

elif msgs>70000000:

    banner()

    print(color)

    print("You Can't Send More than 70000000 Messages at a Time")

elif len(target)==10 and msgs<=70000000:

        print(color)

        banner()

        print("\n")

        check()

        Api.infinite(target, color, msgs)

        print("\n")

        print("Dropped "+str(msgs)+" Calls & Messages on "+str(target)+" at "+str(dt_string))

else:

    print("Please Enter the Correct & Valid Phone Number")
