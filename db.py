#Import the config parser
import configparser
# Import the mysql driver
import mysql.connector


def getConfig():
    # Call the library
    config = configparser.ConfigParser()
    # Read in the config file
    config.readfp(open(r'db.conf'))

    return config

# This function will return a connect object
def connect(config):

    # Establish a connection using the driver
    connection = mysql.connector.connect(
        host = config.get('database_credentials', 'host'),
        user = config.get('database_credentials','user'),
        password = config.get('database_credentials', 'password'),
        database = config.get('database_credentials', 'database'))
    #return 
    return connection

