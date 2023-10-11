CREATE DATABASE data;
\connect data
CREATE TABLE entered_data(word TEXT, time TEXT);
INSERT INTO entered_data(word, time) VALUES ('hello', Now());