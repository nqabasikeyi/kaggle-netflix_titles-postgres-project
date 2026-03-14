CREATE TABLE shows (
    show_id VARCHAR(10) PRIMARY KEY,
    type VARCHAR(20),
    title TEXT NOT NULL,
    date_added DATE,
    release_year INT,
    rating VARCHAR(20),
    duration VARCHAR(50),
    description TEXT
);

CREATE TABLE directors (
    director_id INT PRIMARY KEY,
    name TEXT UNIQUE NOT NULL
);

CREATE TABLE show_directors (
    show_id VARCHAR(10),
    director_id INT,
    PRIMARY KEY (show_id, director_id),
    FOREIGN KEY (show_id) REFERENCES shows(show_id),
    FOREIGN KEY (director_id) REFERENCES directors(director_id)
);

CREATE TABLE actors (
    actor_id INT PRIMARY KEY,
    name TEXT UNIQUE NOT NULL
);

CREATE TABLE show_actors (
    show_id VARCHAR(10),
    actor_id INT,
    PRIMARY KEY (show_id, actor_id),
    FOREIGN KEY (show_id) REFERENCES shows(show_id),
    FOREIGN KEY (actor_id) REFERENCES actors(actor_id)
);

CREATE TABLE countries (
    country_id INT PRIMARY KEY,
    name TEXT UNIQUE NOT NULL
);

CREATE TABLE show_countries (
    show_id VARCHAR(10),
    country_id INT,
    PRIMARY KEY (show_id, country_id),
    FOREIGN KEY (show_id) REFERENCES shows(show_id),
    FOREIGN KEY (country_id) REFERENCES countries(country_id)
);

CREATE TABLE genres (
    genre_id INT PRIMARY KEY,
    name TEXT UNIQUE NOT NULL
);

CREATE TABLE show_genres (
    show_id VARCHAR(10),
    genre_id INT,
    PRIMARY KEY (show_id, genre_id),
    FOREIGN KEY (show_id) REFERENCES shows(show_id),
    FOREIGN KEY (genre_id) REFERENCES genres(genre_id)
);