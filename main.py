import sqlalchemy
import logging

logging.basicConfig()
logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)

engine = sqlalchemy.create_engine(
    "postgresql+psycopg://postgres:postgres@postgres/postgres", echo=True
)

with engine.connect() as conn:
    ddl_query = sqlalchemy.text("""
drop table if exists posts;

create table posts (
    id serial primary key,
    title text,
    content text
);

insert into posts (title, content) values
('Post 1', 'Content 1'),
('Post 2', 'Content 2'),
('Post 3', 'Content 3');

""")
    conn.execute(ddl_query)


# Don't use SQLAlchemy autobegin feature.
# This allows us to create indexes and do other DDL ops.
with engine.connect().execution_options(isolation_level="AUTOCOMMIT") as conn:
    conn.execute(sqlalchemy.text("SET search_path TO test_schema, public"))

    conn.execute(sqlalchemy.text("create index concurrently on posts(title)"))

