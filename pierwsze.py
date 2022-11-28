# p, q = int(input()), int(input())

# for j in range(p, q+1):
#   flaga = True
#   for i in range(2, j):
#     if j % i == 0:
#       flaga = False
#   if flaga == True:
#     print(i, end=" ")

n  = int(input("Podaj ile chcesz liczb pierwszych"))
k = 2
ilosc = 0
while 1:
  if ilosc == n:
    flaga = True
   for i in range(2, k):
     if j % i == 0:
      flaga = False
       break
    if flaga == True:
     print(k, end=" ")
      ilosc = ilosc + 1
if ilosc == n:
  break
k = k + 1
  
    