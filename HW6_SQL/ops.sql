INSERT INTO genders (name)
VALUES ('male'), ('female');

INSERT INTO users (name, email, password, age, gender_id)
VALUES ('Boris', 'boris@test.com', 'password', 23, 1),
('Alina', 'alina@test.com', 'password', 32, 2),
('Maksim', 'maksim@test.com', 'password', 40, 1);

INSERT INTO contacts (name, email, phone, favorite, user_id)
VALUES ('Allen Raymond', 'nulla.ante@vestibul.co.uk', '(992) 914-3792', 0, 1),
('Chaim Lewis', 'dui.in@egetlacus.ca', '(294) 840-6685', 1, 1),
('Kennedy Lane', 'mattis.Cras@nonenimMauris.net', '(542) 451-7038', 1, 2),
('Wylie Pope', 'est@utquamvel.net', '(692) 802-2949', 0, 2),
('Cyrus Jackson', 'nibh@semsempererat.com', '(501) 472-5218', 0, null);


SELECT * FROM contacts 

SELECT name, email FROM contacts ORDER BY name

SELECT ID, NAME, email, AGE
FROM USERS
WHERE age BETWEEN 23 AND 39
ORDER BY name;

SELECT ID, NAME, email
FROM CONTACTS C
WHERE email LIKE '%co_%'
ORDER BY name;

SELECT COUNT(*)
FROM contacts c;

SELECT round(avg(age), 2) as avg_age
FROM users u;

SELECT *
FROM contacts c
where user_id in (select id from users where age BETWEEN 23 and 39);

UPDATE  contacts set user_id = 3
where id = 5;

ALTER TABLE users ADD telegram
varchar(50)

SELECT *
FROM contacts c
join users u on u.id = c.user_id;
where age BETWEEN 24 and 39