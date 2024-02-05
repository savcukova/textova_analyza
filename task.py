#projekt_1.py: první projekt do Engeto Online Python Akademie

#author: Olina Savčuková
#email: olinkasavcuk@gmail.com
#discord: Olina Savčuková

from task_template import TEXTS

users = {"bob": "123",
         "ann": "pass123",
         "mike": "password123",
         "liz": "pass123"}

num_texts = len(TEXTS)

username = input("your username: ")
password = input("your password: ")

print(f"username: {username}")
print(f"password: {password}")
print(40 * "-")

if not username in users:
    print("unregistered user, terminating the program..")
    quit()
elif username in users and users[username] != password:
    print("wrong password")
    quit()
elif username in users and users[username] == password:
    print(f"Welcome to the app, {username}")
    print(f"We have {num_texts} texts to by analyzed.")
    print(40 * "-")
    
    selected_text = input(f"Enter a number btw. 1 and {num_texts} to select: ")
    
    if not 1 <= int(selected_text) <= num_texts or int(selected_text) == 0:
        print(f"text number {selected_text} is not available. Terminating the program.")
        quit()
    elif not selected_text.isdigit():
        print("Invalid input.")
        quit()
    print(40 * "-")
    
    #Pro vybraný text spočítá následující statistiky
    selected_text_index = int(selected_text) - 1
    obsah = TEXTS[selected_text_index]
    
    words = obsah.split()
    pocet_slov = len(words)
    
    velke_1_pismeno = [word for word in words if word.istitle()]
    sum_velke_1_pismeno = len(velke_1_pismeno)
            
    mala_pismena = [word for word in words if word.islower()]
    sum_mala = len(mala_pismena)
            
    velka_pismena = [word for word in words if word.isupper()]
    sum_velka = len(velka_pismena)
            
    cisla = [word for word in words if word.isdigit()]
    sum_cisla = len(cisla)
                
    cisla_dohromady = (int(word) for word in words if word.isdigit())
    dohromady = sum(cisla_dohromady)
    
      
print(f"There are {pocet_slov} words in the selected text.")
print(f"There are {sum_velke_1_pismeno} titlecase words.")
print(f"There are {sum_velka} uppercase words.")
print(f"There are {sum_mala} lowercase words.")
print(f"There are {sum_cisla} numeric strings.")
print(f"The sum of all the numbers {dohromady}.")

print(40 * "-")
print(f"{'LEN': >3}|{'OCCURRENCES': >18} | {'NR.'}")

print(40 * "-")

delka_slov = [len(word.strip(",.!?")) for word in words]

unique_delka = sorted(set(delka_slov))

for length in unique_delka:
    occurences = delka_slov.count(length)
    retezec = "*" * occurences
    print(f"{length: >3} | {retezec: <18}| {occurences}")
    
    