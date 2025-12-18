import pandas as pd
from pandas.api.types import CategoricalDtype

def apply_column_dtypes(df: pd.DataFrame, dtype_map: dict) -> pd.DataFrame:
    df = df.copy()

    for col, dtype_def in dtype_map.items():
        if isinstance(dtype_def, CategoricalDtype):
            df[col] = df[col].astype("category").cat.set_categories(
                dtype_def.categories,
                ordered=dtype_def.ordered,
            )

        elif dtype_def == "string":
            df[col] = df[col].astype("string")

        elif dtype_def == "category":
            df[col] = df[col].astype("category")

        elif dtype_def.startswith("int"):
            # Use nullable int for safety
            df[col] = pd.to_numeric(df[col], errors="coerce").astype("Int64")

        elif dtype_def.startswith("float"):
            df[col] = pd.to_numeric(df[col], errors="coerce").astype("float64")

        else:
            df[col] = df[col].astype(dtype_def)

    return df
