times = ['1_palmeiras', '2_coritiba', '1_corintians', '3_juventude','2_fluminense','3_bahia','1_cuiaba',
         '2_cascavel','3_ponte preta', '2_parana clube', '3_volta redonda']

primeira = []
segunda = []
terceira = []

for i in times:
    if i[0] == '1':
        primeira.append(i)
    elif i[0] == '2':
        segunda.append(i)
    elif i[0] == '3':
        terceira.append(i)

print(f"Primeira divisão: {primeira}")
print(f"Segunda divisão: {segunda}")
print(f"Terceira divisão: {terceira}")