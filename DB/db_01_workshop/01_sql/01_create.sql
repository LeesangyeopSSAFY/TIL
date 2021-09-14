-- 1-1번 답
CREATE TABLE countries (
id INTEGER PRIMARY KEY,
room_num TEXT,
check_in TEXT,
check_out TEXT,
grade TEXT,
price INTEGER
);

-- 1-3
ALTER TABLE countries RENAME TO hotels;

-- 1-4
SELECT room_num, price FROM hotels
ORDER BY price DESC LIMIT 2;

-- 1-5
SELECT grade, COUNT(*) FROM hotels
GROUP BY grade
ORDER BY COUNT(*) DESC;

-- 1-6
SELECT * FROM hotels
WHERE room_num LIKE 'B%' OR grade='deluxe';

-- 1-7
SELECT * FROM hotels
WHERE room_num NOT LIKE 'B%' AND check_in='2020-01-04'
ORDER BY price ASC;