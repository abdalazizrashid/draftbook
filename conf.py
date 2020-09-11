# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('sphinxext'))


# -- Project information -----------------------------------------------------

project = 'Draftbook'
copyright = '2020, Abdalaziz Rashid'
author = 'Abdalaziz Rashid'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.

extensions = [
    'matplotlib.sphinxext.plot_directive',
    'IPython.sphinxext.ipython_directive',
    'IPython.sphinxext.ipython_console_highlighting',
    'sphinx.ext.doctest',
    'sphinx.ext.inheritance_diagram',
    'numpydoc',
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx_math_dollar',
    'sphinx.ext.mathjax',
    'sphinx_math_dollar'
    ]

mathjax_config = {
    'tex2jax': {
    'inlineMath': [ ["\\(","\\)"] ],
    'displayMath': [["\\[","\\]"] ],
    },
    'TeX': {
    'Macros': {
      'b': [r"{\mathbf #1}",1],
      'bb': [r'{\mathbb{#1}}', 1],
      'vertbar': r"\rule[-1ex]{0.5pt}{2.5ex}",
      'horzbar': r"\rule[.5ex]{2.5ex}{0.5pt}"
    }
  }
}
#extensions = ['matplotlib.sphinxext.plot_directive',
#                  'IPython.sphinxext.ipython_directive',
#                  'IPython.sphinxext.ipython_console_highlighting',
#                  'sphinx.ext.mathjax',
#                  'sphinx.ext.autodoc',
#                  'sphinx.ext.doctest',
#                  'sphinx.ext.inheritance_diagram',
#                  'numpydoc']
#

#extensions.append('sphinx.ext.jsmath')

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_book_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

latex_engine = 'xelatex'
latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    'papersize': 'a4paper',
    'releasename':" ",
    # Sonny, Lenny, Glenn, Conny, Rejne, Bjarne and Bjornstrup
    # 'fncychap': '\\usepackage[Lenny]{fncychap}',
    'fncychap': '\\usepackage{fncychap}',
    'fontpkg': '\\usepackage{amsmath,amsfonts,amssymb,amsthm}',

    'figure_align':'htbp',
    # The font size ('10pt', '11pt' or '12pt').
    #
    'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    }


