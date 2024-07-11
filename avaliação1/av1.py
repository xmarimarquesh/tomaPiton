import re

arq = open('clientes.txt',encoding='utf-8',mode='w')
arq.write('''J~_oa*o! V#i.tor
M%a$theu's S#il$va
Car**olin$a Me(i&r*e
Cecilia Meireles
Andressa Alves
Jo$_*se _N+i@va#ldo
An!a Vi/t#oria$
joa?o a'bRE*u
Vinicius car&valho
s#HERL%OCK !holmes
NATHAN L*IMA!
Rafael Joao
M#aria J@ose
G#abriela #Maria
Jessica lim%a**
emanuelle gar&*cia
Fab12ian#a G_+ome-s
Lucas Silveira
Adri3$ana A'!lmeida
Q+UENTI)N ?TARAN@TINO
BA+T M*AN
CLA$Rk @Kent
Bruc?e Al()ves
HELEn+a R_omulo
Nicholas!@ B#ueno
No$ah B&arbosa
Daniel? G_+onçalVES
ELBA! RAMALHO
Le*_onard#o +(Gabriel
Gabri#el Penkal?
''')

arq = open('clientes.txt', 'r')
clientes = arq.read()
nomes_formatados=[]
nomes = clientes.split('\n')

arquivo = open("result.txt", encoding='utf-8',mode='a')

for i in nomes:
    nomes_formatados.append(re.split(r"['?/~_*!#.%$()&@123+-]",i))

for j in nomes_formatados:
    for x in j:
        nome = ''.join(j)
    print(nome)
    arquivo.write(f'{nome.title()}\n\n')

print()
