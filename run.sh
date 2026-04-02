#!/bin/bash

echo "Starting FastAPI..."
uvicorn app.main:app --reload &

echo "Starting Streamlit..."
streamlit run ui/app.py