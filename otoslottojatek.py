import random

nyeroszamok = []
jatekos_szamai = []

talalatok = 0

print('köszöntelek a játékban!')
print('adj meg 5 számot')

for number in range(0,5):
    random_szam = random.randint(1, 90)
    nyeroszamok.append(random_szam)
    
for number in range(0,5):
    jatekos = int(input())
    jatekos_szamai.append(jatekos)
    
for nyersz in nyeroszamok:
    for jatekos in jatekos_szamai:
        if jatekos == nyersz:
            talalatok = talalatok + 1
            
print(f' {talalatok} találatod van')
print(f'A nyerőszámok: {nyeroszamok}')