export PYTHONPATH=${PWD}/server
uvicorn main:app --reload --port 8000