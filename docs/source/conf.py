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
sys.path.insert(0, os.path.abspath('../..'))


# -- Project information -----------------------------------------------------

project = 'pyTermTk'
copyright = '2021, Eugenio Parodi'
author = 'Eugenio Parodi'

# The full version, including alpha/beta/rc tags
if os.path.exists(versionFile:=os.path.join(os.path.dirname(os.path.abspath(__file__)),'../../tmp/docversion.txt')):
    with open(versionFile) as f:
        release = f.read()
else:
    release = 'X.XX.X-a'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.intersphinx',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.autosectionlabel',
	'sphinx_epytext',
    'sphinxcontrib_autodocgen',
    #'sphinxcontrib.fulltoc',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.

html_theme = 'sphinx_rtd_theme' # read-the-docs theme looks better than the default "classic" one but has bugs e.g. no table wrapping

html_theme_options = {
    'display_version': True,
    #'prev_next_buttons_location': 'bottom',
    #'style_external_links': False,
    #'vcs_pageview_mode': '',
    #'style_nav_header_background': 'white',
    # Toc options
    'collapse_navigation': True,
    'sticky_navigation': True,
    #'navigation_depth': 4,
    'includehidden': True,
    #'titles_only': False
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_css_files = [
    # Workaround for RTD 0.4.3 bug https://github.com/readthedocs/sphinx_rtd_theme/issues/117
    'theme_overrides.css',  # override wide tables in RTD theme
    'ttk.css'
]

html_favicon = "https://ceccopierangiolieugenio.github.io/pyTermTk/sandbox/www/favicon.ico"

# html_theme = 'bizstyle'

#html_theme_options = {
#    "sidebar_width": '240px',
#    "stickysidebar": True,
#    "stickysidebarscrollable": True,
#    "contribute": True,
#    "github_fork": "useblocks/groundwork",
#    "github_user": "useblocks",
#}


# import m2r
#
# def docstring(app, what, name, obj, options, lines):
#     md  = '\n'.join(lines)
#     rst = m2r.convert(md)
#     lines.clear()
#     lines += rst.splitlines()
#
# def setup(app):
#     app.connect('autodoc-process-docstring', docstring)

import TermTk

add_module_names = False
autosummary_generate = True
autosummary_generate_overwrite = False

autodocgen_config = {
        'modules':[TermTk],
        'generated_source_dir': os.path.abspath('.')+'/autogen.TermTk/',
        #'add_module_names': False,

        # if module matches this then it and any of its submodules will be skipped
        # 'skip_module_regex': '(.*[.]__|myskippedmodule)',
        'skip_module_regex': '(.*[.]__|myskippedmodule)',

        # produce a text file containing a list of everything documented. you can use this in a test to notice when you've
        # intentionally added/removed/changed a documented API
        'write_documented_items_output_file': 'autodocgen_documented_items.txt',

        # customize autodoc on a per-module basis
        # 'autodoc_options_decider': {},
        # 'autodoc_options_decider': {'members':True, 'inherited-members':True},
        # Can you believe I had to debug autodoc to figure out this FUCKING thing?
        # People are complainig to the lack of documentation of pyTermTk
        # but aat least i hacve examples that cover most use cases
        'autodoc_options_decider': lambda app, what, fullname, obj, docstring, defaultOptions, extra: {'members': True, 'inherited-members':True},

        # choose a different title for specific modules, e.g. the toplevel one
        #'module_title_decider': lambda modulename: 'API Reference' if modulename=='TermTk' else modulename,
}

# autodoc_default_options = { 'inherited-members':True }
autodoc_default_options = {
    'exclude-members': ('as_integer_ratio , bit_count , bit_length , '
                        'conjugate , denominator , from_bytes , imag , '
                        'numerator , real , to_bytes')
}

# Mock pyodide to avoid autogen failure
class pyodideProxy(): pass
sys.modules['pyodideProxy'] = pyodideProxy

class pyodide(): __version__ = "NA"
sys.modules['pyodide'] = pyodide

class windll(): pass
sys.modules['ctypes.windll'] = windll
