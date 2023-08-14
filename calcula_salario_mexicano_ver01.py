#Payment Mexican Payment rate calculator
#When a mexican works more than 48 hrs then every hour after 48 is payed by 2
#But if the hours worked exceed 57 hours every hour after that will be payed by 3
print("Por favor solo agrega numeros!!") 
def computepay(hours,rate):
    print("Recordatorio")
    print("Horas extra despues de 48, se pagan al doble")
    print("A partir de 9 horas extra, cada hora mas se paga al triple")
    print("Horas trabajadas:",hours)
    #If working more than 57
    if hours > 57:
        ot = hours - 48
        hours = 48
        if ot > 9:
            ot2 = ot - 9
            print("Horas Triples:",ot2)
            ot2rate = rate * 3
            otpay2 = ot2*ot2rate
            print("Pago por Horas triples:",otpay2)
            ot = float(9)
        print("Horas Dobles:",ot)
        hours = 48
        otrate = rate * 2
        otpay = ot*otrate
        print("Pago por Horas dobles:",otpay)
        p = (hours * rate) + otpay + otpay2
    #If working more than 48
    elif hours > 48:
        ot = hours - 48
        hours = 48
        print("Horas Dobles:",ot)
        otrate = rate * 2
        otpay = ot*otrate
        print("Pago por Horas dobles:",otpay)
        p = (hours * rate) + otpay
    else:
    #If not
        p = hours * rate
    print("Pago por 48 Horas Normales:",(hours*rate))
    return p

#Data that needs to be collected
hrs = input("Ingresa Horas trabajadas: ")
hours = float(hrs)
rt = input("Ingresa el salario por hora: ")
rate = float(rt)
p = computepay(hours,rate)
#Total pay
print("Paga Total:", p)

