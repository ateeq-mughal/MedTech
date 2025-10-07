import io

from fastapi import FastAPI, File, Form, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, Response
from PIL import Image, ImageEnhance, ImageFilter

# FastAPI app initialization
app = FastAPI(title="MedTech Mini Web-App Backend", version="1.0.0")

# CORS: allowing any origin by default;
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    """Root endpoint to check if the server is running."""
    return JSONResponse(content={"message": "Server is running."})


def simulate_arterial(img: Image.Image) -> Image.Image:
    
    """Increase contrast to simulate arterial phase."""
    # Convert to RGB if needed
    if img.mode != "RGB":
        img = img.convert("RGB")
    contrast = ImageEnhance.Contrast(img)
    # Increasing contrast; tweak as needed
    img = contrast.enhance(1.8)

    # returning image (arterial phase)
    return img


def simulate_venous(img: Image.Image) -> Image.Image:

    """Applying gaussian smoothing to simulate venous phase."""
    if img.mode != "RGB":
        img = img.convert("RGB")
    # returning blurred image (venous phase)
    return img.filter(ImageFilter.GaussianBlur(radius=3.0))  # radius can be adjusted (more -> stronger blur)


@app.post("/process")
async def process_image(file: UploadFile = File(...), phase: str = Form(...)):

    """Accepts an image and a phase ('arterial' or 'venous'), returns processed image bytes (PNG)."""
    phase = phase.lower().strip()
    if phase not in ["arterial", "venous"]:
        raise HTTPException(
            status_code=400,
            detail="Invalid phase. Phase must be 'arterial' or 'venous'.",
        )
    try:
        raw = await file.read()
        img = Image.open(io.BytesIO(raw))
    except Exception:
        raise HTTPException(
            status_code=400, detail="Invalid image. Please upload a valid JPG/PNG."
        )
    # Perform server-side processing
    if phase == "arterial":
        out = simulate_arterial(img)
    else:
        out = simulate_venous(img)
    buf = io.BytesIO()
    out.save(buf, format="PNG")
    buf.seek(0)
    return Response(content=buf.getvalue(), media_type="image/png")
