'''
Returneaza true daca n este prim si false daca nu.
'''
def is_prime(n):
  if n < 2:
    return False
  for i in range (2, n // 2 + 1):
    if n % i == 0:
      return False
  return True
  
  
'''
Returneaza produsul numerelor din lista lst.
'''
def get_product(lst):
  p = 1
  for i in range (0, len(lst)):
    p = p * lst[i]
  return p
  
'''
Returneaza CMMDC a doua numere x si y folosind primul algoritm.
'''
def get_cmmdc_v1(x, y):
  while x != y:
    if x > y:
      x = x - y
    else:
      y = y - x
  return x
  
  
'''
Returneaza CMMDC a doua numere x si y folosind al doilea algoritm.
'''
def get_cmmdc_v2(x, y):
  while y != 0:
    r = x % y
    x = y
    y = r
  return x
  
  
def main():
  finish = False
  while not finish:
    print("1. Verificati daca n este numar prim")
    print("2. Calculati produsul numerelor dintr-o lista")
    print("3. Determinati cel mai mare divizor comun - metoda cu scaderi")
    print("4. Determinati cel mai mare divizor comun - metoda cu impartiri")
    print("x. Exit")
    option = input("Dati optiunea: ")
    if option == '1':
      print("Introduceti numarul..")
      x = int(input())
      print(is_prime(x))
    elif option == '2':
      str = input("Introduceti numerele separate prin virgula: ")
      lst = str.split(',')
      for i, x in enumerate(lst):
        lst[i] = int(x)
      print(get_product(lst))
    elif option == '3':
      print("Va rog introduceti primul numar..")
      x = int(input())
      print("Va rog introduceti al doilea numar..")
      y = int(input())
      print("Cel mai mare divizor comun este..", get_cmmdc_v1(x, y))
    elif option == '4':
      print("Va rog introduceti primul numar..")
      x = int(input())
      print("Va rog introduceti al doilea numar..")
      y = int(input())
      print("Cel mai mare divizor comun este..", get_cmmdc_v2(x, y))
    elif option == 'x':
      finish = True
    else:
      print("Optiunea nu este valida")


if __name__ == '__main__':
  main()
