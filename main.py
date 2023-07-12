import numpy as np
def convertidor_tipo(tipo):
  if tipo == "A":
    t = 1
  elif tipo == "B":
    t = 2
  elif tipo == "C":
    t = 3
  elif tipo == "D":
    t = 4
  return t

def suma(a, b, c, d):
  s = a + b + c + d
  return s

list = [[" ","A","B","C","D"]]
com = []
flag = True
f1 = True
f2 = True
f3 = True
f4 = True
p = 0
t = 0
c = 0
f = 0
da = 0
db = 0
dc = 0
dd = 0
ta = 0
tb = 0
tc = 0
td = 0
totald = 0
total = 0
for i in range(10):
  i += 1
  list.append([str(i),"-","-","-","-"])

while flag:
  print("1. Comprar departamento\n2. Mostrar departamentos disponibles\n3. listado de compradores\n4. Mostrar ganancia totales\n5. Salir\n")
  op = int(input("Elija la opcion que decea: "))
  if op == 1:
    print("Tipo A, 3.800 UF\nTipo B, 3.000 UF\nTipo C, 2.800 UF\nTipo D, 3.500 UF\n")
    arr = np.array(list)
    print(arr,"\n")
    while f4:
      while f2:
        tipo = input("ingrese el tipo de departamento que desea comprar: ")
        if tipo == "A" or tipo == "B" or tipo == "C" or tipo == "D":
          break
        else:
          print("ingrese un tipo valido por favor")
          
      while f3:
        piso = int(input("ingrese el piso del departamento que desea comprar: "))
        if piso <= 10 and piso >= 1:
          break
        else:
          print("ingrese un departamento valido por favor")
          
      t = convertidor_tipo(tipo)
      if list[piso][t] == "X":
        print("Elija un departamento que no este comprado")
      else:
        break
    
    if tipo == "A":
      da += 1
      ta += 3800
    elif tipo == "B":        
      db += 1
      tb += 3000
    elif tipo == "C":
      dc += 1
      tc += 2800
    elif tipo == "D":
      dd += 1
      td += 3500

    list[piso].pop(t)
    list[piso].insert(t,"X")
    while f1:
      rut = int(input("ingrese su numero de rut sin punto, sin guion y sin digito verificador: "))
      if rut <= 99999999 and rut >= 1000000:
        break
      print("ingrese el rut sin digito verificador y valido")
    com.append(rut)
    
  elif op == 2:
    arr = np.array(list)
    print("\n",arr,"\n")
    
  elif op == 3:
    com.sort(reverse=True)
    print("\n",com,"\n")
    
  elif op == 4:
    totald = suma(da, db, dc, dd)
    total = suma(ta, tb, tc, td)
    print(f"\nTipo de departamento  Cantidad    Total\nTipo A 3.800 UF           {da}        {ta} UF\nTipo B 3.000 UF           {db}        {tb} UF\nTipo C 2.800 UF           {dc}        {tc} UF\nTipo D 3.500 UF           {dd}        {td} UF\nTOTAL                     {totald}        {total} UF\n")
    
  elif op == 5:
    print("\nHasta pronto\nDiego Diaz\n12-07-2023")
    break
  else:
    print("elija un valor valido por favor")