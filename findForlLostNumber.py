def findForLostNumber(string):
  
  for i in range(10):
    c = string.replace("x", str(i))
    x=string.index("=")
    
    if eval(c[:x]) == eval(c[x+1:]):
      return str(i)
    
print(findForLostNumber("1x * 11 = 121"))
print(findForLostNumber("1x0 / 3 = 50"))
print(findForLostNumber("10 - x = 4"))