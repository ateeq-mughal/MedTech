
# Backend (FastAPI)

Local dev:

```bash
pip install -r requirements.txt
uvicorn main:app --reload --host 0.0.0.0 --port 7860
```

Endpoints:
- `GET /` → `{"message": "server is running."}`
- `POST /process` (multipart form): fields
  - `file`: image (JPG/PNG)
  - `phase`: `"arterial"` or `"venous"`
Returns a PNG image binary.
