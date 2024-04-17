import sys
from pathlib import Path

sys.path.append([str(x) for x in Path(__file__).parents if x.name == "stc_project"].pop())

from app.extesions.repository.FluentValidation.src.FluentValidation.abstract_validator import AbstractValidator  # noqa: E402, F401
from app.extesions.repository.interfaces import IRepositoryBase  # noqa: E402, F401
from app.extesions.repository.model_base import ModelBase  # noqa: E402, F401
from app.extesions.repository.table.table import Table  # noqa: E402, F401
from app.extesions.repository.table.column_info import ColumnInfo  # noqa: E402, F401
from app.extesions.repository.model_base import MySQLRepository  # noqa: E402

db = MySQLRepository(user="root", password="1234", database="db").connect()
