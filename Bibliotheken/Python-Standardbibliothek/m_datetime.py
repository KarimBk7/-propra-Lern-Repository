import datetime as dt
import locale

# A2
now = dt.datetime.now()
current_time = now.strftime("%H:%M:%S")
print("aktuelle zeit:", current_time)

# A3
dateobj = dt.datetime(day=1, month=12,year=2024,minute=9,hour=13)

# A4
weekid = dateobj.weekday()
monthid = dateobj.month-1
wochentag = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]
monate = ["Januar", "Februar", "März", "April", "Mai", "Juni",
          "Juli", "August", "September", "Oktober", "November", "Dezember"]

 
print("formatierte Zeit;", wochentag[weekid] + dateobj.strftime(f", der %d. {monate[monthid]} %Y, %H:%M Uhr"))