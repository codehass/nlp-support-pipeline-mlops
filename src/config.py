import os

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, '../data')
RAW_DATA_PATH = os.path.join(DATA_DIR, 'raw')
PROCESSED_DATA_PATH = os.path.join(DATA_DIR, 'processed')

# Model Configs
MODEL_NAME = "bert-base-uncased"
EMBEDDING_DIM = 768

# ChromaDB Configs
CHROMA_DB_DIR = os.path.join(DATA_DIR, 'chromadb')
COLLECTION_NAME = "support_tickets"

# Monitoring Configs
EVIDENTLY_REPORT_DIR = os.path.join(BASE_DIR, '../reports')
