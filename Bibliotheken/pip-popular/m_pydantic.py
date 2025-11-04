from dataclasses import dataclass, asdict
from json import loads, dumps
from datetime import datetime
from pydantic import BaseModel

# A1
@dataclass
class GradeEntry:
    name: str
    course: str
    grade: float
    date: datetime
    
    
print("\nA1:")
date = datetime.strptime("2025-05-05T11:30:00","%Y-%m-%dT%H:%M:%S",)
a = GradeEntry(name="Alan Turing", course="ALP-1", grade=2.0, date=date)
print(a)


# A2
print("\nA2:")
a_dict = asdict(a)
print(a_dict)

# A3
print("\nA3:")
a_dict["date"] = str(a_dict["date"])
a_json = dumps(a_dict)
print(a_json)

# A4
print("\nA4:")
dic = loads('{"name": "Alan Turing","course": "ALP-1","grade": 2.0,  "date": "2025-05-05T11:30:00"}')
a_parsed = GradeEntry(name=dic.get("name"), course=dic.get("course"), grade=dic.get("grade"), date=dic.get("date"))

print(a_parsed)
print(type(a_parsed.date))


# A5
@dataclass
class GradeEntry2(BaseModel):
    name: str
    course: str
    grade: float
    date: datetime

# A6
c = GradeEntry(name="Alan Turing", course="ALP-1", grade=2.0, date=date)

# A7
print("\nA7:")
c_dict = asdict(c)
c_dict["date"] = str(c_dict["date"])
c_json = loads(str(c_dict))
print(c_json)