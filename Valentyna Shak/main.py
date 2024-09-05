def fibonacci(first,second,step):
  if step<=0:
      print("Enter positive integer+")

  list_fibonacci = [first]
  if step>1:
    list_fibonacci+=fibonacci(second,first+second,step-1)
  return list_fibonacci

file= open("input.txt")
numbers=file.read().split()
first=numbers[0]
second=numbers[1]
file1=open("steps.txt")

step=file1.read()
res=fibonacci(float(first),float(second),int(step))

with open("result.txt",'w') as file2:
  for num in res:
    file2.write(f"{num} ")

file.close()
file1.close()
file2.close()
