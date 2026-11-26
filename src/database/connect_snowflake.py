import os
import snowflake.connector
from dotenv import load_dotenv

# Load credentials and configuration
load_dotenv()

connection = None

try:
    print("Connecting to Snowflake...")

    # Establish Snowflake connection
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

    # Execute a test query
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            CURRENT_USER(),
            CURRENT_DATABASE(),
            CURRENT_SCHEMA(),
            CURRENT_WAREHOUSE()
    """)

    result = cursor.fetchone()

    print("\nConnection Details")
    print("------------------")
    print("User:", result[0])
    print("Database:", result[1])
    print("Schema:", result[2])
    print("Warehouse:", result[3])

    cursor.close()

except Exception as error:
    print("Snowflake connection failed!")
    print("Error:", error)

finally:
    if connection is not None:
        connection.close()
        print("\nSnowflake connection closed.")