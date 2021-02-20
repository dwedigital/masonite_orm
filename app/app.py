from models.User import User
from config.database import DB
from masoniteorm.query import QueryBuilder

print("APP")
builder = QueryBuilder().table("users")