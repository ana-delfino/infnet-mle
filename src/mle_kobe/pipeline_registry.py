"""Project pipelines."""
from __future__ import annotations

from kedro.framework.project import find_pipelines
from kedro.pipeline import Pipeline
from .pipelines.PreparacaoDados import create_pipeline as preparacao_pipeline
from .pipelines.Treinamento import create_pipeline as treinamento_pipeline


def register_pipelines() -> dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from pipeline names to ``Pipeline`` objects.
    """
    # pipelines = find_pipelines()
    # print("Pipelines encontrados:", list(pipelines.keys()))
    # ordered_pipeline = (
    #     pipelines['PreparacaoDados']+
    #     pipelines['Treinamento']
    # )
    # pipelines["__default__"] =  ordered_pipeline 
    # pipelines["__default__"] = sum(pipelines.values())
    return {
        "PreparacaoDados": preparacao_pipeline(),
        "Treinamento": treinamento_pipeline(),
        "__default__": preparacao_pipeline() + treinamento_pipeline(),
    }
