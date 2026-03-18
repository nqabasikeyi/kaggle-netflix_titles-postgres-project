import pandas as pd
from sqlalchemy import create_engine

# PostgreSQL connection details
username = "postgres"
password = "" #my personal account password
host = "localhost"
port = "5432"
database = "netflix_db" 

engine = create_engine(
    f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}"
)

base_path = r"C:/Users/NqabaXO/Desktop/git-proj-kaggle/kaggle-netflix_titles-postgres-project/data/normalized/"

files = {
    "show": "shows.csv",
    "director": "directors.csv",
    "actor": "actors.csv",
    "country": "countries.csv",
    "genre": "genres.csv",
    "show_director": "show_directors.csv",
    "show_actor": "show_actors.csv",
    "show_country": "show_countries.csv",
    "show_genre": "show_genres.csv",
}

for table_name, file_name in files.items():
    file_path = base_path + file_name
    df = pd.read_csv(file_path)

    df.to_sql(table_name, engine, if_exists="append", index=False)
    print(f"Loaded {file_name} into table {table_name}")

print("All files loaded successfully.")
