# ✨ Enhance Your Images Instantly  
**Bring blurry or low-resolution images to life using AI Super Resolution.**  
**Upload your photo – we’ll do the magic.**

---

## 🏆 Project Title

**AI-Powered Low-Light Image Enhancer using Fine-Tuned ESRGAN & SwinIR**  
🏅 *Ranked #1 among 200+ participants – DLP Jan 2025 (NPPE3) | IIT Madras*

---

## 📌 Overview

This project is a full-stack AI-powered image enhancement application built as part of the **Deep Learning Practice (DLP) course at IIT Madras**. The goal was to denoise and upscale low-light images using cutting-edge deep learning models.

After training and fine-tuning on a Kaggle notebook, the enhanced models were integrated into a **FastAPI** backend and served through a clean and responsive **HTML/CSS UI** for real-time inference.

---
## 🚀 Features

- 🔍 **4x Super-Resolution**: Upscale blurry or pixelated images with enhanced detail.
- 🌙 **Low-Light Denoising**: Automatically reduces noise in poorly-lit photos.
- ⚙️ **Fine-Tuned Models**:
  - ✅ [Real-ESRGAN](https://github.com/xinntao/Real-ESRGAN) (for natural image restoration)
  - ✅ [SwinIR](https://github.com/JingyunLiang/SwinIR) (Transformer-based image restoration)
- 🖼️ **FastAPI App**:
  - Upload images
  - View enhanced results instantly
  - Download the enhanced image
- 💡 **Responsive UI**: Built with Jinja2, HTML5, and CSS3
- 🔐 **Offline Inference**: Fully self-contained application; no external API calls

---

## 🧠 Models and Training

The Real-ESRGAN and SwinIR models were fine-tuned using a Kaggle notebook on a dataset of low-light, noisy images. The training pipeline includes:

- Noise augmentation
- Low-light simulation
- Custom loss function (Perceptual + PSNR)
- Visual validation using SSIM metrics

> ✨ The models were exported and optimized for local inference in this application.

---

## 🛠️ Tech Stack

| Component        | Technology              |
|------------------|--------------------------|
| Backend API      | FastAPI, Uvicorn         |
| Frontend         | HTML, CSS, Jinja2        |
| Image Processing | OpenCV, Pillow, NumPy    |
| DL Models        | ESRGAN, SwinIR (PyTorch) |
| Deployment       | Localhost / Docker Ready |

---

## 📷 Usage

### 🔧 Setup

```bash
# Clone the repo
git clone https://github.com/your-username/image-enhancer-app.git
cd image-enhancer-app

# Create a virtual environment and activate
python3 -m venv venv
source venv/bin/activate

# Install requirements
pip install -r requirements.txt
# Start the FastAPI server
./run.sh
