#!/usr/bin/env python

import sqlalchemy

# Database = tennis; User = federer; Password = grandestslam
# Postgres installed on Vagrant box, w/ PSQL port 5432 forwarded -> local 5432
# Script will probably need to be written as if it's connecting to a local
#   PSQL instance, but the DB configured for remote connections


def connect(user, password, db, host="localhost", port=5432):
    '''
    Returns a connection and metadata object
    '''
    # Connect w/ the help of the PostgreSQL URL
    # postgresql://federer:grandestslam@localhost:5432/tennis
    url = "postgresql://{}:{}@{}:{}/{}"
    url = url.format(user, password, host, port, db)

    # The return value of the create_enginer() is our connection object
    con = sqlalchemy.create_engine(url, client_encoding="utf8")

    # We then bind the connection to MetaData()
    meta = sqlalchemy.MetaData(bind=con, reflect=True)

    return con, meta

con, meta = connect("federer", "grandestslam", "tennis")

print con
print meta
