from scipy.stats import linregress

x = [1,2,3,4]
y = [3,5,7,9]

a = linregress(x,y)
print(a)
for i in range(len(a)):
    print(a[i])
if a[2] ==1:
    print('Deu certo porra')
dado = []
valor = []
for i in range(len(a)):

    a[i] = a[i].split('=')

for i in range(0, len(a)):
    try:
        dado.append(float(a[i][0]))
        valor.append(float(a[i][1]))
    except:
        dado.append(str.lower(a[i][0]))
        valor.append(str.lower(a[i][1]))

print(dado)
print(valor)

print(linregress(x,y))