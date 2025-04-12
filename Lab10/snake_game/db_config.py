import psycopg2
from psycopg2 import Error
from configparser import ConfigParser

def config(filename='database.ini', section='postgresql'):
    """Load connection parameters from an INI file"""
    parser = ConfigParser()
    parser.read(filename)
    
    db_params = {}
    if parser.has_section(section):
        for param in parser.items(section):
            db_params[param[0]] = param[1]
    else:
        raise Exception(f'Section {section} not found in {filename}')
    
    return db_params

def connect():
    """Connect to the PostgreSQL database"""
    conn = None
    try:
        # Read connection parameters
        params = config()
        
        # Connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        
        return conn
    except (Exception, Error) as error:
        print(f"Error connecting to PostgreSQL: {error}")
        return None 