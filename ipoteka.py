def main_calc():
    global dolg
    srok = 0
    dolg = main_dolg
    dolgpay = main_dolgpay
    while dolg > 0:
        procpay = dolg / 100 * proc
        procpays.append(procpay)
        dolg -= dolgpay
        dolgpays.append(dolgpay)
        generalpay = procpay + dolgpay
        generalpays.append(generalpay)
        procpay = dolg / 100 * proc
        dolgpay = dolgpay + (procpays[-1] - procpay)
        srok += 1
    if srok > wanted_srok:
        correction()
        main_calc()


def correction():
    global main_dolgpay
    global procpays
    global dolgpays
    global generalpays
    main_dolgpay += 10
    procpays = []
    dolgpays = []
    generalpays = []


def set_srok():
    value = input("Enter your wanted srok: ")
    if value.isdigit():
        value = int(value)
        return value
    else:
        print("Enter NUMBER please!")
        set_srok()


# proc  это процентная ставка месячная
proc = 0.683333
# main_dolg это константа долга
main_dolg = 2257000
# wanted_srok это желаемый срок кредита
wanted_srok = set_srok()
main_dolgpay = 7000
procpays = []
dolgpays = []
generalpays = []
main_calc()
print(generalpays, '\n')
print('You have', len(generalpays), 'paynments')
