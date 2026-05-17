# FakeStore Dockerized ETL Pipeline 🚀

**Automated ETL: FakeStore API → Pandas → PostgreSQL (Docker)**

## Tech Stack:
Python | Pandas | SQLAlchemy | PostgreSQL | Docker | Dotenv (`.env`) | UV ⚡

## Pipeline Steps:
- **Step 0 (Bridge Check):** The code checks the database connection in Docker first. If it's down, it stops immediately to save server resources (Fail-Fast).
- **Extract:** Fetch products from FakeStore API.
- **Transform:** Use Pandas to clean and flatten nested JSON (separating rating into `rate` and `cnt`).
- **Load:** Insert clean data to PostgreSQL inside Docker (no fake dummy data added during local tests).

## Features:
- ✅ Fully Containerized via Docker
- ✅ High Data Cleanliness & Validation
- ✅ Zero Hardcoded Credentials (via `.env`)
- ✅ Automated logging to `etl_pipeline.log` and `load_product.log`
- ✅ Powered by **UV** for lightning-fast dependency management

## Run:
```bash
# 1. Start the database container
docker-compose up -d

# 2. Run the pipeline instantly with UV
uv run main.py