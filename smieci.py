import datetime

def czyPrzestepny(rok):
  if rok % 400 == 0 and rok % 100 == 0:
    return True 
  elif rok % 4 == 0 and rok % 100 != 0:
    return True
  else:
    return False
    
def zmianaDaty(rok,miesiac,dzien):
  rok1=rok+1
  miesiac1=miesiac+1
  miesiac=miesiac+1
  dzien1=dzien+1
  if miesiac1==1:
    if dzien+1>31:
      miesiac1=2
      dzien1=1
      return (rok,miesiac,miesiac1,dzien,dzien1)
  if miesiac1==2 and czyPrzestepny(rok)==True:
    if dzien+1>29:
      miesiac1=3
      dzien1=1
      return (rok,miesiac,miesiac1,dzien,dzien1)
  if miesiac1==2 and czyPrzestepny(rok)==False:
    if dzien+1>28:
      miesiac1=3
      dzien1=1
      return (rok,miesiac,miesiac1,dzien,dzien1)
  if miesiac1==3:
    if dzien+1>31:
      miesiac1=4
      dzien1=1
      return (rok,miesiac,miesiac1,dzien,dzien1)
  if miesiac1==4:
    if dzien+1>30:
      miesiac1=5
      dzien1=1
      return (rok,miesiac,miesiac1,dzien,dzien1)
  if miesiac1==5:
    if dzien+1>31:
      miesiac1=6
      dzien1=1
      return (rok,miesiac,miesiac1,dzien,dzien1)
  if miesiac1==6:
    if dzien+1>30:
      miesiac1=7
      dzien1=1
      return (rok,miesiac,miesiac1,dzien,dzien1)
  if miesiac1==7:
    if dzien+1>31:
      miesiac1=8
      dzien1=1
      return (rok,miesiac,miesiac1,dzien,dzien1)
  if miesiac1==8:
    if dzien+1>31:
      miesiac1=9
      dzien1=1
      return (rok,miesiac,miesiac1,dzien,dzien1)
  if miesiac1==9:
    if dzien+1>30:
      miesiac1=10
      dzien1=1
      return (rok,miesiac,miesiac1,dzien,dzien1)
  if miesiac1==10:
    if dzien+1>31:
      miesiac1=11
      dzien1=1
      return (rok,miesiac,miesiac1,dzien,dzien1)
  if miesiac1==11:
    if dzien+1>30:
      miesiac1=12
      dzien1=1
      return (rok,miesiac,miesiac1,dzien,dzien1)
  if miesiac1==12:
    if dzien+1>31:
      miesiac1=13
      dzien1=1
      return (rok+1,miesiac,1,dzien,1)
  return (rok,miesiac,miesiac1,dzien,dzien1)

def addToFile(name,filename,rok):
  for i, line in enumerate(filename):
    line=line.replace("\n","")
    line=line.split(" ")
    for j in line:
      x=rok
      rok,miesiac,miesiac1,dzien,dzien1 = zmianaDaty(rok,int(i),int(j))
     
      if miesiac<10:
        miesiac=str("0"+str(miesiac))
      else:
        miesiac=str(miesiac) 
             
      if miesiac1<10:
        miesiac1=str("0"+str(miesiac1))
      else:
        miesiac1=str(miesiac1)
         
      if int(dzien)<10:
        dzien="0"+str(dzien)
     
      if dzien1<10:
        dzien1=str("0"+str(dzien1))
      else:
        dzien1=str(dzien1)
      
      print(rok,miesiac,miesiac1,dzien,dzien1)  
 
      f0.write("BEGIN:VEVENT\n")
      f0.write("DTSTART;VALUE=DATE:"+str(x)+str(miesiac)+str(dzien)+"\n")
      f0.write("DTEND;VALUE=DATE:"+str(rok)+str(miesiac1)+str(dzien1)+"\n")
      f0.write("DTSTAMP:20230101T111111Z\n")
      f0.write("UID:\n")
      f0.write("CLASS:PRIVATE\n")
      f0.write("CREATED:20230101T111111Z\n")
      f0.write("DESCRIPTION:\n")
      f0.write("LAST-MODIFIED:20230101T111111Z\n")
      f0.write("LOCATION:\n")
      f0.write("SEQUENCE:0\n")
      f0.write("STATUS:CONFIRMED\n")
      f0.write("SUMMARY:"+name+"\n")
      f0.write("TRANSP:TRANSPARENT\n")
      f0.write("BEGIN:VALARM\n")
      f0.write("ACTION:DISPLAY\n")
      f0.write("DESCRIPTION:This is an event reminder\n")
      f0.write("TRIGGER:-P0DT17H0M0S\n")
      f0.write("END:VALARM\n")
      f0.write("END:VEVENT\n")

if __name__ == "__main__":
  f0 = open("smieci.ics", "w")
  f1 = open("Dom_Bio.txt", "r")
  f2 = open("Dom_Pet.txt", "r")
  f3 = open("Dom_Smieci.txt", "r")

  f0.write("BEGIN:VCALENDAR\n")
  f0.write("PRODID:-//Google Inc//Google Calendar 70.9054//EN\n")
  f0.write("VERSION:2.0\n")
  f0.write("CALSCALE:GREGORIAN\n")
  f0.write("METHOD:PUBLISH\n")
  f0.write("X-WR-CALNAME:Śmieci\n")
  f0.write("X-WR-TIMEZONE:Europe/Warsaw\n")

  currentDateTime = datetime.datetime.now()
  date = currentDateTime.date()
  rok = int(date.strftime("%Y"))
  addToFile("Dom Bio",f1,rok)
  addToFile("Dom Pet",f2,rok)
  addToFile("Dom Smieci",f3,rok)
          

  f0.write("END:VCALENDAR")
  f0.close()
