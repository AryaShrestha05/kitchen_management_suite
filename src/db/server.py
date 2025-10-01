"""
File: server.py
File-Path: src/db/server.py
Author: Thomas Bruce
Date-Created: 09-29-2025

Description:
    Postgres connection handler

Inputs:
    - .env
    - postgres connection

Outputs:
    - postgres connection
"""

import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from dotenv import load_dotenv

# load env
load_dotenv()

DB_USER = os.getenv("db_owner")
DB_PASS = os.getenv("db_pass")
DB_NAME = os.getenv("db_name")
DB_HOST = os.getenv("db_host", "localhost")
DB_PORT = os.getenv("db_port", "5432")

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# sqlalchemy
engine = create_engine(DATABASE_URL, echo=True, future=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_session():
    """Get a database session"""
    return PostgresSession()

# we can kinda just copy over the init from lab 4 for creating it, but over
# there it is specific to the tables for the lab, so i omitted it for brevity
