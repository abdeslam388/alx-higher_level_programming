#!/usr/bin/python3
"""
Script to list City objects from the database using SQLAlchemy
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from relationship_city import Base, City
from relationship_state import State
import sys

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <mysql_username> <mysql_password> <database_name>"
              .format(sys.argv[0]))
        sys.exit(1)

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Connect to the MySQL server running on localhost at port 3306
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        mysql_username, mysql_password, database_name))

    # Create a session
    session = Session(engine)

    # Retrieve all City objects and their associated State objects
    cities = session.query(City).order_by(City.id).all()

    for city in cities:
        state_name = city.state.name if city.state else "N/A"
        print("{}: {} -> {}".format(city.id, city.name, state_name))

    # Close the session
    session.close()

