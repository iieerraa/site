CREATE TABLE IF NOT EXISTS mainmenu (
id integer PRIMARY KEY AUTOINCREMENT,
title text NOT NULL,
url text NOT NULL
);


CREATE TABLE IF NOT EXISTS user (
id integer PRIMARY KEY AUTOINCREMENT,
email text NOT NULL,
psw text NOT NULL,
time integer NOT NULL
);
