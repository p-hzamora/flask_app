from app.extesions import AbstractValidator
from app.extesions import IRepositoryBase
from app.extesions import ModelBase
from app.extesions import Table
from app.extesions import Column


class Post(Table):
    __table_name__ = "posts"

    def __init__(
        self,
        id,
        title,
        content,
    ) -> None:
        self._id = ColumnInfo("id", id, is_primary_key=True)
        self._title = ColumnInfo("title", title)
        self._content = ColumnInfo("content", content)

    @property
    def id(self) -> int:
        return self._id.column_value

    @id.setter
    def id(self, value: int) -> None:
        self._id.column_value = value

    @property
    def title(self) -> str:
        return self._title.column_value

    @title.setter
    def title(self, value: str) -> None:
        self._title.column_value = value

    @property
    def content(self) -> str:
        return self._content.column_value

    @content.setter
    def content(self, value: str) -> None:
        self._content.column_value = value


class PostModel(ModelBase[Post]):
    def __init__(self, repository: IRepositoryBase):
        super().__init__(Post, repository=repository)


class PostModelValidation(AbstractValidator[Post]):
    def __init__(self) -> None:
        super().__init__()
        self.rule_for(lambda x: x.id).not_null().must(lambda x: isinstance(x, int))
        self.rule_for(lambda x: x.title).must(lambda x: isinstance(x, str)).max_length(150)
        self.rule_for(lambda x: x.content).must(lambda x: isinstance(x, str))


# db.Integer
# db.String(150)
# db.Text
