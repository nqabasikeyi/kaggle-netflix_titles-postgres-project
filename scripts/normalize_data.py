import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
INPUT_FILE = BASE_DIR / "data" / "raw" / "netflix_titles_cleaned.csv"
OUTPUT_DIR = BASE_DIR / "data" / "normalized"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(INPUT_FILE)

# Convert date_added to proper date format
df["date_added"] = pd.to_datetime(df["date_added"], errors="coerce")

shows = df[
    [
        "show_id",
        "type",
        "title",
        "date_added",
        "release_year",
        "rating",
        "duration",
        "description",
    ]
].copy()

shows.to_csv(OUTPUT_DIR / "shows.csv", index=False)

def create_lookup_and_bridge(dataframe, source_column, entity_name, entity_id_col, bridge_name):
    temp = dataframe[["show_id", source_column]].copy()

    temp[source_column] = temp[source_column].fillna("Unknown").apply(
        lambda x: [item.strip() for item in str(x).split(",")]
    )

    exploded = temp.explode(source_column)
    exploded = exploded[exploded[source_column].notna()]
    exploded = exploded[exploded[source_column] != ""]

    lookup = (
        exploded[source_column]
        .drop_duplicates()
        .sort_values()
        .reset_index(drop=True)
        .to_frame(name="name")
    )
    lookup[entity_id_col] = range(1, len(lookup) + 1)
    lookup = lookup[[entity_id_col, "name"]]

    bridge = exploded.merge(lookup, left_on=source_column, right_on="name", how="left")
    bridge = bridge[["show_id", entity_id_col]].drop_duplicates().reset_index(drop=True)

    lookup.to_csv(OUTPUT_DIR / f"{entity_name}.csv", index=False)
    bridge.to_csv(OUTPUT_DIR / f"{bridge_name}.csv", index=False)

create_lookup_and_bridge(df, "director", "directors", "director_id", "show_directors")
create_lookup_and_bridge(df, "cast", "actors", "actor_id", "show_actors")
create_lookup_and_bridge(df, "country", "countries", "country_id", "show_countries")
create_lookup_and_bridge(df, "listed_in", "genres", "genre_id", "show_genres")

print(f"Normalized CSV files saved in: {OUTPUT_DIR}")