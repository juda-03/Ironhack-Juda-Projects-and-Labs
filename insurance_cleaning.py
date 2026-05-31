import pandas as pd


def clean_column_names(df):
    insurance_clean_df = df.copy()

    insurance_clean_df.columns = (
        insurance_clean_df.columns
        .str.lower()
        .str.replace(" ", "_", regex=False)
    )

    insurance_clean_df = insurance_clean_df.rename(columns={"st": "state"})

    return insurance_clean_df


def clean_invalid_values(df):
    insurance_clean_df = df.copy()

    insurance_clean_df["gender"] = insurance_clean_df["gender"].replace({
        "Male": "M",
        "Female": "F",
        "Femal": "F",
        "female": "F",
    })

    insurance_clean_df["state"] = insurance_clean_df["state"].replace({
        "Cali": "California",
        "WA": "Washington",
        "AZ": "Arizona",
    })

    insurance_clean_df["education"] = insurance_clean_df["education"].replace({
        "Bachelors": "Bachelor",
    })

    insurance_clean_df["customer_lifetime_value"] = (
        insurance_clean_df["customer_lifetime_value"]
        .str.replace("%", "", regex=False)
    )

    insurance_clean_df["vehicle_class"] = insurance_clean_df["vehicle_class"].replace({
        "Sports Car": "Luxury",
        "Luxury Car": "Luxury",
        "Luxury SUV": "Luxury",
    })

    return insurance_clean_df


def format_data_types(df):
    insurance_clean_df = df.copy()

    insurance_clean_df["customer_lifetime_value"] = pd.to_numeric(
        insurance_clean_df["customer_lifetime_value"],
        errors="coerce",
    )

    insurance_clean_df["number_of_open_complaints"] = (
        insurance_clean_df["number_of_open_complaints"]
        .str.split("/")
        .str[1]
    )

    insurance_clean_df["number_of_open_complaints"] = pd.to_numeric(
        insurance_clean_df["number_of_open_complaints"],
        errors="coerce",
    )

    return insurance_clean_df


def handle_null_values(df):
    insurance_clean_df = df.copy()

    insurance_clean_df = insurance_clean_df.dropna(subset=["customer"]).copy()
    insurance_clean_df.loc[:, "gender"] = insurance_clean_df["gender"].fillna("Unknown")

    return insurance_clean_df


def remove_duplicates(df):
    insurance_clean_df = df.copy()

    insurance_clean_df = insurance_clean_df.drop_duplicates()
    insurance_clean_df = insurance_clean_df.reset_index(drop=True)

    return insurance_clean_df


def clean_insurance_data(df):
    insurance_clean_df = clean_column_names(df)
    insurance_clean_df = clean_invalid_values(insurance_clean_df)
    insurance_clean_df = format_data_types(insurance_clean_df)
    insurance_clean_df = handle_null_values(insurance_clean_df)
    insurance_clean_df = remove_duplicates(insurance_clean_df)

    return insurance_clean_df
