#!/usr/bin/env python

import sqlalchemy
from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey


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


slams = Table("slams", meta,
              Column("name", String, primary_key=True),
              Column("country", String)
             )

results = Table("results", meta,
                Column("slam", String, ForeignKey("slams.name")),
                Column("year", Integer),
                Column("result", String)
               )

# Create the above tables
meta.create_all(con)

# Print the tables that were just created
for table in meta.tables:
    print table
# meta.tables in an immutabledict that has mapping of table names to
# corresponding Table objects.
# Can get the sqlalchemy.schema.Table object on which can perform inserts by
# `table = meta.tables["table_name"]` for some table_name


# Insert entry
clause = slams.insert().values(name="Wimbledon", country="United Kingdom")
con.execute(clause)

# Insert entry and print primary key
clause = slams.insert().values(name="Roland Garros", country="France")
result = con.execute(clause)
print result.inserted_primary_key
