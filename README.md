
# Full-Stack MedTech Mini Web-App (FastAPI + Static Frontend)

This repo contains a minimal **frontend** and a **FastAPI backend** that simulates surgical planning phases on a 2D medical image:

- **Arterial phase** → increased contrast (ImageEnhance)
- **Venous phase** → Gaussian smoothing (ImageFilter.GaussianBlur)

All processing is done on the **server**.

## Project Structure

```
backend/    # FastAPI app (Hugging Face Space or any server)
frontend/   # Static site (GitHub Pages or any static host)
```

## Local Development

### Backend
```
cd backend
pip install -r requirements.txt
uvicorn main:app --reload --host 0.0.0.0 --port 7860
```
The API exposes:
- `GET /health`
- `POST /process` (multipart: `file`, `phase` = `arterial|venous`) → PNG image

### Frontend
Serve `frontend/` as a static site.
- For quick local testing, open `frontend/index.html` directly.
  
- Edit `frontend/config.js` and set `BACKEND_URL` to your backend URL.

