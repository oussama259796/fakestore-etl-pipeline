import pandas as pd
import logging
import json

logging.basicConfig(
                    level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s",
                    filename= "stor.log"
                )               


def validate_data(row):
    if row.get("id") is None: 
        return False
    if row.get("price", 0) < 0:
        return False
    return True


def tranform_data_stor(raw_data):
    try:
        if isinstance(raw_data, str):
            data_stor = json.loads(raw_data)
        elif isinstance(raw_data, (list, dict)):
            data_stor = raw_data
        else:
            logging.error("Data type error")

        Product_List = []

        products = data_stor if isinstance(data_stor, list) else[data_stor]

        for item in products:
                
            if not isinstance(item, dict):
                continue
            
            if validate_data(item):

                info_item={ "id":item.get("id"),
                            "title": item.get("title", "Unknown").strip().title(),
                            "price": float(item.get("price")),
                            "category": item.get("category", "Uncategorized").strip().title(),
                            "rate": item.get("rating", {}).get("rate"),
                            "cnt": item.get("rating", {}).get("count")
                }
                Product_List.append(info_item)
        logging.info(f"{len(Product_List)} records transformed")        
        df = pd.DataFrame(Product_List)
        return df
    except Exception as e:
        logging.error(f"Error transformed data: {e}")

if __name__ == "__main__":
    validate_data()
    tranform_data_stor()