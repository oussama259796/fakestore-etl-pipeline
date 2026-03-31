# FakeStore ETL Pipeline 🚀

**Automated ETL: FakeStore API → PostgreSQL**

## Tech Stack:
Python | Requests | psycopg2 | PostgreSQL | Logging

## Pipeline Steps:
- **Extract:** Fetch products from FakeStore API
- **Transform:** Validate + clean + format data
- **Load:** Insert to PostgreSQL (no duplicates)

## Features:
- ✅ Full error handling
- ✅ Data validation
- ✅ Duplicate prevention (ON CONFLICT)
- ✅ Automated logging to stor.log
- ✅ Secure password via ENV variable

## Run:
```bash
pip install requests psycopg2-binary
python etl_pipeline.py
```

**Result:** 20 clean products loaded in seconds!

---
Portfolio by Oussama | Data Engineer
