# CSV to SQLite ETL Pipeline

## Project Overview

This project demonstrates a simple end-to-end ETL (Extract, Transform, Load) pipeline build using Python, Pandas, and SQLite.

The pipeline:

* Extracts e-commerce order data from a CSV file
* Cleans and transforms the data using pandas
* Loads the transformed data into a SQLite database
* Implements logging and error handling
* Structuring a scalable ETL pipeline

---

## Project Structure

```text
csv-to-sqlite-etl-pipeline/
│
├── data/                          # Input CSV files
│   └── E-commerce_Orders.csv
│
├── logs/                          # Log files
│   └── etl.log
│
├── output/                        # SQLite database output
│   └── orders.db
│
├── venv/                          # Virtual environment
│
├── analysis.py                   # Analysing the data
├── etl.py                        # Main ETL pipeline 
├── transformation.py            # Data Transformation logic
├── requirements.txt             # Project dependencies
├── README.md                    # Project documentation
└── .gitignore
```

## Technologies Used

* Python
* Pandas
* SQLAlchemy
* SQLite
* Logging module

---

## ETL Pipeline Steps

### Extract

* Reads CSV data using Pandas
* Validate data loading
* Logs extraction details

### Transform

* Removes duplicate records
* Converts date types:
    * `OrderDate` -> datetime
    * `TotalAmount` -> float
* Converts numeric columns
* Creates additional columns:

  * OrderMonth
  * OrderYear

### Load

* Loads transformed data into SQLite
* Creates table: `orders` 
* Adds indexes:
    * `orderid`
    * `customerid`
* Logs successful load operation

## Dataset Analysis

The `analysis.py` script performs:

* Null value checks
* Duplicate checks
* OrderID uniqueness validation
* Future date validation
* Negative amount validation
* Statistical analysis

---

## Setup Instructions

### 1. Clone Repository

```bash
git clone <repository-url>
cd csv-to-sqlite-etl-pipeline
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Virtual Environment

#### Windows PowerShell

```bash
.\venv\Scripts\Activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run the ETL Pipeline

```bash
python etl.py
```

---

## Run Data Analysis

```bash
python analysis.py
```

---

## Output

### SQLite Database

Generated at:

```text
output/orders.db
```

### Logs

Generated at:

```text
logs/etl.log
```

---

## Future Improvements

* Add unit tests
* Handle Incremental data loads
* Add Airflow orchestration
* Add Docker support

* Add automated scheduling
* Add data validation framework

---

#### Author

#### Purnima Singh
# csv-to-sqlite-etl-pipeline
###### Practice Project for DE

