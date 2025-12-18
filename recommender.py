
"""
SHL GenAI Assessment Recommendation Engine
------------------------------------------
This module implements the core Retrieval-Augmented Recommendation logic
using semantic embeddings and cosine similarity.

Author: Shashwat Pandey
"""

from typing import List, Dict
import numpy as np
from sentence_transformers import SentenceTransformer


class SHLRecommender:
    """
    Core recommender class for SHL assessment recommendation.
    """

    def __init__(self, catalog: List[Dict]):
        """
        Initialize recommender with SHL catalog.

        Args:
            catalog (List[Dict]): List of SHL assessment metadata dictionaries
        """
        self.catalog = catalog
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

        self.embeddings = self.model.encode(
            [item["description"] for item in catalog],
            normalize_embeddings=True
        )

    def recommend(self, query: str, top_k: int = 10) -> List[Dict]:
        """
        Recommend top-k SHL assessments for a given query.

        Args:
            query (str): Hiring query or job description
            top_k (int): Number of recommendations

        Returns:
            List[Dict]: Ranked SHL assessment recommendations
        """
        query_embedding = self.model.encode(
            [query],
            normalize_embeddings=True
        )

        similarity_scores = np.dot(
            self.embeddings, query_embedding.T
        ).flatten()

        ranked_indices = similarity_scores.argsort()[::-1][:top_k]

        return [self.catalog[i] for i in ranked_indices]
