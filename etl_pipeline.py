import os
import requests
import psycopg2
import logging

logging.basicConfig(
                    level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s",
                    filename= "stor.log"
)
url ='https://fakestoreapi.com/products'

# -------------------------
# Extract
# -------------------------

def fetch_data():
    try:
        response = requests.get(url , timeout=10)
        response.raise_for_status()
        data = response.json()
        logging.info("Data fetched successfully")
        return data
    except requests.RequestException as e:
        logging.error(f"Error fetching data: {e}")
        return []

# -------------------------
# Transform 
# -------------------------
def transform_data(data):
    transfrmd = []
    for row in data:
        if validate_data(row):
            transfrmd.append({
                "id": row["id"],
                "title": row["title"].strip().title(),
                "price": float(row["price"]),
                "category": row["category"].strip().title(),
                "rate": row["rating"]["rate"],
                "cnt": row["rating"]["count"]
            })
    logging.info(f"{len(transfrmd)} records transformed")
    return transfrmd


def validate_data(row):
    if row.get("id") is None: 
        return False
    if row.get("price", 0) < 0:
        return False
    return True

# -------------------------
# Load  
# -------------------------
def load_to_postgres(transfrmd):
    try:
        conn = psycopg2.connect(
            host=os.getenv("PG_HOST", "localhost"),
            port=os.getenv("PG_PORT", "5432"),
            dbname=os.getenv("PG_DBNAME", "postgres"),
            user=os.getenv("PG_USER", "postgres"),
            password=os.getenv("PGPASSWORD")
        )
        cur = conn.cursor()
        sql = """INSERT INTO products (id, title, price, category, rate, cnt) 
                 VALUES (%s, %s, %s, %s, %s, %s) 
                 ON CONFLICT (id) DO NOTHING;"""
        for item in transfrmd:
            cur.execute(sql, (
                item["id"],
                item["title"],
                item["price"],
                item["category"],
                item["rate"],
                item["cnt"]
            ))
        conn.commit()
        cur.close()
        conn.close()
        logging.info("Data loaded to PostgreSQL successfully")
    except psycopg2.Error as e:
        logging.error(f"Error loading data to PostgreSQL: {e}")

def run_etl():
    data = fetch_data()
    transfrmd = transform_data(data)
    
    if transfrmd:
        load_to_postgres(transfrmd)
    else:
        logging.warning("no valid data ")
if __name__ == "__main__":
    run_etl()
