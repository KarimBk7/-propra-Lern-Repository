import json

# A1
with open("m_json_student.json", mode="rb") as fl:
	data = json.load(fl)

# A2
def hat_uni(json, studentname: str, wochentag: str) -> bool:
	for student in json["Studenten"]:
		if student.get("Name") == studentname:
			vorl = student.get("Vorlesungen",{})
			for kurs in vorl.values():
				if wochentag in kurs.get("Tage",[]):
					return True
			
	return False

# A3
print("Max hat Donnerstag eine Veranstaltung:", hat_uni(data, "Max", "Donnerstag"))
print("Max hat Freitag eine Veranstaltung:", hat_uni(data, "Max", "Freitag"))

# A4
def setze_wunschnote(json, studentname: str, fachname: str, wunschnote: float):
	for student in json["Studenten"]:
		if student.get("Name") == studentname:
			ws = student.get("Wunschnoten",{})
			if fachname in ws.keys():
				ws.update({fachname: wunschnote})
				
				

# A5
setze_wunschnote(data, "Max", "Lineare Algebra", 2.3)

# A6
with open("m_json_student2.json", mode="w") as fl:
	json.dump(data, fl, indent=4 ,ensure_ascii=False)
	