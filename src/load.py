import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
import logging
load_dotenv()

logging.basicConfig(
                    level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s",
                    filename= "load_product.log",
                    encoding="utf-8"
                )       
engine = create_engine(os.getenv("DATABASE_URL"))

def get_engine():
    try:
        with engine.connect():
            logging.info("تم الاتصال بـ PostgreSQL بنجاح")
        return engine
    except Exception as e:
        logging.error(f"فشل الاتصال: {e}")
        raise


def load_data_stor(df, db_engine):
    try:
        df.to_sql(
                "products",
                db_engine,
                if_exists="append",
                index=False
            )
        logging.info(f"successful loading process: {len(df)} row")
    except Exception as e:
        logging.error(f"Loading failed due to: {e}")
        raise


if __name__ == "__main__":
    get_engine()
    load_data_stor()