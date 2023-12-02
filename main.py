import os

# *************   Functions:   *************

def clear():
    os.system('clear')

def menu():
    clear()
    show_menu_options()
    selected_option = receive_selected_option()
    run_selected_option(selected_option)



def show_menu_options():
    header = "Plik lotto.dat zawiera wyniki losowań lotto w pewnym zakresie czasu."
    description = "Z pliku wypisać do pliku tekstowego te wyniki losowań, w których:"

    options_list = ("zadanie 1: tylko liczby parzyste",
        "zadanie 2: suma wylosowanych liczb w przedziale 110 - 190",
        "zadanie 3: suma cyfr wszystkich wylosowanych liczb równa 50",
        "zadanie 4: różnica między największą a najmniejszą równa 30",
        "zadanie 5: cztery wylosowane liczby o takiej samej ostatniej cyfrze",
        "zadanie 6: cztery wylosowane liczby w jednym z zakresów: 1-9 albo 10-19 albo 20-29 albo 30-39 albo 40-49",
        "zadanie 7: własne ciekawe przetwarzanie"
    )

    nl = "\n"           #* new line
    div = 2*nl          #* divider

    options_stringified = nl.join(options_list)

    print(header+div+description+div+options_stringified+call_to_action)



def receive_selected_option():
    user_selection = input("Wpisz cyfrę zadania aby uruchomić funkcję:")
    selected_option = null

    while not user_selection.isdigit():
        user_selection = input("Błędna wartość, spróbuj jeszcze raz: ")

    while user_selection > 7:
        user_selection = input("Zbyt duża wartość, podaj cyfrę od 0 do 7: ")
        break
    selected_option = user_selection

    return selected_option



def run_selected_option(selected_option):
    if selected_option == 0:
        end_program()

    while selected_option !=0:
        match selected_option:
            case 1:
                run_excercise_1()
            case 2:
                run_excercise_2()
            case 3:
                run_excercise_3()
            case 4:
                run_excercise_4()
            case 5:
                run_excercise_5()
            case 6:
                run_excercise_6()
            case 7:
                run_excercise_7()



## ******   Functions: file operations   ******
"""
? 0. numer
? 1. data_losowania
? 2. L_1
? 3. L_2
? 4. L_3
? 5. L_4
? 6. L_5
? 7. L_6
"""

def get_data():
    file_lines_list = get_file_lines()
    organized_list = organize_file_lines(file_lines_list)

    return organized_list



def get_file_lines():
    lotto_file = open("lotto.dat", "r") #* "r" is the second parameter by default

    try:
        if lotto_file.readable():
            lotto_file_records = lotto_file.readlines() #* Outputs a list with lines from file as elements
                #* Outputs:
                #* 'numer\tdata losowania\tL_1\tL_2\tL_3\tL_4\tL_5\tL_6\n'
                #* '4408\t2007-07-04\t33\t16\t4\t45\t40\t47\n'
    except:
        print("Wystąpił błąd podczas otwierania pliku - plik nie jest do odczytu.")
    finally:
        lotto_file.close()
    
    lotto_file_records.pop(0)
    return lotto_file_records



def organize_file_lines(file_lines):
    list_of_dictionaries = []

    for line in file_lines:
        values = line.split('\t')

        # Creating a dictionary with keys and values
        dictionary = {
            'number': values[0],
            'date': values[1],
            'drawn_numbers': [values[2], values[3], values[4], values[5], values[6], values[7]]
        }
        # line is organized now

        list_of_dictionaries.append(dictionary)

    return list_of_dictionaries



## ******   Functions: Tasks   ******





## ******   Functions: Others   ******

def end_program():
    msg = "Dziękujemy za skorzystanie z programu."
    print(msg)



# *************   Operations   *************

while True:
    menu()
    end_check = input("Aby zamknąć program wciśnij 0 na klawiaturze, każdy inny wpis otworzy program na nowo.")

    if end_check.isdigit() and end_check == 0:
        break
    else:
        continue

exit()
