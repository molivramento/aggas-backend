import ormar
import databases
import sqlalchemy

database = databases.Database('sqlite:///db.sqlite')
metadata = sqlalchemy.MetaData()


class BaseMeta(ormar.ModelMeta):
    database = database
    metadata = metadata
