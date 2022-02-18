def convertTime(num):
  
  time= str(int(num / 60))
  minute= str(num % 60)
  minuteFormat = "0" + minute if len(minute) == 1 else minute
  
  return time + ":" + minuteFormat
  
print(convertTime(128))