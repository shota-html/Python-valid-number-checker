import phonenumbers
import time
from art import *
from random import randint
from colorama import init
from termcolor import colored

init()

art = text2art("VAL", font="block")

print(colored(art, "red"))

country_code = input(colored("Введите код страны (например, +7 для России): ", "blue"))
number = input(colored("Введи номер без плюса и кода страны для проверки: ", "red"))

full_number = f"{country_code}{number}"
print(colored("Нахожу инфу...", "red"))
time.sleep(randint(1, 4))

try:
    parsed_number = phonenumbers.parse(full_number)
    
    valid_check = phonenumbers.is_valid_number(parsed_number)
    
    if valid_check:
        print(colored("Номер валиден.", "green"))
        time.sleep(2)
        print(colored("Создатель: @shotakos.", "red"))
    else:
        print(colored("Номер не валиден.", "red"))
        
except phonenumbers.NumberParseException:
    print(colored("Ошибка: Неверный формат номера.", "red"))