Disable SQLAlchemy autobegin function that wraps each operation in transaction.

This enables to operate on Postgres DDL, like creating table indexes.

See `main.py` for source code.

Run `docker compose up` for reproducible example.
Add `--watch` for automatic restart on source change.
Run `docker compose logs app` to narrow down to python logs.

The sauce is `isolation_level="AUTOCOMMIT"`. It tell underlying Postgres library to
commit on each statement. SQLAlchemy knows it so it doesn't autobegin transactions.
See more in [SQLALchemy docs][0]. Note that solution will not work if you want to create mutliple
indexes in one transaction. If you wanna do it your best bet is to use DBAPI directly.

[0]: https://docs.sqlalchemy.org/en/20/core/connections.html#setting-transaction-isolation-levels-including-dbapi-autocommit

