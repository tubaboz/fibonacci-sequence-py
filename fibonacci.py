fibo_num= []
first = 0
second = 1
for i in range(11):
  fibo_num.append(first)
  temp = first
  first = second
  second = temp + second
print(fibo_num) 
