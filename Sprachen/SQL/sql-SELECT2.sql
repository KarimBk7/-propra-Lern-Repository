DROP TABLE IF EXISTS dogs;


CREATE TABLE dogs(
  name TEXT,
  breed TEXT,
  age INT,
  gender TEXT,
  color TEXT,
  birthdate TEXT, 
  owner_id INT
);

INSERT INTO dogs
VALUES ('Buddy', 'Labrador Retriever', 3, 'Male', 'Golden', '2019-05-10', 1),
('Max', 'German Shepherd', 5, 'Male', 'Black and Tan', '2017-08-15', 2),
('Bella', 'Golden Retriever', 2, 'Female', 'Golden', '2020-02-20', 3),
('Charlie', 'Poodle', 4, 'Male', 'White', '2018-11-28', 1),
('Lucy', 'Beagle', 6, 'Female', 'Tricolor', '2016-04-03', 4),
('Rocky', 'Boxer', 3, 'Male', 'Brindle', '2019-09-08', 5),
('Luna', 'Siberian Husky', 1, 'Female', 'Gray and White', '2023-01-15', 6),
('Bailey', 'Dachshund', 8, 'Female', 'Red', '2015-07-20', 7),
('Cooper', 'Golden Retriever', 2, 'Male', 'Golden', '2020-03-25', 8),
('Molly', 'Yorkshire Terrier', 5, 'Female', 'Black and Tan', '2017-11-12', 9),
('Duke', 'Doberman Pinscher', 4, 'Male', 'Black and Rust', '2018-04-30', 10),
('Zoe', 'Shih Tzu', 7, 'Female', 'White and Brown', '2015-12-03', 11),
('Goldix', 'Golden Retriever', 6, 'Female', 'Golden', '2017-01-01', 12),
('Goldiy', 'Golden Retriever', 16, 'Male', 'Golden', '2007-01-01', 12); 


-- A1
SELECT COUNT(*) FROM dogs;

-- A2 
SELECT COUNT(age) FROM dogs;

-- A3
SELECT AVG(owner_id) FROM dogs;

-- A4 
SELECT MIN(age) FROM dogs;

-- A5 
SELECT MAX(age) FROM dogs;

-- A6 
SELECT AVG(age) FROM dogs
WHERE gender = 'Female';

-- A7 
SELECT SUM(age) FROM dogs
WHERE breed = 'Golden Retriever';

-- A8 
SELECT COUNT(*) FROM dogs
WHERE gender = 'Male';

-- A9 
SELECT breed FROM dogs
GROUP BY breed;

-- A10 
SELECT owner_id, COUNT(*) FROM dogs
GROUP BY owner_id;

-- A11 
SELECT gender, AVG(age) FROM dogs
GROUP BY gender;

-- A12 
SELECT COUNT(owner_id) FROM (
  SELECT owner_id FROM dogs
  GROUP BY owner_id HAVING COUNT(*) > 1
);

-- A13
SELECT breed FROM dogs
GROUP BY breed HAVING COUNT(*) > 2;

-- A14 
SELECT name, age FROM dogs
ORDER BY age ASC;

-- A15
SELECT name, age, breed FROM dogs
ORDER BY age DESC, breed ASC;

-- A16 
SELECT COUNT(DISTINCT color) FROM dogs;

-- A17 
SELECT DISTINCT breed FROM dogs;

-- A18 
SELECT * FROM dogs
WHERE name LIKE 'B%';

-- A19 
SELECT * FROm dogs 
WHERE breed LIKE '%Retriever%';

-- A20 
INSERT INTO dogs
VALUES ('Shadow', 'Mixed', 2, 'Male', NULL, '2022-06-06', 13);

-- A21 
SELECT * FROM dogs
WHERE color IS NULL;

 -- A22 
 SELECT COUNT(*) FROM dogs
 WHERE color IS NULL;
 
 -- A23
 SELECT UPPER(breed) FROM dogs;
 
 -- A24 
 SELECT name, LENGTH(name) FROm dogs;