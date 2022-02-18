from re import A


def capitalize(str):
  
  string = str.split(' ')
  letter = ''
  
  for i in string:
    letter += i[0].upper() + i[1:] + ' '
    
  return letter

print(capitalize("dün ayın gününün başında"))

# python üzerinde build in function olanrak title() fonksiyonu cümle içindeki kelimelerin baş harflerini büyük harfe çevirir.


