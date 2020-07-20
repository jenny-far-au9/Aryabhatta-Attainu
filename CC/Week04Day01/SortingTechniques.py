# Bubble Sort
def bubbleSort(a):
  length = len(a)
  for i in range(length):             
    for j in range(length-1-i):      #Compare only n-1 times as last place has been occupied
      if a[j] > a[j+1]:
        a[j],a[j+1] = a[j+1],a[j] 
  return a                           # Important Step

a = [11,33,1,4,7]
# bubbleSort(a)  
print("bubbleSort", bubbleSort(a))  

def OptimizedBuubleSort(b):
  length = len(b)
  optimized = False
  for i in range(length-1):
    for j in range(length-i-1):
      if b[j] > b[j+1]:
        b[j], b[j+1] = b[j+1], b[j]
        optimized = True
      if optimized is False:
        break
  return b
b = bubbleSort(a)
print("Optimized bubbleSort", bubbleSort(b))  
 

# Selection Sort

def selectionSort(a):
  length = len(a)
  for i in range(length):
    minimumOfAllIndex = i 
    for j in range(i+1, length):
      if a[minimumOfAllIndex] > a[j]:
        minimumOfAllIndex = j 
    a[i], a[minimumOfAllIndex] = a[minimumOfAllIndex], a[i] 
  return a
print("Selection Sort", selectionSort(a))

# Insertion Sort

def insertionSort(a):
  length = len(a)
  for i in range(0, length):
    j = i - 1
    x = a[i]
    while j >= 0:
      if a[j] > x:
        a[j+1] = a[j]
      else:
        break
      j = j-1
    a[j+1] = x
  return a
print("Insertion Sort", insertionSort(a))
