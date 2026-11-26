# GeoPulse: Hyper-Local Retail Mobility Analytics

## Project Overview
GeoPulse is a data analytics project designed to analyze hyper-local retail mobility patterns using anonymized and synthetic GPS movement data.

The project aims to understand customer movement, estimate store footfall, identify retail catchment areas, and generate insights that support better retail location and business decisions.

## Objectives
- Generate and analyze synthetic GPS mobility data.
- Clean, preprocess, and validate location records.
- Analyze spatial movement patterns and retail catchment areas.
- Estimate hourly footfall around retail locations.
- Identify store cannibalization opportunities and risks.
- Build interactive dashboards and visualizations.
- Automate data processing and reporting workflows.

## Planned Technologies
- Python
- Pandas and PySpark
- Apache Sedona
- Snowflake
- dbt
- React
- Kepler.gl
- Apache Airflow

*Technology integration will be implemented and validated during project development.*

## Project Structure
```text
GeoPulse-Retail-Mobility-Analytics/
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
├── src/
│   ├── data_generation/
│   ├── preprocessing/
│   └── spatial_analysis/
├── snowflake/
│   └── sql/
├── dbt_project/
├── dashboard/
│   ├── frontend/
│   └── components/
├── airflow/
│   └── dags/
├── reports/
└── documentation/
```

## Project Deliverables
- Source code
- Cleaned and processed datasets
- Data analysis and visualizations
- Interactive dashboard
- Project documentation
- Final project report and presentation

## Data Privacy
This project uses synthetic and anonymized mobility data. It does not require tracking real individuals.

## Project Status
🚧 Initial setup and development in progress.
## Development Progress

## Development Progress

### Day 1 – Synthetic GPS Data Generation ✅

**Completed:**
- Created a Python-based GPS data generator.
- Generated 1,000 synthetic customers.
- Generated 20 synthetic retail stores.
- Simulated 7 days of GPS records.
- Generated 336,000 GPS records.
- Exported GPS mobility and retail store datasets into CSV format.
- Verified dataset structure and missing values.

### Day 2 – Realistic GPS Movement Simulation ✅

**Completed:**
- Improved the GPS data generator to simulate customer journeys.
- Generated customer starting locations.
- Simulated travel towards nearby retail stores.
- Added store visit and dwell periods.
- Simulated return journeys towards customer starting locations.
- Added small GPS coordinate variations.
- Verified customer movement using Pandas.

**Validation Results:**

| Validation | Result |
|---|---:|
| Total customers | 1,000 |
| Total stores | 20 |
| Total GPS records | 336,000 |
| Records per customer | 336 |
| GPS columns | 6 |
| Unique positions for sample customer | 336 |

**Technologies Used:** Python, Pandas, Random.

**Note:** All customer movement and location data are synthetically generated.
### Day 3 – GPS Data Cleaning and Validation ✅

**Completed:**
- Created a Python preprocessing script using Pandas.
- Loaded the raw GPS mobility dataset.
- Checked and handled missing values.
- Removed duplicate event IDs.
- Converted timestamps into datetime format.
- Validated latitude and longitude ranges.
- Applied a GPS accuracy threshold of 0–100 metres.
- Generated the cleaned GPS mobility dataset.
- Saved the processed dataset in `data/processed/`.

**Validation Results:**

| Validation | Result |
|---|---:|
| Original records | 336,000 |
| Cleaned records | 336,000 |
| Missing values | 0 |
| Duplicate event IDs | 0 |
| Invalid timestamps | 0 |
| Invalid coordinates | 0 |
| Records removed | 0 |

**Technologies Used:** Python, Pandas.

**Output:** `data/processed/cleaned_gps_mobility.csv`

### Overall Project Status

Development in progress.
### Overall Project Status
## Week 1 Progress

### Day 4 – Snowflake Database Setup
- Created the `GEOPULSE_DB` database and `RETAIL_ANALYTICS` schema.
- Created `GPS_MOBILITY` and `RETAIL_STORES` tables.
- Configured Python connectivity using the Snowflake Connector and browser-based OAuth.
- Created database connection and data-loading scripts.

### Day 5 – Data Loading and Verification
- Uploaded 336,000 cleaned GPS mobility records to Snowflake.
- Uploaded 20 retail store records.
- Verified both table record counts successfully.
- Used chunked data loading with `write_pandas`.

### Week 1 Summary
- Generated synthetic GPS data for 1,000 customers across 7 days.
- Simulated customer movement, store visits, dwell periods, and return journeys.
- Cleaned and validated 336,000 GPS records.
- Loaded and verified all records in Snowflake.

**Note:** All GPS movement data is synthetic and created for this project. It does not represent real customer tracking.
🚧 Development in progress.

## Author
Developed as part of the Infotact Solutions Data Analytics Internship.