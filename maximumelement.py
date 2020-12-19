stack, queries = list(), ("1", "2", "3")
itterations = int(input("Enter an integer: "))

def is_valid_query(query, queries):
   return query in queries

print(stack)

for i in range(itterations):
   array = []
   entry = input()
   array = entry.split(" ")
   print(array)
   query = array[0] 
   if is_valid_query(query, queries):
      if query == "1":
         stack.append(array[-1])
      elif query == "2":
         stack.pop()
      elif query == "3":
         duplicate = stack.copy()
         duplicate.sort()
         print(duplicate[0])

         
         

   
