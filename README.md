# AI_Testing_Framework

## Restful Booker API tests (pytest + requests)

Setup

1. Create a virtualenv and install deps:

```bash
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

2. Run tests:

```bash
pytest -q
```

Environment variables
- `BOOKER_BASE_URL` - override default base URL
- `BOOKER_USER` / `BOOKER_PASS` - credentials for `/auth` (defaults: admin / password123)

Notes
- Uses cookie-based token returned from `/auth` for protected endpoints.
- Tests will perform create/delete operations on the public demo API; expect shared state.
