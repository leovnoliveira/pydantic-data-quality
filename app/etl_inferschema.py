import os
from pathlib import Path

import pandas as pd
import pandera as pa
from dotenv import load_dotenv
from app.schema import ProdutoSchema
from sqlalchemy import create_engine


def load_settings():
    """Carrega as configurações a partir de variáveis de ambiente"""

    dotenv_path = Path.cwd() / '.env'
    load_dotenv(dotenv_path=dotenv_path)

    settings = {
        "db_host": os.getenv("POSTGRES_HOST"),
        "db_port": os.getenv("POSTGRES_PORT"),
        "db_name": os.getenv("POSTGRES_DB"),
        "db_user": os.getenv("POSTGRES_USER"),
        "db_password": os.getenv("POSTGRES_PASSWORD"),
    }

    return settings

pa.check_output(ProdutoSchema)

def extrair_do_sql(query: str) -> pd.DataFrame:
    """Extrai dados de um banco de dados SQL e retorna um DataFrame do pandas"""

    settings = load_settings()
    engine = create_engine(
        f"postgresql+psycopg2://{settings['db_user']}:{settings['db_password']}@{settings['db_host']}:{settings['db_port']}/{settings['db_name']}"
    )

    with engine.connect() as connection, connection.begin():
        df = pd.read_sql_query(query, connection)

    return df


if __name__ == "__main__":
    query = "SELECT * FROM produtos_bronze"
    # df_crm = extrair_do_sql(query)
    # schema_crm = pa.infer_schema(df_crm)
    # print(schema_crm)

    # with open("schema_crm.py", "w", encoding="utf-8") as f:
    #     f.write(schema_crm.to_script())