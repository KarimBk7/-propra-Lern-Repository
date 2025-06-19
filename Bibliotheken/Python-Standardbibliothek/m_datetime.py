import datetime as dt
import zoneinfo as zf

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


# A5
datestr = "2024-12-15##13:09:44"
dateexp = dt.datetime.strptime(datestr,"%Y-%m-%d##%H:%M:%S",)
print("geparste zeit:",  dateexp)

# A6
berlin_time = dt.datetime(2024,12,15,hour=13,minute=9,second=44, tzinfo=zf.ZoneInfo("Europe/Berlin"))
print("Berliner Zeit:", berlin_time)

# A7
caracas_time = dt.datetime(2024,12,15,hour=13,minute=9,second=44, tzinfo=zf.ZoneInfo("America/Caracas"))
print("Caracas Zeit:", caracas_time)

# A8
abstand = caracas_time.utcoffset()
print("UTC-Abstand:", abstand)

# A9
new_caracas = caracas_time - abstand
new_caracas = new_caracas.replace(tzinfo=zf.ZoneInfo("UTC"))
print("Caracas-nach-UTC:", new_caracas)