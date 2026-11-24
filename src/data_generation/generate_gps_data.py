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

    # Customer's home location
    home_lat = CENTER_LATITUDE + random.uniform(-0.025, 0.025)
    home_lon = CENTER_LONGITUDE + random.uniform(-0.025, 0.025)

    # Find five nearby stores
    nearby_stores = sorted(
        stores,
        key=lambda store: (
            (store["latitude"] - home_lat) ** 2
            + (store["longitude"] - home_lon) ** 2
        )
    )[:5]

    for day in range(NUM_DAYS):

        current_date = START_DATE + timedelta(days=day)

        # Select one nearby store for the day's visit
        selected_store = random.choice(nearby_stores)

        store_lat = selected_store["latitude"]
        store_lon = selected_store["longitude"]

        # Random travel and visit timings
        departure_slot = random.randint(4, 12)
        travel_slots = random.randint(1, 4)
        arrival_slot = departure_slot + travel_slots

        dwell_slots = random.randint(2, 8)
        return_start = arrival_slot + dwell_slots

        return_slots = random.randint(1, 4)
        return_end = return_start + return_slots

        # Generate 48 GPS records per day (9 AM to 9 PM)
        for slot in range(48):

            timestamp = current_date + timedelta(
                hours=9,
                minutes=slot * GPS_INTERVAL_MINUTES
            )

            # Phase 1: Customer stays near home
            if slot < departure_slot:
                latitude = home_lat
                longitude = home_lon

            # Phase 2: Customer travels to the store
            elif slot < arrival_slot:
                progress = (
                    (slot - departure_slot + 1) / travel_slots
                )

                latitude = home_lat + (
                    store_lat - home_lat
                ) * progress

                longitude = home_lon + (
                    store_lon - home_lon
                ) * progress

            # Phase 3: Customer stays near the store
            elif slot < return_start:
                latitude = store_lat
                longitude = store_lon

            # Phase 4: Customer travels back home
            elif slot < return_end:
                progress = (
                    (slot - return_start + 1) / return_slots
                )

                latitude = store_lat + (
                    home_lat - store_lat
                ) * progress

                longitude = store_lon + (
                    home_lon - store_lon
                ) * progress

            # Phase 5: Customer stays near home
            else:
                latitude = home_lat
                longitude = home_lon

            # Add small GPS location variations
            latitude += random.uniform(-0.00008, 0.00008)
            longitude += random.uniform(-0.00008, 0.00008)

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