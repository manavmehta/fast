from dotenv import dotenv_values

def get_credentials():
    config = dotenv_values(".env")
    username = config["DB_USERNAME"]
    password = config["DB_PASSWORD"]
    host = config["DB_HOST"]
    port = config["DB_PORT"]

    return username, password, host, port
