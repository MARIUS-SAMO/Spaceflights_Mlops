"""Project pipelines."""
from typing import Dict

from kedro.framework.project import find_pipelines
from kedro.pipeline import Pipeline
from spaceflights.pipelines import etl as etl
from spaceflights.pipelines import ml as ml



def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from pipeline names to ``Pipeline`` objects.
    """
    etl_pipeline = etl.create_pipeline()
    ml_pipeline = ml.create_pipeline()
    
    return {
        "__default__": etl_pipeline + ml_pipeline,
        "etl" : etl_pipeline,
        "ml" : ml_pipeline
        
    }