DROP TABLE IF EXISTS dogs;

-- A1
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
('Goldiy', 'Golden Retriever', 16, 'male', 'Golden', '2007-01-01', 12); 

-- A2 
SELECT * FROM dogs;
 
-- A3
SELECT name FROM dogs;
 
-- A4
SELECT name FROM dogs WHERE age = 8;

-- A5
SELECT * FROM dogs WHERE name = 'Luna'; 

-- A6
SELECT * FROM dogs WHERE gender = 'Female' LIMIT 3 OFFSET 3;

-- A7 
SELECT owner_id FROM dogs WHERE owner_id > 10 AND owner_id < 20;

-- A8 
SELECT * FROM dogs WHERE age = 4 AND gender = 'Male';

-- A9 
SELECT * FROM dogs WHERE breed = 'Golden Retriever' AND age < 8 AND gender = 'Male';

-- A10 
SELECT name FROM dogs WHERE age < 5 AND gender ='Female' LIMIT 3;

-- A11 
SELECT * FROM dogs WHERE age > 4 AND color = 'Golden' LIMIT 2;

-- A12 
SELECT name FROM dogs WHERE owner_id IN (
  SELECT owner_id FROm dogs WHERE name = 'Charlie');

-- A13
SELECT name FROM dogs WHERE owner_id IN (
  SELECT owner_id FROM dogs WHERE name = 'Buddy' OR name = 'Luna');

-- A14 
WITH sub AS (
  SELECT owner_id FROM dogs WHERE breed = 'Golden Retriever')
  
SELECT name FROM dogs
WHERE owner_id in (SELECT owner_id FROM sub);


-- A15 
wITH sub AS (
  SELECT owner_id FROM dogs WHERE color = 'Golden')

SELECT * FROM dogs
WHERE age < 5 AND owner_id IN (SELECT owner_id FROM sub);

-- A16
SELECT name AS Female_dogs_under_the_age_of_5
FROM dogs WHERE age < 5 AND gender ='Female' LIMIT 3;

-- A17
SELECT name AS Hundename, color AS Fellfarbe
FROM dogs;

-- A18
SELECT *
FROM dogs AS hundeinfo WHERE age > 4;
