
import random
from datetime import datetime, timedelta
from pathlib import Path

import pandas as pd

# ---------------- PROJECT CONFIGURATION ----------------

NUM_CUSTOMERS = 1000
NUM_STORES = 20
NUM_DAYS = 7

GPS_INTERVAL_MINUTES = 15
START_DATE = datetime(2026, 11, 23)

# Approximate geographical area around Mandya
CENTER_LATITUDE = 12.5221
CENTER_LONGITUDE = 76.9000

OUTPUT_DIR = Path("data/raw")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

random.seed(42)

# ---------------- GENERATE RETAIL STORES ----------------

stores = []

for i in range(1, NUM_STORES + 1):
    stores.append({
        "store_id": f"STORE_{i:03d}",
        "store_name": f"Retail Store {i}",
        "store_category": random.choice([
            "Supermarket",
            "Clothing",
            "Electronics",
            "Grocery",
            "Pharmacy"
        ]),
        "latitude": CENTER_LATITUDE + random.uniform(-0.025, 0.025),
        "longitude": CENTER_LONGITUDE + random.uniform(-0.025, 0.025)
    })

stores_df = pd.DataFrame(stores)

# ---------------- GENERATE CUSTOMER GPS DATA ----------------

gps_records = []

for customer_number in range(1, NUM_CUSTOMERS + 1):

    customer_id = f"CUST_{customer_number:04d}"

    # Each customer has a starting location
    base_latitude = CENTER_LATITUDE + random.uniform(-0.025, 0.025)
    base_longitude = CENTER_LONGITUDE + random.uniform(-0.025, 0.025)

    for day in range(NUM_DAYS):

        current_date = START_DATE + timedelta(days=day)

        # Simulated active hours: 9 AM to 9 PM
        for hour in range(9, 21):

            for minute in [0, 15, 30, 45]:

                timestamp = current_date.replace(
                    hour=hour,
                    minute=minute
                )

                latitude = base_latitude + random.uniform(-0.003, 0.003)
                longitude = base_longitude + random.uniform(-0.003, 0.003)

                gps_records.append({
                    "event_id": f"EVT_{len(gps_records) + 1:08d}",
                    "customer_id": customer_id,
                    "timestamp": timestamp,
                    "latitude": latitude,
                    "longitude": longitude,
                    "accuracy_m": round(random.uniform(5, 30), 2)
                })

# ---------------- SAVE DATASETS ----------------

gps_df = pd.DataFrame(gps_records)

gps_df.to_csv(OUTPUT_DIR / "gps_mobility.csv", index=False)
stores_df.to_csv(OUTPUT_DIR / "stores.csv", index=False)

# ---------------- DISPLAY SUMMARY ----------------

print("GeoPulse GPS Data Generation Completed!")
print("----------------------------------------")
print("Total customers:", NUM_CUSTOMERS)
print("Total stores:", NUM_STORES)
print("Total GPS records:", len(gps_df))
print("Duration:", NUM_DAYS, "days")
print("GPS interval:", GPS_INTERVAL_MINUTES, "minutes")
print("GPS dataset columns:", list(gps_df.columns))
print("Store dataset columns:", list(stores_df.columns))
print("Output directory:", OUTPUT_DIR)
