import pandas as pd
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()
# Paramètres de connexion
rds_endpoint = os.getenv("RDS_ENDPOINT")
db_username = os.getenv("DB_USERNAME")
db_password = os.getenv("DB_PASSWORD")
db_name = os.getenv("DB_NAME")

def main():
    query = "SELECT * FROM job_listings;"

    connection_url = f'postgresql+psycopg2://{db_username}:{db_password}@{rds_endpoint}/{db_name}'
    engine = create_engine(connection_url)
    df = pd.read_sql(query, engine)
    return df

if __name__ == "__main__":
    main()