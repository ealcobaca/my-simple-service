from sqlmodel import create_engine

sqlite_file_name = "my-database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"
engine = create_engine(url=sqlite_url, echo=True)
