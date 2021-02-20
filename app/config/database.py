from masoniteorm.connections import ConnectionResolver

DATABASES = {
    "default": "sqlite",
    "sqlite": {
        "database": "masonite.db",
    }
}

DB = ConnectionResolver().set_connection_details(DATABASES)