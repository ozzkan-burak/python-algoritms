# input olarak verilen argüman içinde aynı harften kaçtane olduğunu bulan fonksiyon

def frequencyFind(string):
  
  i = 0
  final_string = ""
  
  while i < len(string):
    
    c = string[i]
    j = i +1
    
    compressed = [1,c]
    # print(compressed)
    
    while j < len(string):
      if string[j] == c:
        compressed[0] +=1
      else:
        break
      
      j+=1

    final_string += "".join(map(str, compressed))
    i = j    
    
  return final_string

print(frequencyFind("zzkkkbbwaaz"))