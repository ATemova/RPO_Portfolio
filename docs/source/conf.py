# Configuration file for the Sphinx documentation builder.

# -- Project information -----------------------------------------------------
project = 'RPO Portfolio (Python Docs)'
author = 'Anastasija Temova'
copyright = '2025, Anastasija Temova'
release = '1.0'

# -- Path setup: allow autodoc to import your modules ------------------------
import os
import sys
# This path points from docs/source/ -> ../../python_src
sys.path.insert(0, os.path.abspath('../../python_src'))

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',   # auto API from docstrings
    'sphinx.ext.napoleon',  # Google/NumPy style docstrings
]

# Optional: nicer default options for autodoc
autodoc_default_options = {
    'members': True,
    'undoc-members': False,
    'show-inheritance': True,
}

templates_path = ['_templates']
exclude_patterns = []

# Language of the docs
language = 'en'

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'   
html_static_path = ['_static']