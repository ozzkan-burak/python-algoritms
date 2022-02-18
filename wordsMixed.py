# argüman olarak verilen ikinci kelime kümesi, srt1 kelimesini karşılıyor mu?

def wordMixed(str1, str2):
  
  if len(str1) != len(str2):
    return False
  
  for i in str2:
    if i not in str1:
      return False
    
  return True


print(wordMixed("ankara", "kanara"))