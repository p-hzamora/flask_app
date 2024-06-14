from .orm.orm import MySQLRepository  # noqa: E402

db = MySQLRepository(user="root", password="1234", database="sakila").connect()