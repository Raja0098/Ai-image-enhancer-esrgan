import torch
import cv2
import numpy as np
from torchvision.transforms import ToTensor
from basicsr.archs.rrdbnet_arch import RRDBNet

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

def load_esrgan_model(model_path='models/esrgan_finetuned.pth'):
    model = RRDBNet(num_in_ch=3, num_out_ch=3, num_feat=64, num_block=23, num_grow_ch=32)
    state_dict = torch.load(model_path, map_location=device)
    if 'params_ema' in state_dict:
        state_dict = state_dict['params_ema']
    model.load_state_dict(state_dict, strict=True)
    model.eval()
    model.to(device)
    return model

def enhance_image(model, img_np: np.ndarray) -> np.ndarray:
    img_np = (img_np / 255.0).astype(np.float32)
    img_tensor = ToTensor()(img_np).unsqueeze(0).to(device)
    with torch.no_grad():
        sr = model(img_tensor).clamp(0, 1)
    sr_img = sr.squeeze().permute(1, 2, 0).cpu().numpy()
    return (sr_img * 255).astype(np.uint8)
