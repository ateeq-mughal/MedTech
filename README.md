
# Full-Stack MedTech Mini Web-App (FastAPI + Static Frontend)

This repo contains a minimal **frontend** and a **FastAPI backend** that simulates surgical planning phases on a 2D medical image:

- **Arterial phase** → increased contrast (ImageEnhance)
- **Venous phase** → Gaussian smoothing (ImageFilter.GaussianBlur)

All processing is done on the **server**.

---

## Live Demo

- **Frontend (GitHub Pages):** [https://ateeq-mughal.github.io/MedTech/](https://ateeq-mughal.github.io/MedTech/)  
- **Backend (Render):** [https://medtech-z68t.onrender.com/](https://medtech-z68t.onrender.com/)

⚠️ **Note/Disclaimer:** The backend is hosted on **Render Free Tier**, which spins down when idle.  
That means the **first request may be slow (30–50s cold start)**, but subsequent requests should be faster.

---

## Project Structure

```
backend/    # FastAPI app
frontend/   # Static site
```

## Local Development

After cloning the repository from [https://github.com/ateeq-mughal/MedTech.git](https://github.com/ateeq-mughal/MedTech.git). Follow these steps:

### Backend
```
cd backend
pip install -r requirements.txt
uvicorn main:app --reload --host 0.0.0.0 --port 7860
```
The API exposes:
- `GET /` → Server Health Check
- `GET /docs` → Swagger API docs
- `POST /process` (multipart: `file`, `phase` = `arterial|venous`) → PNG image

### Frontend
Serve `frontend/` as a static site.
- For quick local testing, open `frontend/index.html` directly on your browser.
  
- Edit `frontend/config.js` and set `BACKEND_URL` to your backend URL e.g. "http://localhost:7860" for local.
