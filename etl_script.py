import psycopg2
from datetime import datetime

# Database connection parameters
DB_PARAMS = {
    'dbname': 'your_database',
    'user': 'your_user',
    'password': 'your_password',
    'host': 'localhost',
    'port': 5432
}

def clean_tables():
    '''Clean all Fact tables before loading data'''
    queries = [
        "DELETE FROM FactOrderDetails;",
        "DELETE FROM FactClientesAtendidos;",
        "DELETE FROM FactOrders;"
    ]
    try:
        conn = psycopg2.connect(**DB_PARAMS)
        cursor = conn.cursor()
        for query in queries:
            cursor.execute(query)
        conn.commit()
        print("Tables cleaned successfully.")
    except Exception as e:
        print(f"Error cleaning tables: {e}")
    finally:
        cursor.close()
        conn.close()

def load_data():
    '''Load sample data into Fact tables'''
    try:
        conn = psycopg2.connect(**DB_PARAMS)
        cursor = conn.cursor()

        # Load data into FactOrders
        cursor.execute("""
            INSERT INTO FactOrders (OrderDate, CustomerID, TotalAmount)
            VALUES
            ('2024-11-01', 1, 150.75),
            ('2024-11-02', 2, 200.00);
        """)

        # Load data into FactClientesAtendidos
        cursor.execute("""
            INSERT INTO FactClientesAtendidos (AtencionFecha, AtencionTipo)
            VALUES
            ('2024-11-01', 'In-store'),
            ('2024-11-02', 'Online');
        """)

        # Load data into FactOrderDetails
        cursor.execute("""
            INSERT INTO FactOrderDetails (OrderID, ProductID, Quantity, UnitPrice)
            VALUES
            (1, 101, 2, 50.00),
            (1, 102, 1, 50.75),
            (2, 103, 4, 50.00);
        """)

        conn.commit()
        print("Data loaded successfully.")
    except Exception as e:
        print(f"Error loading data: {e}")
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    clean_tables()
    load_data()
