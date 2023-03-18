#At the beginning we hve 2 rabbits,each pair born 2 rabbits,total rabbits number equals the former total number plus the new born rabbits
#at the beginning there are two rabbits
total=2
#this is the first generation
generation=1
#loop for generation 
while total<100:
  newborn=total/2*2
  total+=newborn
  generation+=1
print("The total number is over 100 after generation",generation)
#The total number is over 100 after generation 7
