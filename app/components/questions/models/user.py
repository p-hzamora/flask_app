from app.extesions import AbstractValidator
from app.extesions import db


class Client(db.Table):
    __table_name__ = "client"

    def __init__(
        self,
        id,
        name,
        password,
    ) -> None:
        self._id = db.Column(db.nameof(id), id, is_primary_key=True)
        self._name = db.Column(db.nameof(name), name)
        self._password = db.Column(db.nameof(password), password)

    @property
    def id(self) -> type:
        return self._id.column_value

    @id.setter
    def id(self, value) -> type:
        self._id.column_value = value

    @property
    def name(self) -> type:
        return self._name.column_value

    @name.setter
    def name(self, value) -> type:
        self._name.column_value = value

    @property
    def password(self) -> type:
        return self._password.column_value

    @password.setter
    def password(self, value) -> type:
        self._password.column_value = value


class ClientModel(db.ModelBase[Client]):
    def __init__(self, repository: db.IRepositoryBase):
        super().__init__(Client, repository=repository)


class ClientValidation(AbstractValidator[Client]):
    def __init__(self) -> None:
        super().__init__()
        self.rule_for(lambda x: x.id).not_null().must(lambda x: isinstance(x, int))
        self.rule_for(lambda x: x.name).must(lambda x: isinstance(x, str))
        self.rule_for(lambda x: x.password).must(lambda x: isinstance(x, str))
