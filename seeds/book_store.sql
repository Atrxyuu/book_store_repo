-- 1. Wipe the slate completely clean
DROP TABLE IF EXISTS books;

-- 2. Build a brand new table structure
CREATE TABLE books (
  id SERIAL PRIMARY KEY,
  title TEXT,
  author TEXT
);

INSERT INTO books (title, author) VALUES ('The Gruffalo', 'Julia Donaldson');
INSERT INTO books (title, author) VALUES ('Ada Twist, Scientist', 'Andrea Beaty');
INSERT INTO books (title, author) VALUES ('The Girl Who Drank the Moon', 'Kelly Barnhill');
INSERT INTO books (title, author) VALUES ('Dragons in a Bag', 'Zetta Elliott');
