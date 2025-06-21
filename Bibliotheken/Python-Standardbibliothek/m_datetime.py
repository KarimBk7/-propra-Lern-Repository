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

# A10
print("+1024d+512m:", new_caracas + dt.timedelta(days=1024, minutes=512))


# A11 und A12
logs = [
  ('2024-01-01##10:11:14', 1, 'start'),
  ('2024-01-02##03:01:01', 2, 'start'),
  ('2024-01-03##00:11:15', 1, 'end'),
  ('2024-01-03##03:02:02', 2, 'end')
]



def time_average(logs: list[tuple[str,int,str]]) -> dt.timedelta:
    start = {}
    diffs = []

    # convert strings and calculate difference
    for timestamp, eventnumber, flag in logs:
        if flag == 'start':
            start[eventnumber] = dt.datetime.strptime(timestamp,'%Y-%m-%d##%H:%M:%S')
        elif flag == 'end':
            diffs.append(dt.datetime.strptime(timestamp, '%Y-%m-%d##%H:%M:%S') - start[eventnumber])

    # calculate average
    result = dt.timedelta()
    for d in diffs:
        result += d

    return result / len(diffs)


print("Durchschnittliche Ausführungszeit:", time_average(logs))