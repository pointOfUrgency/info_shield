from sqlalchemy import MetaData, Column, String, Integer, Table, JSON, ForeignKey

meta = MetaData()

Roles = Table(
    "roles",
    meta,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("permissions", JSON),
)

Users = Table(
    "users",
    meta,
    Column("id", Integer, primary_key=True),
    Column("username", String, nullable=False),
    Column("email", String, unique=True, nullable=False),
    Column("hashed_password", String(length=100), nullable=False),
    Column("roles_id",ForeignKey(Roles.c.id)),
)