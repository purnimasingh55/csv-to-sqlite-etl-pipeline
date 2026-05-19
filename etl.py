import pandas as pd
import logging 
from sqlalchemy import create_engine
from sqlalchemy import text
from transformation import clean_data

# Set up logging
logging.basicConfig(
    filename = 'logs/etl.log',
    level = logging.INFO,
    format = '%(asctime)s - %(levelname)s - %(message)s'
)

# ETL Functions
def extract(file_path):
    try:
        df = pd.read_csv(file_path)
        logging.info(f"Data extracted successfully from {file_path}")
        logging.info(f"Rows in extracted data: {df.shape[0]}")
        return df
    except Exception as e:
        logging.error(f"Error in extract: {str(e)}")
        raise None

def transform(df):
    try:
        df = clean_data(df)
        logging.info("Data transformed successfully")
        logging.info(f"Rows in transformed data: {df.shape[0]}")
        return df
    except Exception as e:
        logging.error(f"Error in transform: {str(e)}")
        raise None

def load(df, db_path):
    try:
        engine = create_engine(f'sqlite:///{db_path}')
        df.to_sql('orders', engine, if_exists='replace', index=False)
        logging.info(f"Data loaded successfully into {db_path}")

        # creating indexes
        with engine.connect() as conn:
            conn.execute(text("CREATE INDEX IF NOT EXISTS idx_order_date ON orders(OrderID)"))
            conn.execute(text("CREATE INDEX IF NOT EXISTS idx_order_status ON orders(CustomerID)"))

            logging.info("Indexes created successfully")

    except Exception as e:
        logging.error(f"Error in load: {str(e)}")
        raise None

def main():
    input_file = "data/E-commerce_Orders.csv"
    db_file = "output/orders.db"
    df = extract(input_file)
    if df is not None:
        df = transform(df)
        if df is not None:
            load(df, db_file)

            logging.info("""ETL pipeline completed successfully
                        Source: {input_file}
                        Destination: {db_file}
                        Total Records Processed: {df.shape[0]}
                    """)
if __name__ == "__main__":
    main()

    


