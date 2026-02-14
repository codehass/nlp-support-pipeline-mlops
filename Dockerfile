# 1. Use standard Python
FROM python:3.12-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app
ENV UV_COMPILE_BYTECODE=1
ENV UV_LINK_MODE=copy
ENV CUDA_VISIBLE_DEVICES=-1

COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev

COPY notebooks/best_email_classifier.pkl ./best_email_classifier.pkl
COPY main.py .

RUN uv run python -c "from sentence_transformers import SentenceTransformer; SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')"

CMD ["uv", "run", "python", "main.py"]