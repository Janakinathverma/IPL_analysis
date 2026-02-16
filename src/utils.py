import sqlite3
import pandas as pd

def create_connection(db_path="ipl.db"):
    """Create SQLite connection"""
    conn = sqlite3.connect(db_path)
    return conn


def load_csv_to_sqlite(csv_path, conn, table_name="ipl"):
    """Load CSV data into SQLite database"""
    df = pd.read_csv(csv_path, low_memory=False)
    df.to_sql(table_name, conn, if_exists="replace", index=False)
    return df


def run_query(conn, query):
    """Run SQL query and return result as DataFrame"""
    return pd.read_sql_query(query, conn)


def print_section(title):
    """
    Print formatted section heading
    """
    print("\n" + "=" * 50)
    print(title.upper())
    print("=" * 50)


def percentage_format(value):
    """
    Format float as percentage string
    """
    return f"{value:.2f}%"

