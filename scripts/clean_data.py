import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
RAW_FILE = BASE_DIR / "data" / "raw" / "netflix_titles.csv"
OUTPUT_FILE = BASE_DIR / "data" / "raw" / "netflix_titles_cleaned.csv"

df = pd.read_csv(RAW_FILE)

# Remove exact duplicate rows
df = df.drop_duplicates()

# Fill missing values for multi-value text columns
df["director"] = df["director"].fillna("Unknown")
df["cast"] = df["cast"].fillna("Unknown")
df["country"] = df["country"].fillna("Unknown")
df["rating"] = df["rating"].fillna("Not Rated")

# Drop rows missing important fields
df = df.dropna(subset=["date_added", "duration"])

# Strip surrounding whitespace from string columns
for col in df.select_dtypes(include="object").columns:
    df[col] = df[col].str.strip()

# Save cleaned file
OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(OUTPUT_FILE, index=False)

print(f"Cleaned dataset saved to: {OUTPUT_FILE}")
print(f"Rows remaining: {len(df)}")