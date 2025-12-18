
# SHL GenAI Assessment Recommendation System

A GenAI-powered Retrieval-Augmented Generation (RAG) system that recommends the most relevant
SHL Individual Test Solutions from natural language hiring queries, job descriptions, or JD URLs.

This repository was developed as part of SHL’s GenAI Technical Assessment and demonstrates
end-to-end AI engineering, including data ingestion, semantic retrieval, evaluation, and deployment.

---

## Problem Statement

Recruiters often rely on keyword-based filtering to select assessments, which is inefficient
and fails to capture the true intent of a role. This system uses semantic understanding and
retrieval-based AI to intelligently recommend assessments aligned with job requirements.

---

## Solution Overview

Hiring Query / Job Description
→ Query Understanding (GenAI-assisted)
→ Semantic Embedding Generation
→ Vector Similarity Search
→ Re-ranking & Balance Logic
→ Top 5–10 SHL Assessment Recommendations

---

## Repository Structure

shl-genai-assessment-recommendation/
├── api/                # FastAPI backend
├── src/                # Core recommendation logic
├── frontend/           # Streamlit web application
├── evaluation/         # Recall@10 evaluation
├── data/               # SHL catalog data
├── shashwat_pandey.csv # SHL submission predictions
└── SHL_GenAI_Approach.pdf

---

## Technology Stack

- Python
- FastAPI
- Sentence-Transformers
- NumPy
- Streamlit
- Render
- Streamlit Cloud

---

## Evaluation

The system is evaluated using Mean Recall@10 on labeled training data.
Evaluation is applied at both retrieval and final recommendation stages
to ensure robustness and relevance.

---

## API Endpoints

GET /health  
POST /recommend

---

## Author

Shashwat Pandey
