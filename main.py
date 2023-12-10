import os
from collections import Counter # for run_excercise_5()

#! GitHub repo link: https://github.com/s-andrzejewski/python_lotto_data_analysis



# *************   Functions:   *************

def init():
    while True:
        clear()
        show_menu_options()
        
        selected_option = receive_selected_option()
        run_selected_option(selected_option)
        end_check = input("Aby zamknąć program wciśnij 0 na klawiaturze, każdy inny wpis otworzy program na nowo.")

        if end_check.isdigit() and end_check == 0:
            break
        else:
            continue

    exit()



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

    call_to_action = "Wybierz odpowiednią opcję, aby rozpocząć zadanie (1-7)."

    nl = "\n"           #* new line
    div = 2*nl          #* divider

    options_stringified = nl.join(options_list)

    print(header+div+description+div+options_stringified+div+call_to_action)



def receive_selected_option():
    user_selection = input("Wpisz cyfrę zadania aby uruchomić funkcję:")
    selected_option = None

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

def prepare_data():
    data = get_data()
    how_many_counter = 0
    which_lines_counter = []
    
    return data, how_many_counter, which_lines_counter



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
    
    lotto_file_records.pop(0) #* delete first record (table heading)
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

def run_excercise_1():
#? zadanie 1: tylko liczby parzyste
    # list of dictionaries
    data, how_many_counter, which_lines_counter = prepare_data()

    for index, dict in enumerate(data):
        drawn_numbers = dict['drawn_numbers']

        if all(num % 2 == 0 for num in drawn_numbers):
            how_many_counter += 1
            which_lines_counter.append(index)
    
    print(f"Jest {how_many_counter} losowań z samymi liczbami parzystymi.")



def run_excercise_2():
#? zadanie 2: suma wylosowanych liczb w przedziale 110 - 190
    data, how_many_counter, which_lines_counter = prepare_data()

    for index, dict in enumerate(data):
        drawn_numbers = dict['drawn_numbers']
        drawn_sum = sum(drawn_numbers)

        if 110 <= drawn_sum <= 190:
            how_many_counter += 1
            which_lines_counter.append(index)

    print(f"Jest {how_many_counter} losowań w których suma liczb znajduje się w przedziale od 110 do 190.")




def run_excercise_3():
#? zadanie 3: suma cyfr wszystkich wylosowanych liczb równa 50
    data, how_many_counter, which_lines_counter = prepare_data()
    target_sum = 50

    for index, dict in enumerate(data):
        drawn_numbers = dict['drawn_numbers']

        if sum(sum(map(int, num)) for num in drawn_numbers) == target_sum:
            # example list: ["123", "45", "67"]
            # (1+2+3) + (4+5) + (6+7) ?= 50
            how_many_counter += 1
            which_lines_counter.append(index)

    print(f"Jest {how_many_counter} losowań z sumą cyfr wylosowanych liczb równą {target_sum}.")



def run_excercise_4():
#? zadanie 4: różnica między największą a najmniejszą równa 30
    data, how_many_counter, which_lines_counter = prepare_data()
    target_value = 30

    for index, dict in enumerate(data):
        drawn_numbers = dict['drawn_numbers']
        sorted_numbers = sorted(drawn_numbers)
        first = sorted_numbers[0]
        last = sorted_numbers[-1]
        difference = last - first

        if difference == target_value:
            how_many_counter += 1
            which_lines_counter.append(index)

    print(f"Jest {how_many_counter} losowań z róźnicą między największą a najmniejszą liczbą równą {target_value}.")



def run_excercise_5():
#? zadanie 5: cztery wylosowane liczby o takiej samej ostatniej cyfrze
    data, how_many_counter, which_lines_counter = prepare_data()

    # stores the same list but last digits instead of whole numbers
    files_last_digits = [] # list of lists

    for index, dict in enumerate(data):
        drawn_numbers = dict['drawn_numbers']
        lines_last_digits = []

        for number in drawn_numbers:
            # 24, 21, 4, 14, 94, 11
            last_digit = int(str(number)[-1])
            # 4, 1, 4, 4, 4, 1
            lines_last_digits.append(last_digit)  # list contains last digits of numbers instead of original numbers
        # [[4, 1, 4, 4, 4, 1],[...],...]
        files_last_digits.append(lines_last_digits)

    for index, line in enumerate(files_last_digits):
        if check_repeats(line, 4):
            how_many_counter += 1
            which_lines_counter.append(index)
    
    print(f"Jest {how_many_counter} losowań z czterema liczbami o takiej samej ostatniej cyfrze.")
    


def run_excercise_6():
#? zadanie 6: cztery wylosowane liczby w jednym z zakresów: 1-9 albo 10-19 albo 20-29 albo 30-39 albo 40-49

    data, how_many_counter, which_lines_counter = prepare_data()

    for index, dict in enumerate(data):
        drawn_numbers = dict['drawn_numbers']

        counter_1_9 = counter_10_19 = counter_20_29 = counter_30_39 = counter_40_49 = 0

        for number in drawn_numbers:
            # 1, 2, 4, 8, 9, 9
            if 1 <= number <= 9:
                counter_1_9 += 1
            elif 10 <= number <= 19:
                counter_10_19 += 1
            elif 20 <= number <= 29:
                counter_20_29 += 1
            elif 30 <= number <= 39:
                counter_30_39 += 1
            elif 40 <= number <= 49:
                counter_40_49 += 1
        
        if counter_1_9 == 4 or counter_10_19 == 4 or counter_20_29 == 4 or counter_30_39 == 4 or counter_40_49 == 4:
            how_many_counter += 1
            which_lines_counter.append(index)
    
    print(f"Jest {how_many_counter} losowań z czterema liczbami w jednym z zakresów: 1-9 albo 10-19 albo 20-29 albo 30-39 albo 40-49.")



def run_excercise_7():
#? zadanie 7: własne ciekawe przetwarzanie
# Sprawdza, czy istnieją trzy kolejne liczby w liście, których suma jest równa 29.

    data, how_many_counter, which_lines_counter = prepare_data()

    for index, dict in enumerate(data):
        drawn_numbers = dict['drawn_numbers']

        #* example: [a, b, c, d, e]:
        for i in range(len(drawn_numbers) - 2):
            #* 0 -> a + b + c
            #* 1 -> b + c + d
            #* 2 -> c + d + e
            sum_of_three = drawn_numbers[i] + drawn_numbers[i + 1] + drawn_numbers[i + 2]

            if sum_of_three == 29:
                how_many_counter += 1
                which_lines_counter.append(index)
                break  #* If found, no need to continue checking for the current set of numbers

    print(f"Jest {how_many_counter} losowań z trzema kolejnymi liczbami, których suma wynosi 29.")



## ******   Functions: Others   ******

def clear():
    os.system('clear')


def check_repeats(lst, target_count):
    #* Count occurrences of each element in the list
    counts = Counter(lst)

    #* Check if any element occurs exactly target_count times
    for element, count in counts.items():
        if count == target_count:
            return True

    return False


def end_program():
    msg = "Dziękujemy za skorzystanie z programu."
    print(msg)



# *************   Operations   *************

init()