def fibonacci(first,second,step):
  if step<=0:
      print("ZERO STEP CAN`T,ENTER POSITIVE INTEGER")
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
res=fibonacci(int(first),int(second),int(step))
print("Save in file")
with open("result.txt",'w') as file2:
  for num in res:
    file2.write(f"{num} ")


file.close()
file1.close()
file2.close()