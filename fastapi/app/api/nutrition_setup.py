import os
import json
import logging
from fastapi import FastAPI , APIRouter, HTTPException
import pymongo


## as always set up a logging config in console and router for the application
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger= logging.getLogger("workout_optimization")

nutrition_setup = APIRouter()

@nutrition_setup.get("/test_mongo_db/")
async def test_mongo_db():
    """Test MongoDB connection with improved error handling"""
    from pymongo import MongoClient, errors

    mongo_user = os.getenv("MONGO_USER")
    mongo_password = os.getenv("MONGO_PASSWORD")
    mongo_db_name = os.getenv("MONGO_DB_NAME")

    mongo_hosts_to_try = [
        ####"mongodb_ai_fitness_planner",  # Docker service name not yet established
        "localhost",  # If running locally mainly for now 
    ]

    for host in mongo_hosts_to_try :
        try:
            logger.info(f"attempting to connect at MongoDB at host : {host}")

            return {
                "status": "success",
                "connected_host": host,
                "port": port,
                "database_name": mongo_db_name or "usda_nutrition",
                "total_collections": len(collection_names),
                "collections_sample": existing_collections,
                "environment_vars": {
                    "MONGO_USER": mongo_user,
                    "MONGO_PASSWORD": "***" if mongo_password else None,
                    "MONGO_DB_NAME": mongo_db_name,
                },}
        
        except errors.ServerSelectionTimeoutError as err: