CREATE DATABASE datarepresentation

CREATE TABLE game (id INT AUTO_INCREMENT PRIMARY KEY, title VARCHAR(255), developer VARCHAR(255), price INT)

insert into game (title, developer, price) values (%s,%s,%s) values ("Dayz Gone","SIE Bend Studio",40)