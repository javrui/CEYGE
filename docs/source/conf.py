# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'ceyge'
copyright = '2025, javrui'
author = 'javrui'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

templates_path = ['_templates']
exclude_patterns = []

language = 'es'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_static_path = ['_static']

# -- Config predefinida javrui -----------------------------------------------
#> Add the required extensions:

extensions = [
    'sphinx.ext.autodoc',        # Automatically document Python modules
    'sphinx.ext.autosummary',    # Generate summary tables for modules
    'sphinx.ext.napoleon',       # Parse Google/NumPy-style docstrings
    'sphinx_autodoc_typehints',  # Add type hints to documentation
    'm2r2'                       # Support Markdown files
]


#> Set the path to include your project directory:
#(path to locate `search_GitHub-javrui`)

import os
import sys
sys.path.insert(0, os.path.abspath('../../'))



#> Enable .md file processing, adding:

source_suffix = ['.rst', '.md']


#> Configure autodoc, adding:

autodoc_member_order = 'bysource'  # Order by appearance in code
autodoc_typehints = 'description'  # Include type hints in descriptions

#> Modificar tema de splhinx, sustitutendo la linea por esta:

html_theme = 'sphinx_rtd_theme'


#> Configurar settings de Napoleon (interporete de Google style docstrings)

# Napoleon settings
napoleon_google_docstring = True  # Enable parsing of Google-style docstrings
napoleon_numpy_docstring = False  # Disable NumPy-style docstrings (optional)
napoleon_include_init_with_doc = True  # Include `__init__` docstrings
napoleon_include_private_with_doc = False  # Exclude private members
napoleon_use_param = True  # Use `:param` for parameters in the output
napoleon_use_rtype = True  # Use `:rtype` for return types
napoleon_preprocess_types = True  # Preprocess type hints for better formatting