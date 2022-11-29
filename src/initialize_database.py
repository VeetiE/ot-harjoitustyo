from db_connection import get_database_connection


def drop_tables(connection):
    """Poistaa tietokantataulut.
    Args:
        connection: Tietokantayhteyden Connection-olio
    """

    cursor = connection.cursor()

    cursor.execute("""
        drop table if exists users;
    """)

    connection.commit()


def create_tables(connection):
    cursor=connection.cursor()

    cursor.execute("""
        CREATE TABLE users (
            id INTEGER PRIMARY KEY,
            username TEXT,
            password TEXT
        );  
    """)
    connection.commit()

    cursor.execute("""
        CREATE TABLE budgets (
            t_id INTEGER 
            REFERENCES reference_types,
            name TEXT,
            amount INTEGER,
            beginning_date DATE,
            ending_date DATE,
            current_date DATE
        );
    """)
    connection.commit()




def initialize_database():
    """Alustaa tietokantataulut."""

    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)


if __name__ == "__main__":
    initialize_database()
