import databases
import sqlalchemy
from pydantic import BaseModel, Field
from sqlalchemy import create_engine

DATABASE_URL = 'sqlite:///lesson6_task2/db2.db'
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
db2 = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("user_id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("username", sqlalchemy.String(50)),
    sqlalchemy.Column("email", sqlalchemy.String(50)),
    sqlalchemy.Column("birthday", sqlalchemy.String(10)),
    sqlalchemy.Column("password", sqlalchemy.String(128)),
    sqlalchemy.Column("address", sqlalchemy.String(128)),
)


class Users(BaseModel):
    user_id: int
    username: str = Field(title="Name", min_length=2, max_length=50)
    email: str = Field(title="Email", max_length=50,
                       pattern='([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    birthday: str = Field(title="Birthday", min_length=10, max_length=10,
                          pattern='(0?[1-9]|[12][0-9]|3[01])(\.)(0?[1-9]|1[012])(\.)((19|20)\d\d)')
    password: str = Field(title="Password", min_length=8,
                          max_length=128, pattern='(.*[a-z])||(.*[0-9])')
    address: str = Field(title="Address", min_length=5, max_length=128)
