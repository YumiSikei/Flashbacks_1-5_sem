def form_array(arr, n):
  new_arr = []

  nn=n
  i = 0
  while (i < n):
    if (arr[i] < 0):
      new_arr.append(arr[i])
      nn -= 1
    
    i += 1
    
  return new_arr, nn


def print_array(arr, n):
  i = 0
  while (i < n):
    print(arr[i], end = " ")
    i += 1
  
  print("")
    
