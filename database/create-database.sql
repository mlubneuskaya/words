DO $$ BEGIN
    IF NOT EXISTS (SELECT FROM pg_database WHERE datname = 'data') THEN
        CREATE DATABASE data;
    END IF;
END $$;

\connect data

CREATE TABLE IF NOT EXISTS entered_data(word TEXT, time TEXT);
INSERT INTO entered_data(word, time) VALUES ('hello', Now());
