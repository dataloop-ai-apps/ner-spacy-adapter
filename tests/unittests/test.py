import dtlpy as dl
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from adapter import Adapter


def prd():
    dataset = project.datasets.get(dataset_id='')
    item_json = dataset.items.get(item_id='')
    items = [item_json]
    adapter.predict_items(items=items, with_upload=True)


if __name__ == '__main__':
    # dl.login()
    # dl.setenv('rc')

    project = dl.projects.get(project_id='')

    model_entity = dl.models.get(model_id='')
    model_entity.model_artifacts = []

    adapter = Adapter(model_entity=model_entity)

    prd()