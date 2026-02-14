# NLP Support Pipeline MLOps

An end-to-end Machine Learning pipeline for automated support ticket classification. This project leverages **Sentence Transformers** for text embeddings and metadata handling to improve classification accuracy. It includes a complete MLOps workflow with monitoring, containerization, and Kubernetes deployment.

## 🚀 Features

- **Hybrid Classification Model**: Combines text embeddings (Sentence Transformers) with categorical metadata.
- **Vector Database Integration**: Uses **ChromaDB** for efficient vector storage and retrieval.
- **MLOps Pipeline**: complete training and inference pipelines.
- **Monitoring & Drift Detection**: Integrated **Evidently AI** to track data drift and model performance.
- **Containerization**: Docker support for reproducible environments.
- **Orchestration**: Kubernetes manifests for scalable deployment.

## 📂 Project Structure

```
.
├── .github/workflows/   # CI/CD configurations
├── k8s/                 # Kubernetes manifests
├── notebooks/           # Jupyter notebooks for EDA and experiments
├── src/                 # Source code
│   ├── data/            # Data loading & processing scripts
│   ├── models/          # Model definitions & vector store logic
│   ├── monitoring/      # Evidently AI monitoring setup
│   └── pipelines/       # Training & inference pipelines
├── Dockerfile           # Docker configuration
├── pyproject.toml       # Project dependencies and configuration
├── requirements.txt     # Python dependencies (legacy)
├── uv.lock              # Lock file for uv package manager
└── .gitignore           # Git ignore rules
```

## 🛠️ Getting Started

### Prerequisites

- **Python 3.11+**
- **uv** (recommended) or **pip**

### Installation

1. **Clone the repository**:

   ```bash
   git clone <repository-url>
   cd nlp-support-pipeline-mlops
   ```

2. **Install dependencies**:
   Using `uv` (recommended):
   ```bash
   uv sync
   ```

## 🏃 Usage

### 1. Run the Pipeline (Inference)

To classify a single support ticket, run the `main.py` script:

```bash
python main.py
```

This will load the trained model artifacts from `notebooks/best_email_classifier.pkl` and predict the category for a sample ticket.

### 2. Training

To retrain the model, execute the training pipeline:

```bash
python src/pipelines/training_pipeline.py
```

### 3. Monitoring

Monitoring reports are generated using Evidently AI. Check the `src/monitoring` directory for configuration and report generation scripts.

## ⚙️ Configuration

Key configurations such as model names, paths, and hyperparameters can be found in `src/config.py`.

## 🐳 Docker Support

Build the Docker image:

```bash
docker build -t nlp-support-pipeline .
```

Run the container:

```bash
docker run nlp-support-pipeline
```

## Docker & Monitoring Stack

The project uses a multi-container architecture for the monitoring suite, which can run alongside the NLP pipeline.

### 1. Build and Launch the Monitoring Stack

Start the Prometheus, Grafana, and resource exporters with a single command:

```bash
docker compose up -d
```

### 2. Accessing Services

The following services will be available:

| Service | URL | Usage |
| :--- | :--- | :--- |
| **Prometheus** | `http://localhost:9090` | Query raw hardware/container metrics |
| **Grafana** | `http://localhost:3000` | View visual dashboards (Default: admin/admin) |
| **cAdvisor** | `http://localhost:8080` | Real-time container resource usage |
| **Node Exporter** | `http://localhost:9100` | Hardware and OS metrics |

