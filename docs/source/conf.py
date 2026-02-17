#!/usr/bin/env python3
project = 'Multi-Stage Verification'
author = 'Gus Smith'
copyright = ''

# select HTML theme
html_theme = 'furo-ys'
html_css_files = ['custom.css']
html_theme_options: dict[str, str] = {
    "source_repository": "https://github.com/YosysHQ-Docs/AppNote-130",
    "source_branch": "main",
    "source_directory": "docs/source/",
}

# These folders are copied to the documentation's HTML output
html_static_path = ['_static', '_images']

# code blocks style 
highlight_language = 'text'

# generate section labels from their heading
extensions = ['sphinx.ext.autosectionlabel']

# ensure that autosectionlabel will produce unique names
autosectionlabel_prefix_document = True

from sphinx.application import Sphinx
def setup(app: Sphinx) -> None:
    from furo_ys.lexers.SBYLexer import SBYLexer
    app.add_lexer("sby", SBYLexer)
