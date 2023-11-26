# Import necessary module
from sqlalchemy import create_engine
from sqlalchemy import MetaData

# Create engine: engine
engine = create_engine('sqlite:///site.db')

metadata = MetaData()
metadata.reflect(bind=engine)

table_names = [table.name for table in metadata.tables.values()]

print(table_names)