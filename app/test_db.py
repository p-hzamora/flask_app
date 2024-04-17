import sys
from pathlib import Path

sys.path.append([str(x) for x in Path(__file__).parents if x.name == "flask_app"].pop())

from app.posts.models.post import PostModel, PostModelValidation  # noqa: E402
from app.extesions.extensions import db  # noqa: E402


model = PostModel(db).all()

for post in model:
    validate = PostModelValidation().validate(post)
    if not validate.is_valid:
        for x in validate.errors:
            print(x.ErrorMessage)
print("todo correcto")
for post in model:
    print(post)
