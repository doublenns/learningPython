#!/usr/bin/env python

import sqlalchemy

# Database = tennis; User = federer; Password = grandestslam
# Postgres installed on Vagrant box, w/ PSQL port 5432 forwarded -> local 5432
# Script will probably need to be written as if it's connecting to a local
#   PSQL instance, but the DB configured for remote connections
