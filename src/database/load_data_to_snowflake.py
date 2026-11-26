import os
from pathlib import Path

import pandas as pd
import snowflake.connector
from snowflake.connector.pandas_tools import write_pandas
from dotenv import load_dotenv


# ==========================================
# GEOPULSE - SNOWFLAKE DATA LOADING
# ==========================================

# Load environment configuration
load_dotenv()

# Project directory
PROJECT_DIR = Path(__file__).resolve().parents[2]

# Dataset paths
GPS_FILE = PROJECT_DIR / "data" / "processed" / "cleaned_gps_mobility.csv"
STORES_FILE = PROJECT_DIR / "data" / "raw" / "stores.csv"


# ==========================================
# 1. CONNECT TO SNOWFLAKE
# ==========================================

def connect_to_snowflake():

    print("\nConnecting to Snowflake...")

    connection = snowflake.connector.connect(
        account=os.getenv("SNOWFLAKE_ACCOUNT"),
        user=os.getenv("SNOWFLAKE_USER"),
        authenticator="OAUTH_AUTHORIZATION_CODE",
        warehouse=os.getenv("SNOWFLAKE_WAREHOUSE"),
        database=os.getenv("SNOWFLAKE_DATABASE"),
        schema=os.getenv("SNOWFLAKE_SCHEMA"),
        role=os.getenv("SNOWFLAKE_ROLE")
    )

    print("Snowflake connection successful!")

    return connection


# ==========================================
# 2. LOAD DATASETS
# ==========================================

def load_datasets():

    connection = None
    cursor = None

    try:

        # ----------------------------------
        # Read datasets
        # ----------------------------------

        print("\nReading project datasets...")

        if not GPS_FILE.exists():
            raise FileNotFoundError(f"GPS dataset not found: {GPS_FILE}")

        if not STORES_FILE.exists():
            raise FileNotFoundError(f"Stores dataset not found: {STORES_FILE}")

        gps_df = pd.read_csv(GPS_FILE)

        stores_df = pd.read_csv(STORES_FILE)

        gps_df["timestamp"] = pd.to_datetime(
            gps_df["timestamp"],
            errors="raise"
        )

        print("GPS records:", len(gps_df))
        print("Retail stores:", len(stores_df))

        # ----------------------------------
        # Connect to Snowflake
        # ----------------------------------

        connection = connect_to_snowflake()

        cursor = connection.cursor()

        # ----------------------------------
        # Clear existing table records
        # ----------------------------------

        print("\nPreparing Snowflake tables...")

        cursor.execute(
            "TRUNCATE TABLE GEOPULSE_DB.RETAIL_ANALYTICS.GPS_MOBILITY"
        )

        cursor.execute(
            "TRUNCATE TABLE GEOPULSE_DB.RETAIL_ANALYTICS.RETAIL_STORES"
        )

        print("Existing table records cleared.")

        # ----------------------------------
        # Upload GPS mobility dataset
        # ----------------------------------

        print("\nUploading GPS mobility data...")

        gps_result = write_pandas(
            conn=connection,
            df=gps_df,
            table_name="GPS_MOBILITY",
            database="GEOPULSE_DB",
            schema="RETAIL_ANALYTICS",
            chunk_size=5000,
            parallel=1,
            compression="snappy",
            auto_create_table=False,
            overwrite=False,
            quote_identifiers=False
        )

        gps_success, gps_chunks, gps_rows, gps_output = gps_result

        print("\nGPS upload successful:", gps_success)
        print("GPS chunks uploaded:", gps_chunks)
        print("GPS rows uploaded:", gps_rows)

        if not gps_success:
            raise RuntimeError("GPS dataset upload failed.")

        # ----------------------------------
        # Upload retail stores dataset
        # ----------------------------------

        print("\nUploading retail stores data...")

        stores_result = write_pandas(
            conn=connection,
            df=stores_df,
            table_name="RETAIL_STORES",
            database="GEOPULSE_DB",
            schema="RETAIL_ANALYTICS",
            chunk_size=5000,
            parallel=1,
            compression="snappy",
            auto_create_table=False,
            overwrite=False,
            quote_identifiers=False
        )

        stores_success, stores_chunks, stores_rows, stores_output = stores_result

        print("\nStores upload successful:", stores_success)
        print("Store chunks uploaded:", stores_chunks)
        print("Store rows uploaded:", stores_rows)

        if not stores_success:
            raise RuntimeError("Retail stores dataset upload failed.")

        # ----------------------------------
        # Verify uploaded records
        # ----------------------------------

        print("\nVerifying Snowflake records...")

        cursor.execute(
            "SELECT COUNT(*) FROM GEOPULSE_DB.RETAIL_ANALYTICS.GPS_MOBILITY"
        )

        gps_count = cursor.fetchone()[0]

        cursor.execute(
            "SELECT COUNT(*) FROM GEOPULSE_DB.RETAIL_ANALYTICS.RETAIL_STORES"
        )

        stores_count = cursor.fetchone()[0]

        # ----------------------------------
        # Final report
        # ----------------------------------

        print("\n========== FINAL REPORT ==========")

        print("Expected GPS records:", len(gps_df))
        print("GPS records in Snowflake:", gps_count)

        print("Expected retail stores:", len(stores_df))
        print("Retail stores in Snowflake:", stores_count)

        if gps_count != len(gps_df):
            raise RuntimeError("GPS record count does not match.")

        if stores_count != len(stores_df):
            raise RuntimeError("Store record count does not match.")

        print("\nGeoPulse data loading completed successfully!")

    except Exception as error:

        print("\nData loading failed!")
        print("Error:", error)

        raise

    finally:

        if cursor is not None:
            cursor.close()

        if connection is not None:
            connection.close()
            print("\nSnowflake connection closed.")


# ==========================================
# 3. MAIN PROGRAM
# ==========================================

if __name__ == "__main__":

    print("====================================")
    print("GEOPULSE DATA LOADING STARTED")
    print("====================================")

    load_datasets()