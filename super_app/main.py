from fastapi import FastAPI, UploadFile, File, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uuid
from super_app.model import load_esrgan_model, enhance_image
from super_app.utils import read_uploadfile_as_np
from PIL import Image
import os

app = FastAPI(title="ESRGAN Super Resolution API")
model = load_esrgan_model()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))

# Mount static files correctly
app.mount("/static", StaticFiles(directory=os.path.join(BASE_DIR, "static")), name="static")


@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


# @app.post("/upload/", response_class=HTMLResponse)
# async def upload_image(request: Request, file: UploadFile = File(...)):
#     input_img = read_uploadfile_as_np(file)
#     output_img = enhance_image(model, input_img)

#     filename = f"{uuid.uuid4().hex}.png"
#     out_path = os.path.join(BASE_DIR, "static", filename)
#     Image.fromarray(output_img).save(out_path)

#     return templates.TemplateResponse("index.html", {
#         "request": request,
#         "image_url": f"/static/{filename}"
#     })
    
@app.post("/upload/", response_class=HTMLResponse)
async def upload_image(request: Request, file: UploadFile = File(...)):
    input_img = read_uploadfile_as_np(file)
    print(f"Original image shape: {input_img.shape}")  # Log original size

    output_img = enhance_image(model, input_img)
    print(f"Enhanced image shape: {output_img.shape}")  # Log enhanced size

    filename = f"{uuid.uuid4().hex}.png"
    out_path = os.path.join(BASE_DIR, "static", filename)
    Image.fromarray(output_img).save(out_path)

    return templates.TemplateResponse("index.html", {
        "request": request,
        "image_url": f"/static/{filename}"
    })

