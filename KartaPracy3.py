# pentla liczb dwucyfrowych od 10 do 22
# for i in range(10,22): print(i, end=" ")
# pętla liczb dwucyfrowych nieparzystych od 15 do 31
# for i in range(15,32,2): print(i, end=" ")
# pętla liczb dwucyfrowych malejąco (step ujemny)
# for i in range(99,9,-1): print(i, end=" ")
# pętla liczb dwucyfrowych malejąco (step dodatni)
# for i in range(10,100,1): print(109-i, end=" ")
# pętla liczb 3-cyfrowych podzielna przez 20
# for i in range(100, 1000, 20): print(i, end=" ")
# Zad 1
# n = int(input())
# for i in range(n):
#   print(i**3+3, end=" ")
# Zad 2 
# for i in range(105, 1000, 15):
#   print(i, end=" ")
# PRE 2

#Pętle for liczb trzycyfrowych podzielnych prez 13
# for i in range(104,999,13):
#   print(i, end=" ")
# Pętle for liczb dwucyfrowych parzystych
# for i in range(10,99,2):
#   print(i, end=" ")
# Pętle for potęg cyfr: 0, 1, 4, 9, 16 .. 81
# for i in range(10):
#   print(i*i, end=" ")

#Zad 3
n = int(input())
for i in range(1, n+1):
   if n % i == 0:
  print(i)

  