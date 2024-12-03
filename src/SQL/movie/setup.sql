CREATE TABLE IF NOT EXISTS movie(
    imdbid VARCHAR(10) NOT NULL, 
    title VARCHAR(255), 
    year INT(4), 
    rating VARCHAR(5) CHECK( rating IN ('G', 'PG', 'PG-13', 'R', 'NC-17', 'NR')),
    runtime VARCHAR(255),
    genre TEXT,
    director VARCHAR(255),
    writer VARCHAR(255),
    actors TEXT,
    plot TEXT,
    score FLOAT(3), 
    PRIMARY KEY (imdbid)
);
