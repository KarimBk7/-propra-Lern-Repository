import os
import sqlite3
import random

DBNAME = 'profile.db'


def create_table(dbfile: str):
    conn = sqlite3.connect(dbfile)
    c = conn.cursor()
    c.execute('DROP TABLE IF EXISTS profile')
    c.execute('CREATE TABLE profile (name TEXT, age INTEGER)')
    conn.commit()
    conn.close()


def generate_first_names():
    return ['Alice', 'Bob', 'Carla', 'David', 'Eve', 'Ford', 'Gotthilf', 'Hermione', 'Ira', 
            'Jolande', 'Kermit', 'Lady']


def generate_last_names():
    return ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Prefect', 'Gaga', 'Lastname']


def generate_middle_initials():
    return ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']


def generate_full_names():
    first_names = generate_first_names()
    last_names = generate_last_names()
    middle_initials = generate_middle_initials()
    names = []
    for first_name in first_names:
        for last_name in last_names:
            for middle_initial in middle_initials:
                name = first_name + ' ' + middle_initial + '. ' + last_name
                names.append(name)
    return names


def profile_this(dbfile: str):
    names = generate_full_names()

    for name in names:
        conn = sqlite3.connect(dbfile)
        c = conn.cursor()
        age = random.randint(18, 65)
        c.execute('INSERT INTO profile VALUES (?, ?)', (name, age))
        conn.commit()
        conn.close()


def main():
    create_table(DBNAME)
    profile_this(DBNAME)
    os.unlink(DBNAME)


if __name__ == '__main__':
    main()