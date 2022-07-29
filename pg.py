#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from getpass import getuser
from platform import system
from os import mkdir, replace, getcwd
from sys import argv
from secrets import choice
from numpy import append
from json import load


def PassGen(amount = 8, count = 10, special = True, name = pass, is_file = False):
    user_name = getuser()
    if system() == "Linux":
        try:

            js = open("/home/" + user_name + "/.config/PassGen/alph.json", "r")

        except BaseException:

            mkdir("/home/" + user_name + "/.config/PassGen")
            replace(
                getcwd() +
                "/alph.json",
                "/home/" +
                user_name +
                "/.config/PassGen/alph.json")
            print(
                "the file alph.json has been moved to a /home/" +
                user_name +
                "/.config/PassGen/")

            js = open("/home/" + user_name + "/.config/PassGen/alph.json", "r")

    elif "Windows" in system():
        try:
            js = open("C:/Users/" + user_name + "/PassGen/alph.json", "r")

        except BaseException:

            mkdir("C:/Users/" + user_name + "/PassGen")
            replace(
                getcwd() +
                "/alph.json",
                "C:/Users/" +
                user_name +
                "/PassGen/alph.json")
            print(
                "the file alph.json has been moved to a C:/Users/" +
                user_name +
                "/PassGen/")

            js = open("C:/Users/" + user_name + "/PassGen/alph.json", "r")

    full_alph = load(js)
    simb = full_alph["alph"]
    s_simb = full_alph["s_alph"]

    if special == "True":
        us_alph = append(simb, s_simb)

    else:
        us_alph = simb

    lst = ""
    password = ""

    for i in range(count):
        password = ""
        for j in range(amount):
            password += choice(us_alph)
        lst += password + "\n"
    if is_file == "True":
        file = open(name + ".txt", "w")
        file.write(lst)
    print()
    print(lst)


if __name__ == "__main__":

    for i in range(len(argv)):
        if argv[i] == "-h" or argv[i] == "--help" or len(argv) == 0:
            print("""
-a or --amount  : number of characters in the password (int)
-c or --count   : amount passwords (int)
-s or --special : use or not use special characters (y 1 true True or other)
-n or --name    : output file name (str)
-f or --file    : create a text file or not (does not require parameters)
            """)
            exit(0)
        if argv[i] == "-a" or argv[i] == "--amount":
            amount_ = int(argv[i + 1])

        if argv[i] == "-c" or argv[i] == "--count":
            count_ = int(argv[i + 1])

        if argv[i] == "-s" or argv[i] == "--special":
            special_ = argv[i + 1]

        if argv[i] == "-n" or argv[i] == "--name":
            name_ = argv[i + 1]
        if argv[i] == "-f" or argv[i] == "--file":
            file_ = "True"

    PassGen(
        amount=amount_,
        count=count_,
        special=special_,
        name=name_,
        is_file=file_)
