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

### Overall Project Status

Development in progress.
### Overall Project Status

🚧 Development in progress.

## Author
Developed as part of the Infotact Solutions Data Analytics Internship.