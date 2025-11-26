-- A1
DROP TABLE IF EXISTS dogs;
CREATE TABLE dogs(
	DogID INT,
    DogName TEXT,
    Gender TEXT,
    Age INT
);

-- A2
ALTER TABLE dogs
	ADD COLUMN Owner TEXT;
    
-- A3
ALTER TABLE dogs
	RENAME COLUMN Age TO DogAge;
-- A4    
ALTER TABLE dogs	
	DROP COLUMN Owner;
    
    
-- A5
DROP TABLE IF EXISTS dogs;

-- A6
CREATE TABLE dogs(
	DogID INT PRIMARY KEY,
    DogName TEXT NOT NULL,
    Gender TEXT,
    Age INT
);

-- A7
INSERT INTO dogs (dogid, dogname, gender, age)
VALUES(1, 'Maggus', 'M',3);

INSERT INTO dogs (dogid, dogname, gender, age)
VALUES(2, 'Rex', 'M',5);

INSERT INTO dogs (dogid, dogname, gender, age)
VALUES(3, 'Susie', 'F',2);

INSERT INTO dogs (dogid, dogname, gender, age)
VALUES(4, 'Sauer', 'F',8);


-- A8
SELECT dogname, age FROM dogs;

-- A9
SELECT * FROM dogs;

-- A10 
SELECT dogname, age FROM dogs
WHERE age > 4;

-- A11 
DELETE FROM dogs
WHERE dogid = 1;

-- A12 
DELETE FROM dogs
WHERE dogid != 2;


