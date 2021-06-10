print ("MULTIPLICACIÓN DE MATRICES")
fm1 = int(input("Ingrese el numero de filas de la matriz 1: "))
cm1 = int(input("Ingrese el numero de columnas de la matriz 1: "))

matriz1 =[]
for i in range(fm1):
  matriz1.append([])
  for j in range(cm1):
    valor1 = float(input("Fila {}, Columna {}: ".format(i+1, j+1)))
    matriz1[i].append(valor1)

fm2 = int(input("Ingrese el numero de filas de la matriz 2: "))
cm2 = int(input("Ingrese el numero de columnas de la matriz 2: "))

matriz2 =[]
for i in range(fm2):
  matriz2.append([])
  for j in range(cm2):
    valor2 = float(input("Fila {}, Columna {}: ".format(i+1, j+1)))
    matriz2[i].append(valor2)
    
'''
a=[[1,2,3],
  [4,5,6]]
b = [[1,2],
    [3,4],
    [5,6]]
'''

def multiplicar_matrices(m1, m2):
  if len(m1[0]) == len(m2):
    m3 = []
    for i in range(len(m1)):
      m3.append([])
      for j in range (len(m2[0])):
        m3[i].append(0)
    
    for i in range(len(m1)):
      for j in range(len(m2[0])):
        for k in range(len(m1[0])):
          m3[i][j] += m1[i][k] * m2[k][j]
    return m3
  else:
    return None

c = multiplicar_matrices(matriz1, matriz2)

if c == None:
  print("No se puden multiplicar")
else:
  print("Resultado de la multiplicación")
  for fila in c:
    print("[", end=" ")
    for elemento in fila:
      print(elemento, end=" ")
    print("]")


