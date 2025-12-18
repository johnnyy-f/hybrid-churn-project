import pandera.pandas as pa
from pandera.pandas import Column, Check, DataFrameSchema


def get_telco_schema():
    return DataFrameSchema(
        {
            "customerID": Column(pa.String),
            "gender": Column(pa.String, Check.isin(["Male", "Female"])),
            # "SeniorCitizen": Column(pa.Int, Check.in_range(0, 1)),
            "SeniorCitizen": Column(pa.String),
            "Partner": Column(pa.String),
            "Dependents": Column(pa.String),
            "tenure": Column(pa.Int, Check.ge(0)),
            "PhoneService": Column(pa.String),
            "MultipleLines": Column(pa.String, nullable=True),
            "InternetService": Column(pa.String),
            "OnlineSecurity": Column(pa.String, nullable=True),
            "OnlineBackup": Column(pa.String, nullable=True),
            "DeviceProtection": Column(pa.String, nullable=True),
            "TechSupport": Column(pa.String, nullable=True),
            "StreamingTV": Column(pa.String, nullable=True),
            "StreamingMovies": Column(pa.String, nullable=True),
            "Contract": Column(pa.String),
            "PaperlessBilling": Column(pa.String),
            "PaymentMethod": Column(pa.String),
            "MonthlyCharges": Column(pa.Float, Check.ge(0)),
            "TotalCharges": Column(pa.Float, Check.ge(0), nullable=True),
            "Churn":Column(pa.String),
        },
        strict=True  # require all expected columns, forbid extras
    )

def validate_df(df):
    schema = get_telco_schema()
    return schema.validate(df, lazy=True)
