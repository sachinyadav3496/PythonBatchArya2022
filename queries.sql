SHOW DATABASES;
USE world;
SHOW TABLES;
DESCRIBE country;
DESCRIBE city;
DESCRIBE countrylanguage;

SELECT COUNT(*) FROM country;
SELECT COUNT(*) FROM city;

SELECT Code, Name, Continent, SurfaceArea, Population FROM Country ORDER BY  SurfaceArea DESC LIMIT 10;

SELECT DISTINCT(Continent) FROM Country;

CREATE TABLE A(gender ENUM("M", "F", "O"), salary DOUBLE);
INSERT INTO A VALUES ("M", 20), ("F", 30), ("F", 20), ("M", 30), ("M", 30), ("F", 20), ("M", 30), ("M", 20); 

SELECT * FROM A;

SELECT gender, COUNT(gender) AS `Frequency` FROM A GROUP BY gender;

SELECT gender, COUNT(gender) AS `Count`, SUM(salary) AS `Total Sum`, AVG(salary) AS `Average Salary` FROM A GROUP BY gender ORDER BY `Average Salary` DESC;  


DESC Country;


SELECT Continent, COUNT(Code) AS `Count`, SUM(Population) as `Total Population` FROM Country GROUP BY Continent ORDER BY `Count` DESC;

# SQL JOINs  
/* List top 10 Countries According to Surface Area;
SORTING -> [ ['sachin', 30], ['ravi', 40], ['rajat', 70], ['gaurav', 50] ]
.sort(key=lambda v:v[1], reverse=True)[:10]
SELECT * FROM data ORDER BY marks DESC LIMIT 10;
*/

/* List how many country each  Continent have ? */

