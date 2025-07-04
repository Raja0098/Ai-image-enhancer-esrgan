#!/bin/bash
cd "$(dirname "$0")"
PYTHONPATH=$(pwd) uvicorn super_app.main:app --host 127.0.0.1 --port 8080 --reload

