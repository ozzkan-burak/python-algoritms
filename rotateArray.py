def rotateArray(array):
  old_start = array[0]
  new_start = [str(array[old_start])]
  
  count = old_start + 1
  
  length = len(array)
  
  while count%length != old_start:
    new_start.append(str(array[count%length]))
    count += 1
    
  return "".join(new_start)
  


print(rotateArray([1,5,6,7,8,9,10,11,12]))