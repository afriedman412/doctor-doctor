import os

import deepdoctection as dd

os.environ["USE_DD_PILLOW"] = "True"
os.environ["USE_DD_OPENCV"] = "False"

analyzer = dd.get_dd_analyzer(
    config_overwrite=[
        "PT.LAYOUT.WEIGHTS=microsoft/table-transformer-detection/pytorch_model.bin",
        "PT.ITEM.WEIGHTS=microsoft/table-transformer-structure-recognition/pytorch_model.bin",
        "PT.ITEM.FILTER=['table']",
        "OCR.USE_DOCTR=True",
        "OCR.USE_TESSERACT=False",
    ])

