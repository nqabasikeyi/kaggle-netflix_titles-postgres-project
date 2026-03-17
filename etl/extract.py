import pandas as pd
from pathlib import Path


def extract_data(file_path: str) -> pd.DataFrame:
    """
    Extract data from a CSV file and return a pandas DataFrame.
    """

    try:
        df = pd.read_csv(file_path)
        print(f"Data successfully loaded from {file_path}")
        print(f"Shape: {df.shape}")
        return df

    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        raise

    except Exception as e:
        print(f"Error while reading file: {e}")
        raise


if __name__ == "__main__":
    # Build path dynamically (avoids path issues)
    BASE_DIR = Path(__file__).resolve().parent.parent
    file_path = BASE_DIR / "data" / "raw" / "netflix_titles.csv"

    df = extract_data(file_path)

    # Quick preview
    print(df.head())