-- lib/create.sql
CREATE TABLE bears (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  age INTEGER,
  sex TEXT CHECK(sex IN ('M', 'F')),
  color TEXT,
  temperament TEXT,
  alive BOOLEAN
);
