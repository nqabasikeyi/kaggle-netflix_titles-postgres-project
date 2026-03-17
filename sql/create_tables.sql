
SET search_path TO public;

CREATE TABLE show (
    show_id VARCHAR(10) PRIMARY KEY,
    type VARCHAR(20),
    title TEXT NOT NULL,
    date_added DATE,
    release_year INT,
    rating VARCHAR(20),
    duration VARCHAR(50),
    description TEXT
);

CREATE TABLE director (
    director_id INT PRIMARY KEY,
    name TEXT UNIQUE NOT NULL
);

CREATE TABLE actor (
    actor_id INT PRIMARY KEY,
    name TEXT UNIQUE NOT NULL
);

CREATE TABLE country (
    country_id INT PRIMARY KEY,
    name TEXT UNIQUE NOT NULL
);

CREATE TABLE genre (
    genre_id INT PRIMARY KEY,
    name TEXT UNIQUE NOT NULL
);

CREATE TABLE show_director (
    show_id VARCHAR(10),
    director_id INT,
    PRIMARY KEY (show_id, director_id),
    FOREIGN KEY (show_id) REFERENCES show(show_id),
    FOREIGN KEY (director_id) REFERENCES director(director_id)
);

CREATE TABLE show_actor (
    show_id VARCHAR(10),
    actor_id INT,
    PRIMARY KEY (show_id, actor_id),
    FOREIGN KEY (show_id) REFERENCES show(show_id),
    FOREIGN KEY (actor_id) REFERENCES actor(actor_id)
);

CREATE TABLE show_country (
    show_id VARCHAR(10),
    country_id INT,
    PRIMARY KEY (show_id, country_id),
    FOREIGN KEY (show_id) REFERENCES show(show_id),
    FOREIGN KEY (country_id) REFERENCES country(country_id)
);

CREATE TABLE show_genre (
    show_id VARCHAR(10),
    genre_id INT,
    PRIMARY KEY (show_id, genre_id),
    FOREIGN KEY (show_id) REFERENCES show(show_id),
    FOREIGN KEY (genre_id) REFERENCES genre(genre_id)
);