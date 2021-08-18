CREATE TABLE IF NOT EXISTS mainmenu (
id integer PRIMARY KEY AUTOINCREMENT,
title text NOT NULL,
url text NOT NULL
);


CREATE TABLE IF NOT EXISTS user (
id integer PRIMARY KEY AUTOINCREMENT,
name text NOT NULL,
email text NOT NULL,
psw text NOT NULL,
time integer NOT NULL
);


CREATE TABLE IF NOT EXISTS content (
id integer PRIMARY KEY AUTOINCREMENT,
user integer NOT NULL REFERENCES user(time),
time integer NOT NULL,
content text NOT NULL,
photo text DEFAULT NULL
);
