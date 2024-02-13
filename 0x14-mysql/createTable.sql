CREATE DATABASE tyrell_corp;
USE tyrell_corp;
CREATE TABLE nexus6(id INTEGER, name TEXT);
INSERT INTO nexus6 VALUES (0, "watch");
GRANT SELECT ON tyrell_corp.nexus6 TO holberton_user@localhost;
