# 🎬 Netflix Data Engineering Project

This project demonstrates an end-to-end data pipeline using the Netflix Titles dataset from Kaggle.  
The pipeline includes data extraction, cleaning, normalization, and loading into a PostgreSQL database for analysis.

---

## 📌 Project Overview

The goal of this project is to transform raw Netflix data into a structured relational database that can be queried using SQL.

### Workflow:


Raw CSV → Data Cleaning → Data Normalization → PostgreSQL → SQL Analysis


---

## 📂 Project Structure


kaggle-netflix_titles-postgres-project/
│
├── data/
│ ├── raw/
│ │ └── netflix_titles.csv
│ ├── cleaned/
│ │ └── netflix_titles_cleaned.csv
│ └── normalized/
│ ├── shows.csv
│ ├── directors.csv
│ ├── actors.csv
│ ├── countries.csv
│ ├── genres.csv
│ ├── show_directors.csv
│ ├── show_actors.csv
│ ├── show_countries.csv
│ └── show_genres.csv
│
├── notebooks/
│ └── explore.ipynb
│
├── etl/
│ ├── extract.py
│ ├── transform.py
│ ├── normalize_data.py
│ └── load_data.py
│
├── sql/
│ ├── create_database.sql
│ ├── create_tables.sql
│ └── analysis_queries.sql
│
├── requirements.txt
└── README.md


---

## ⚙️ Technologies Used

- Python (pandas, SQLAlchemy)
- PostgreSQL
- pgAdmin
- Jupyter Notebook
- Git & GitHub

---

## 🔄 ETL Pipeline

### 1. Extract
Data is loaded from the raw CSV file using `extract.py`.

### 2. Transform
Data cleaning includes:
- Handling missing values
- Removing duplicates
- Standardizing text

### 3. Normalize
The dataset is split into multiple relational tables:
- shows
- directors
- actors
- countries
- genres
- bridge tables (many-to-many relationships)

### 4. Load
Normalized CSV files are loaded into PostgreSQL using `load_data.py`.

---

## 🗄️ Database Schema

The database is designed using a normalized relational model:

- **shows**
- **directors**
- **actors**
- **countries**
- **genres**
- **show_directors**
- **show_actors**
- **show_countries**
- **show_genres**

---

## 🚀 How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/your-username/kaggle-netflix_titles-postgres-project.git
cd kaggle-netflix_titles-postgres-project
```
### 2. Install dependencies

```bash 
pip install -r requirements.txt
```

### 3. Clean the data

Run the notebook:

```bash
notebooks/explore.ipynb
```
This generates:
data/cleaned/netflix_titles_cleaned.csv

### 4. Normalize the data

```bash 
python etl/normalize_data.py
```
### 5. Create PostgreSQL database

Using pgAdmin or SQL:
```bash
CREATE DATABASE kaggle_netflix_db;
```
### 6. Create tables
Run:
```bash
sql/create_tables.sql
```
### 7. Load data into PostgreSQL
```bash
python etl/load_data.py
```

## 📊 Example SQL Queries
#### Count Movies vs TV Shows
```bash
SELECT type, COUNT(*) AS total
FROM shows
GROUP BY type;
Top 10 Genres
```

```bash
SELECT g.name, COUNT(*) AS total
FROM genres g
JOIN show_genres sg ON g.genre_id = sg.genre_id
GROUP BY g.name
ORDER BY total DESC
LIMIT 10;
```
#### Most Common Ratings
```bash
SELECT rating, COUNT(*) AS total
FROM shows
GROUP BY rating
ORDER BY total DESC;
```
## 📈 Key Learnings

Data cleaning using pandas

Data normalization and relational modeling

Building ETL pipelines

Loading data into PostgreSQL using Python

Writing analytical SQL queries

## 🔒 Notes

The PostgreSQL database is not included in this repository.

Use the provided SQL scripts and CSV files to recreate it locally.

Ensure your PostgreSQL credentials are configured correctly in load_data.py.

## ✨ Future Improvements

Automate the pipeline using Airflow

Add data visualizations (Power BI / Tableau)

Deploy the pipeline to the cloud (AWS/GCP)

## 📬 Author

Nqaba Jabulani Sikeyi