"""Helpers for building SDNB workshop notebooks via nbformat.

Provides a tiny `Notebook` builder with `.md(...)` and `.code(...)` methods,
and a standard COLAB_SETUP cell used at the top of every notebook.
"""

from pathlib import Path
import nbformat as nbf

NOTEBOOKS = Path(__file__).resolve().parent.parent / "notebooks"
NOTEBOOKS.mkdir(parents=True, exist_ok=True)


COLAB_SETUP = '''# ── Install & Setup (run this first on Google Colab) ──
import sys, os

try:
    import pandas as pd
    import matplotlib.pyplot as plt
    import numpy as np
    print("✅ All libraries ready!")
except ImportError as e:
    print(f"Installing missing library: {e}")
    os.system("pip install pandas matplotlib numpy seaborn -q")
    import pandas as pd
    import matplotlib.pyplot as plt
    import numpy as np

# Where the CSV data files live.
# - On Colab after uploading the workshop folder: "/content/sdnb_python_workshop/data/"
# - When running locally from notebooks/ folder:   "../data/"
DATA_PATH = "../data/" if os.path.exists("../data") else "data/"
print(f"📁 Using data path: {DATA_PATH}")
'''


class Notebook:
    """Minimal builder around nbformat — chain .md() / .code() calls."""

    def __init__(self):
        self.nb = nbf.v4.new_notebook()
        self.nb["metadata"] = {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3",
            },
            "language_info": {
                "name": "python",
                "version": "3.11",
            },
        }
        self.cells = []

    def md(self, source: str):
        self.cells.append(nbf.v4.new_markdown_cell(source.strip("\n")))
        return self

    def code(self, source: str):
        self.cells.append(nbf.v4.new_code_cell(source.strip("\n")))
        return self

    def save(self, filename: str):
        self.nb["cells"] = self.cells
        path = NOTEBOOKS / filename
        with path.open("w", encoding="utf-8") as f:
            nbf.write(self.nb, f)
        return path
