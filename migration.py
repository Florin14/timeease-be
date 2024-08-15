# Id: run_migration.py 202206 23/06/2022
#
# backend
# Copyright (c) 2011-2013 IntegraSoft S.R.L. All rights reserved.
#
# Author: cicada
#   Rev: 202206
#   Date: 23/06/2022
#
# License description...
import os
from argparse import Namespace

from alembic import command
from alembic.config import Config
from sqlalchemy import text

from src.extensions.sqlalchemy import SqlBaseModel, SessionLocal
from src.project_helpers import postgres

# from extensions.sqlalchemy import SessionLocal
# from modules import *

target_metadata = SqlBaseModel.metadata
# make_searchable(metadata=SqlBaseModel.metadata, options={"regconfig": "pg_catalog.simple"})
alembicConfig = Config(
    "migrations/alembic.ini",
    cmd_opts=Namespace(autogenerate=True, ignore_unknown_revisions=True, x=None),
)
session = SessionLocal()
session.execute(text("DROP TABLE IF EXISTS alembic_version;"))
session.commit()
alembicConfig.set_main_option("sqlalchemy.url", postgres.uri())
alembicConfig.set_main_option("script_location", "migrations")
isExist = os.path.exists("migrations/versions")


if not isExist:
    os.makedirs("migrations/versions")
command.stamp(alembicConfig, revision="head")
command.revision(alembicConfig, autogenerate=True)
command.upgrade(alembicConfig, revision="head")
command.stamp(alembicConfig, revision="head")

session.close()

exit(0)
