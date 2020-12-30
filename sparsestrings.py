strings, queries = list(), list()
no_of_strings = int(input("Enter number of strings: "))
no_of_queries = int(input("Enter number of queries: "))

for i in range(no_of_strings):
   string = input("Enter string: ").lower()
   strings.append(string)

for j in range(no_of_queries):
   query = input("Enter query: ").lower()
   queries.append(query)

def matchStrings(strings, queries):
   dictionary, array = dict(), list()
   for string in strings:
      for query in queries:
         if query == string:
            dictionary.setdefault(query, 0)
            dictionary[query] =  dictionary[query] + 1

   for value in dictionary.values():
      array.append(value)

   return array

print(str(matchStrings(strings, queries)))