primos = [3,5]

def chegarPrimo(primo1, primo2, n):
    if n == 1:
        primo = primo1 * primo2 - 2
    elif n == 2:
        primo = primo1 * primo2 + 2
    cond = 0
    for i in range(1, primo+1):
        if primo % i == 0:
            cond +=1
        if cond == 2 and i == primo and n == 1:
            print (primo1,"*", primo2, -2," = ", primo1 * primo2 - 2)
            return 0
        elif cond == 2 and i == primo and n == 2:
            print (primo1,"*", primo2,"+2"," = ", primo1 * primo2 + 2)
            return 1
    return 2

i = 0
for primo1 in primos:
    for primo2 in primos:
        resulte = chegarPrimo(primo1, primo2, 1)
        if  resulte == 0:  
            primos.append(primo1 * primo2 - 2)
        resulte = chegarPrimo(primo1, primo2, 2)
        if resulte == 1:  
            primos.append(primo1 * primo2 + 2)
        i += 1
        if i == 10:
            break 
    break
    
# print (primos)