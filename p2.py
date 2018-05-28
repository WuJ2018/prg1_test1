def is_factorion(n):
   result = 0
   x = n // 10
   y = n % 10
   while not(x==0 and y==0):
      result += factorial(y)
      y = x % 10
      x = x // 10
   return n == result
