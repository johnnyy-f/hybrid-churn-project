import pandas as pd
from pathlib import Path

def load_raw_data(path: str) -> pd.DataFrame:
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")
    
    df = pd.read_csv(path, low_memory=False)
    return df

def initial_cleaning(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # Fix TotalCharges: contains " " blanks -> convert to numeric
    if "TotalCharges" in df.columns:
        df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

    if "SeniorCitizen" in df.columns:
        df["SeniorCitizen"] = df["SeniorCitizen"].astype(str)

    # Clean object columns: strip whitespace, convert "" to NA
    obj_cols = df.select_dtypes(include=["object"]).columns
    for c in obj_cols:
        df[c] = df[c].astype("string").str.strip().replace({"": pd.NA})

    return df

from .column_schema import COLUMN_DTYPES
from .type_utils import apply_column_dtypes
from .schema_validation import validate_df
import pandas as pd

def load_and_prepare(path: str) -> pd.DataFrame:
    df = load_raw_data(path)
    df = initial_cleaning(df)
    df = apply_column_dtypes(df, COLUMN_DTYPES)
    validate_df(df)
    return df
