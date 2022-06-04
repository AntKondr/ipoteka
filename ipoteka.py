def main_calc():
    global srok
    dolg = main_dolg
    firstprocpay = dolg / 100 * proc
    procpays.append(firstprocpay)
    dolgpay = main_dolgpay
    while dolg > 0:
        dolg -= dolgpay
        dolgpays.append(dolgpay)
        procpay = dolg / 100 * proc
        dolgpay = dolgpay + (procpays[-1] - procpay)
        procpays.append(procpay)
        generalpay = procpay + dolgpay
        generalpays.append(generalpay)
        srok += 1
    if srok > want_srok:
        correction()
        main_calc()


def correction():
    global main_dolgpay
    global srok
    global procpays
    global dolgpays
    global generalpays
    main_dolgpay += 10
    srok = 0
    procpays = []
    dolgpays = []
    generalpays = []


proc = 0.683333
main_dolg = 2257000
srok = 0
want_srok = int(input("enter want srok: "))
print()
main_dolgpay = 5000
procpays = []
dolgpays = []
generalpays = []
main_calc()
print(generalpays)
print(len(generalpays))
