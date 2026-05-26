# Calculator API

This repository provides a FastAPI service with a single endpoint that evaluates arithmetic expressions.

## Endpoint

- **POST** `/api/calculator`
  - **Request JSON**: `{ "expression": "2+3*4" }`
  - **Success Response**: `{ "result": 14 }`
  - **Error Response**: HTTP 400 with a JSON error message.
  - **Rate‑limit Header**: `X-RateLimit-Limit` and `X-RateLimit-Remaining` are added to the response.

## Running

```bash
uvicorn src.main:app --reload
```

## Tests

You can test the endpoint with `curl`:

```bash
curl -X POST http://localhost:8000/api/calculator \
     -H "Content-Type: application/json" \
     -d '{"{\"expression\": \"2+3*4\"}}'"
```
