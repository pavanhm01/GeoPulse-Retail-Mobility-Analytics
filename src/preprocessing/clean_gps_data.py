import pandas as pd
from pathlib import Path

# ---------------- PROJECT PATHS ----------------

INPUT_FILE = Path("data/raw/gps_mobility.csv")
OUTPUT_DIR = Path("data/processed")

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# ---------------- LOAD RAW DATA ----------------

gps_df = pd.read_csv(INPUT_FILE)

print("GeoPulse Data Cleaning Started!")
print("--------------------------------")

print("Original dataset shape:", gps_df.shape)

print("\nFirst 5 records:")
print(gps_df.head())

print("\nDataset information:")
print(gps_df.info())
# ---------------- DATA CLEANING ----------------

print("\nStarting data cleaning...")

# Convert timestamp into datetime format
gps_df["timestamp"] = pd.to_datetime(
    gps_df["timestamp"],
    errors="coerce"
)

# Remove duplicate event IDs
gps_df = gps_df.drop_duplicates(
    subset=["event_id"]
)

# Remove missing values
gps_df = gps_df.dropna()

# Validate latitude
gps_df = gps_df[
    gps_df["latitude"].between(-90, 90)
]

# Validate longitude
gps_df = gps_df[
    gps_df["longitude"].between(-180, 180)
]

# Validate GPS accuracy
gps_df = gps_df[
    gps_df["accuracy_m"].between(0, 100)
]

print("Data cleaning completed!")
print("Cleaned dataset shape:", gps_df.shape)
# ---------------- FINAL VALIDATION ----------------

print("\nFinal Data Validation")
print("---------------------")

print("Missing values:", gps_df.isnull().sum().sum())
print("Duplicate event IDs:", gps_df["event_id"].duplicated().sum())
print("Invalid timestamps:", gps_df["timestamp"].isna().sum())
print("Invalid latitude:", (~gps_df["latitude"].between(-90, 90)).sum())
print("Invalid longitude:", (~gps_df["longitude"].between(-180, 180)).sum())

# ---------------- SAVE CLEANED DATA ----------------

OUTPUT_FILE = OUTPUT_DIR / "cleaned_gps_mobility.csv"

gps_df.to_csv(OUTPUT_FILE, index=False)

print("\nData cleaning completed successfully!")
print("Original records: 336000")
print("Cleaned records:", len(gps_df))
print("Removed records:", 336000 - len(gps_df))
print("Final dataset shape:", gps_df.shape)
print("Timestamp data type:", gps_df["timestamp"].dtype)
print("Saved file:", OUTPUT_FILE)