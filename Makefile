start-model-server:
	uvicorn api.src.main:app --reload