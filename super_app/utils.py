from fastapi import UploadFile
from PIL import Image
import numpy as np
import io

def read_uploadfile_as_np(file: UploadFile) -> np.ndarray:
    image = Image.open(io.BytesIO(file.file.read())).convert("RGB")
    return np.array(image)

def to_image_response(np_img: np.ndarray):
    image = Image.fromarray(np_img)
    buf = io.BytesIO()
    image.save(buf, format="PNG")
    buf.seek(0)
    return buf
