DROP TABLE IF EXISTS websites;

-- A1
CREATE TABLE websites(
  id INT PRIMARY KEY,
  name TEXT,
  url TEXT,
  alexa INT,
  country TEXT
);

INSERT INTO websites
VALUES  (1, 'Google', 'https://www.google.com/', 1, 'USA'),
        (2, 'Taobao', 'https://www.taobao.com/', 13, 'CN'),
        (3, 'Runoob', 'http://www.runoob.com/', 5000, 'USA'),
        (4, 'Weibo', 'http://weibo.com/', 20, 'CN'),
        (5, 'Facebook', 'https://www.facebook.com/', 3, 'USA');


-- A2
UPDATE websites
SET alexa = 4689
WHERE name = 'Runoob';

-- A3 
UPDATE websites
SET alexa = 2,
    country = 'Global'
WHERE name = 'Facebook';

-- A4 
UPDATE websites
SET country = 'China'
WHERE country = 'CN';

-- A5
SELECT *
FROM websites;

-- A6 
UPDATE websites
SET country = 'TEST';

-- A7 
SELECT *
FROM websites;

-- A8 
DROP TABLE IF EXISTS websites;

CREATE TABLE websites (
  id      INTEGER PRIMARY KEY,
  name    TEXT,
  url     TEXT,
  alexa   INTEGER,
  country TEXT
);

INSERT INTO websites 
VALUES  (1, 'Google',   'https://www.google.com/',   1,    'USA'),
        (2, 'Taobao',   'https://www.taobao.com/',   13,   'CN'),
        (3, 'Runoob',   'http://www.runoob.com/',    5000, 'USA'),
        (4, 'Weibo',    'http://weibo.com/',         20,   'CN'),
        (5, 'Facebook', 'https://www.facebook.com/', 3,    'USA');

-- A9 
CREATE VIEW usa_websites AS
SELECT *
FROM websites
WHERE country = 'USA';
 
-- A10 
CREATE VIEW top_websites AS
SELECT *
FROM websites
WHERE alexa < 100;

-- A11 
SELECT * FROM usa_websites;

SELECT * FROM top_websites;

-- A12 
DROP VIEW IF EXISTS usa_websites;

-- A13 
SELECT * FROM usa_websites;

-- A14 
CREATE VIEW usa_websites AS
SELECT *
FROM websites
WHERE country = 'USA';

-- A15 
CREATE VIEW website_info AS
SELECT
  name   AS site_name,
  url    AS domain,
  alexa  AS popularity_rank,
  country AS region
FROM websites;

-- A16 
CREATE VIEW website_categories AS
SELECT
  name,
  url,
  alexa,
  country,
  CASE
    WHEN alexa <= 10 THEN 'Top Tier'
    ELSE 'Standard'
  END AS category
FROM websites;

-- A17 
UPDATE websites
SET alexa = 2
WHERE name = 'Google';

-- A18 
SELECT *
FROM top_websites;

-- A19 
SELECT *
FROM website_categories;

-- A20 
CREATE VIEW outdated_rankings AS
SELECT *
FROM websites
WHERE alexa > 1000;

-- A21 
ALTER TABLE websites
ADD COLUMN status TEXT DEFAULT 'active';

-- A22 
UPDATE websites
SET status = 'needs_review'
WHERE alexa > 1000;

-- A23 
CREATE VIEW website_summary AS
SELECT
  country,
  COUNT(*) AS website_count
FROM websites
GROUP BY country;

-- A24 
DROP VIEW IF EXISTS website_summary;

CREATE VIEW website_summary AS
SELECT
  country,
  COUNT(*) AS website_count,
  AVG(alexa) AS avg_alexa
FROM websites
GROUP BY country;
