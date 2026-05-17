import logging
import json
import requests


logging.basicConfig(
                    level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s",
                    filename= "stor.log"
)
url ='https://fakestoreapi.com/products'

# -------------------------
# Extract
# -------------------------

def fetch_stor_data():
    try:
        response = requests.get(url , timeout=10)
        response.raise_for_status()
        data = response.json()
        logging.info("Data fetched successfully")
        with open("stor_data.json","w" , encoding="utf-8")as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        return data
    except requests.RequestException as e:
        logging.error(f"Error fetching data: {e}")
        

if __name__ == "__main__":
    fetch_stor_data()