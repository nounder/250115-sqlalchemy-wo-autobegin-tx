Disable SQLAlchemy autobegin function that wraps each operation in transaction.

This enables to operate on Postgres DDL, like creating table indexes.

See `main.py` for source code.

Run `docker compose up` for reproducible example.
Add `--watch` for automatic restart on source change.
Run `docker compose logs app` to narrow down to python logs.

