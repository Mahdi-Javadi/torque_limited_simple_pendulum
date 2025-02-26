# Configuration file for the Sphinx documentation builder.
#
# For a full list of all Sphinx configuration options see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
import datetime
import importlib
import sphinx_rtd_theme

from sphinx.builders.html import StandaloneHTMLBuilder

# Set up paths for import
# file_path = os.path.realpath(__file__)                            # Obtain path of this config file
# root_path = (os.sep).join(file_path.split(os.sep)[:-4])           # Obtain project root path
# sys.path.insert(1, root_path)                                     # Import from root path
sys.path.insert(0, os.path.abspath('../../../software/python/'))

# -- Project information -----------------------------------------------------
#from docs.reference.source.project import project, author, codename, codedir, report_title, report_author, logo
project = 'Torque-limited Simple Pendulum'
author  = 'Felix Wiebe, Jonathan Babel, Shivesh Kumar, Shubham Vyas, Daniel Harnack, Melya Boukheddimi, Mihaela Popescu, Frank Kirchner'
#codename = 'simple_pendulum'
#codedir = 'software/python'
#report_title = rf'Torque-limited\\Simple Pendulum:\\Reference'
#report_author = r'''
#Felix Wiebe, Jonathan Babel,\\
#\vspace*{0.5cm}
#{\fontsize{10}{10}\selectfont Contributors:}\\
#\vspace*{0.2cm}
#Shivesh Kumar, Shubham Vyas, Daniel Harnack,\\
#Melya Boukheddimi, Mihaela Popescu, Frank Kirchner'''
#logo = 'logo.jpg'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
              'sphinx.ext.autodoc',
              'sphinx.ext.autosummary',
              'numpydoc',
              'sphinx.ext.coverage',
              'sphinx.ext.napoleon',
              "sphinx.ext.autosectionlabel",
              ]
numpydoc_show_class_members = False


templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_theme_options={'titles_only' : True,
                    'collapse_navigation' : False,
                    'navigation_depth' : 5,
                    }
html_static_path = ['_static']

#-----------------------------------------------------------------------------
#html_logo = f'../figures/logo.jpg'
html_logo = f'../figures/pendulum_light_painting.jpg'
html_theme_options = {
    'logo_only': False,
    'display_version': True,
}


## Scan the project to generate documentation
#scan = True
#
# # Source
# src = lambda sep: codedir.replace('/', sep) + f'{sep}' if codedir != '.' else ''
#
# # Obtain the project's release version, which must be stored in a
# # __version__ variable inside the main project script or package.
# # WARNING: the script or the package's __init__.py WILL BE RUN
# # on import.
# # In the case of single-script projects, the following architecture
# # is suggested:
# #
# #            # My single-script project
# #
# #            __version__ = <version of your project>
# #
# #            if __name__ == '__main__':
# #                <body of your project>
# release = importlib.import_module(f'{src(".")}{codename}').__version__  # Get project version
#
# sys.path.remove(root_path)                                           # Remove root path from search
#
# # Copyright
# copyright = f'{datetime.datetime.now().date().strftime("%Y")}, {author}'
#
# # Language
# language = 'en'
#
# # -- Text editing ------------------------------------------------------------
#
# # Replacements
# rst_epilog = f'''
# .. |project| replace:: {project}
# .. |version| replace:: {release}
# .. |codename| replace:: {codename}
# '''
#
# # Custom roles
# rst_prolog = '''
# '''
#
# # Cross-referencing
# numfig = True
# numfig_format = {'figure':     'Figure %s',
#                  'table':      'Table %s',
#                  'code-block': 'Listing %s',
#                  'section':    'Section %s'}
# autosectionlabel_maxdepth = 1                      # Automatically label top level sections only
#
# # BibTeX citations
# #    In text:           :cite:t:`key`
# #    Parenthetical:     :cite:p:`key`
# extensions      = ['sphinxcontrib.bibtex']
# bibtex_bibfiles = ['bibliography.bib']
#
# # -- General configuration ---------------------------------------------------
#
# # Extract documentation from the __init__ function of classes
# autoclass_content = 'init'
#
# # Add any Sphinx extension module names here, as strings. They can be
# # extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# # ones.
# extensions += ['sphinx.ext.autodoc',
#                'sphinx.ext.autosummary',
#                'sphinx.ext.imgmath',
#                'sphinx.ext.autosectionlabel'
# ]
#
# # Add any paths that contain templates here, relative to this directory.
# templates_path = ['source/_templates']
#
# # If true, the current module name will be prepended to all description
# # unit titles (such as .. function::).
# add_module_names = False
#
# # A list of prefixes that are ignored for sorting the Python module index
# # (e.g., if this is set to ['foo.'], then foo.bar is shown under B, not F).
# # This can be handy if you document a project that consists of a single package.
# # Works only for the HTML builder currently. Default is [].
# modindex_common_prefix = [f'{codename}.']
#
# # -- Use package and module documentation templates with better_apidoc  --------
# def run_apidoc(app):
#     """Generage API documentation"""
#     import better_apidoc
#
#     # Set package search path
#     sys.path.insert(0, os.path.abspath(f'../../{src("/")}.'))
#
#     better_apidoc.APP = app
#     better_apidoc.main(
#         [
#             'better-apidoc',
#             '-t',
#             templates_path[0],
#             '-fMeET',
#             '-o',
#             'source',
#             f'../../{src("/")}{codename}',
#         ]
#     )
#
# # List of patterns, relative to source directory, that match files and
# # directories to ignore when looking for source files.
# # This pattern also affects html_static_path and html_extra_path.
# exclude_patterns = ['_templates/*']     # Exclude templates from rendering
#
# # -- HTML SETTINGS -------------------------------------------------------------
# root_doc = 'index'
#
# # Figure format priority for .. image:: <name>.*
# StandaloneHTMLBuilder.supported_image_types = [
#     'image/svg+xml',
#     'image/gif',
#     'image/png',
#     'image/jpeg'
# ]
#
# # Add any paths that contain custom static files (such as style sheets) here,
# # relative to this directory. They are copied after the builtin static files,
# # so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']
#
# # The theme to use for HTML and HTML Help pages.  See the documentation for
# # a list of builtin themes.
# html_theme = 'sphinx_rtd_theme'
# extensions += ['sphinx_rtd_theme']
#
# # Logo
# html_logo = f'../figures/{logo}'
# html_theme_options = {
#     'logo_only': False,
#     'display_version': True,
# }
#
# # Math
# imgmath_image_format = 'svg'
# imgmath_latex = 'latex'
# imgmath_latex_preamble = ''
#
# # -- LATEX SETTINGS ------------------------------------------------------------
#
# report_doc             = 'report'
# figures                = [os.path.join(dp, f) for dp, dn, filenames in os.walk('figures') for f in filenames]
# latex_additional_files = ['report.sty', 'project.sty'] + figures
#
# latex_engine = 'lualatex'
#
# latex_elements = {
# 'preamble': r'''
# \RequirePackage{project}
# ''',
# 'releasename': 'Version',
# 'papersize': 'a4paper',
# 'pointsize': '11pt',
# 'classoptions': ',openany,oneside',
# 'maketitle': '\maketitle',
# 'tableofcontents': '',
# 'figure_align': 'H',
# 'sphinxsetup': r'''
# hmargin={2cm,2cm},
# vmargin={4cm,3cm},
# ''',
# }
#
# latex_documents = [
#   (report_doc, 'main.tex', report_title, report_author, 'manual'),
# ]
#
# # Document __init__ files
# special_members = '__init__'
#
# # -- Generate documentation ----------------------------------------------------
# if scan:
#     def setup(app):
#         app.connect('builder-inited', run_apidoc)
