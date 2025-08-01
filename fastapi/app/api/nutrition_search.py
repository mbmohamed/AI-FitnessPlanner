import os
import json
import logging
from typing import List, Dict, Any, Optional
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from langchain_openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.schema import Document
from pymongo import MongoClient
from datetime import datetime


# Set up logging confifguration and fastapi router for the nutrition-vector-search app 
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger("nutrition_vector_search")

nutrition_search = APIRouter()


## Pydantic models for API 
class NutritionQuery(BaseModel):
    query : str = Field(...,description="Natral language search query")
    dietary_restrictions:Optional[List[str]] = Field(default={},description="dietary restrictions imposed by users like 'vegan' , 'sugar-free' ...")
    macro_goals: Optional[Dict[str, float]] = Field(
        default={},
        description="Macro targets like {'protein_min': 20, 'carbs_max': 10}",
    )
    limit: int = Field(default=10, description="Number of results to return")
    similarity_threshold: float = Field(
        default=0.5, description="Minimum similarity score (0-1)"
    )
    use_full_database: bool = Field(
        default=False,
        description="Use full database (branded_foods) vs sample (branded_foods_sample)",
    )

class VectorSearchResponse(BaseModel):
    query: str
    results_found: int
    results: List[Dict[str, Any]]
    search_time_ms: int


   """def get_mongo_client():
    get the mongodb cllient connection 
    global mongo_client
    if mongo_client is None:
        mongo_user"""