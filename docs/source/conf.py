# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Transactional Machine Learning (TML)'
copyright = '2024, Otics Advanced Analytics, Incorporated - For Support email support@otics.ca'
author = 'Sebastian Maurice'

release = '0.1'
version = '0.1.0'

# -- General configuration

# The master toctree document.
master_doc = 'index'

latex_elements = {
    'sphinxsetup': "verbatimforcewraps",        
    'extraclassoptions': 'openany,oneside',
    'releasename': " ",
    'preamble': r'''
        \usepackage{amsmath,amsfonts,amssymb,amsthm}
    ''',
}

latex_documents = [
    (master_doc, 'tml.tex', 'Transactional Machine Learning Documentation',
     'Author Name', 'manual'),
]
extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.autosectionlabel',
    'sphinx_copybutton',
    'sphinx.ext.mathjax'
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'
