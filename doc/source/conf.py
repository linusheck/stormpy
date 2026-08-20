# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# Needed for version information
import re

import stormpy

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "stormpy"
copyright = "2016-2026 Storm Developers"
author = "Sebastian Junges, Matthias Volk"
release = stormpy.__version__
language = "en"


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.autosectionlabel",
    #'sphinx.ext.intersphinx',
    "sphinx.ext.githubpages",
    "sphinx_copybutton",
    "nbsphinx",
    "myst_parser",
]
autosectionlabel_prefix_document = True

# Autodoc options
autoclass_content = "both"  # Add documentation for both the class and __init__

# Display e.g. "BitVector" instead of "stormpy.storage.BitVector"
python_use_unqualified_type_names = True
# Wrap long signatures instead of scrolling them
python_maximum_signature_line_length = 100

templates_path = ["_templates"]
exclude_patterns = []

add_module_names = False


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_nefertiti"
html_theme_options = {
    ## Font options
    "sans_serif_font": "Nunito",
    "monospace_font": "Ubuntu Sans Mono",
    ## Style options
    "style": "blue",
    "style_header_neutral": False,
    "pygments_light_style": "pastie",
    "pygments_dark_style": "dracula",
    "logo": "storm_logo.png",
    "logo_width": 36,
    "logo_height": 36,
    "logo_alt": "Storm logo",
    ## Repos
    "repository_name": "stormpy",
    "repository_url": "https://github.com/stormchecker/stormpy",
    ## Header options
    "header_links_in_2nd_row": False,
    "header_links": [
        {
            "text": "Getting Started",
            "link": "getting_started",
        },
        {
            "text": "Documentation",
            "match": "doc/*",
            "dropdown": (
                {
                    "text": "Advanced Examples",
                    "link": "advanced_topics",
                },
                {
                    "divider": True,
                },
                {
                    "text": "Getting Started with Pycarl",
                    "link": "using_pycarl",
                },
            ),
        },
        {
            "text": "API",
            "link": "api",
            "match": "api/*",
        },
        {
            "text": "Storm",
            "link": "https://www.stormchecker.org/",
        },
    ],
    ## Footer options
    "footer_links": [
        {
            "text": "Documentation",
            "link": "https://stormchecker.github.io/stormpy/",
        },
        {
            "text": "Package",
            "link": "https://pypi.org/project/stormpy/",
        },
        {
            "text": "Repository",
            "link": "https://github.com/stormchecker/stormpy/",
        },
        {
            "text": "Issues",
            "link": "https://github.com/stormchecker/stormpy/issues",
        },
    ],
    "show_powered_by": True,
}
html_static_path = ["_static"]
html_css_files = ["custom.css"]
html_favicon = "_static/favicon.png"


# -- Nbsphinx options --
# Need to set newer require.js version to fix JavaScript issues with older version
nbsphinx_requirejs_path = "https://cdnjs.cloudflare.com/ajax/libs/require.js/2.3.7/require.min.js"

# Add binder badge
nbsphinx_prolog = """
{% set docname = env.doc2path(env.docname, base=False) %}

.. raw:: html

    <div class="admonition note">
      Try online: <span><a href="https://mybinder.org/v2/gh/stormchecker/stormpy/master?filepath=notebooks/{{ docname }}"><img alt="Binder badge" src="https://mybinder.org/badge_logo.svg" style="margin-bottom: 0rem"></a></span>
    </div>
"""

# -- Myst options --
myst_enable_extensions = [
    "colon_fence",
]

# The following code makes Sphinx display e.g. "Environment()" instead of "<stormpy.Environment object at 0x10abc123>"
_PYBIND_OBJECT_REPR = re.compile(r"<(?P<type>[A-Za-z_]\w*(?:\.[A-Za-z_]\w*)*) object(?: at 0x[0-9a-fA-F]+)?>")


def _stabilize_pybind_signatures(app, what, name, obj, options, signature, return_annotation):
    if signature is not None:
        signature = _PYBIND_OBJECT_REPR.sub(lambda match: f"{match.group('type').rsplit('.', 1)[-1]}()", signature)
    return signature, return_annotation


def setup(app):
    app.connect("autodoc-process-signature", _stabilize_pybind_signatures)
