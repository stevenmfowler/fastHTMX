#!/bin/bash


. venv/bin/activate
cd app
uvicorn main:app --reload
firefox '127.0.0.1:8000'
