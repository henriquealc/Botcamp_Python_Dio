'''
link util- https://academiapme-my.sharepoint.com/:p:/g/personal/nubia_dio_me/EaMAaOx_Bq5JqkD9h-Ksh0kB6tFp8Uj38OIjOy-hALypeQ?rtime=EDZ9pn9v3Eg
'''

salario = 2000

def salario_bonus(bonus, lista):
    global salario
    
    lista_aux = lista.copy()
    lista_aux.append(5)
    print(f'lista aux= {lista_aux}')

    salario += bonus
    return salario

lista = [1]
salario_com_bonus = salario_bonus(500, lista) # 2500 
print(salario_com_bonus)
print(lista)