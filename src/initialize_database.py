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
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE users (
            id INTEGER PRIMARY KEY,
            username VARCHAR(255) NOT NULL,
            password VARCHAR(255) NOT NULL
        );  
    """)
    connection.commit()

    cursor.execute("""
        CREATE TABLE budgets (
            id INTEGER PRIMARY KEY,
            user_id INTEGER NOT NULL,
            name VARCHAR(255) NOT NULL,
            amount DECIMAL(10, 2) NOT NULL,
            beginning_date DATE,
            ending_date DATE,
            current_date DATE,
            FOREIGN KEY (user_id) REFERENCES users(id)
        );
    """)
    connection.commit()


'''self, name, user, amount, beginning_date, ending_date, current_date'''


def initialize_database():
    """Alustaa tietokantataulut."""

    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)


if __name__ == "__main__":
    initialize_database()
