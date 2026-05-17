import logging
from src.extract import fetch_stor_data
from src.transform import tranform_data_stor
from src.load import get_engine, load_data_stor


def main():
   try:
       db_engine = get_engine()

       raw_data = fetch_stor_data()
       if raw_data:
           df = tranform_data_stor(raw_data)
           if not df.empty:
               load_data_stor(df , db_engine)
               logging.info("Done! Check your CSV and Log files.")
           else:
                logging.warning("Transform stage resulted in an empty DataFrame.")
       else:
            logging.error("No data fetched from the source (Raw data is empty).")
   except Exception as e:
        logging.error(f"ETL Pipeline failed during execution: {e}")
    


if __name__ == "__main__":
    main()
