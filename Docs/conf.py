#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# AMMR documentation build configuration file, created by
# sphinx-quickstart on Wed Aug 23 14:56:19 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- General configuration ------------------------------------------------


import os
import re
import sys
import subprocess
from pathlib import Path
from datetime import datetime


sys.path.insert(0, os.path.abspath("exts"))
sys.path.insert(0, os.path.abspath("tools"))

try:
    import pygments_anyscript
except ImportError:
    raise ImportError("Please install pygments_anyscript to get AnyScript highlighting")


def tagged_commit():
    """Check if we are on a tagged commit"""
    try:
        subprocess.check_call(
            ["git", "describe", "--tags", "--exact-match", "HEAD"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
    except subprocess.CalledProcessError:
        return False
    else:
        return True


if tags.has("offline"):
    # building offline version
    pass


if not tagged_commit() and not tags.has("offline"):
    tags.add("draft")


# `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = tags.has("draft")


# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "sphinx.ext.mathjax",
    "sphinx.ext.githubpages",
    # 3rd party extensions
    # 'sphinxcontrib.fulltoc',
    # "sphinx_gallery.gen_gallery",
    "ammr_directives",
    "inline_highlight",
    "myst_parser",
    "sphinxext.opengraph",
    "sphinx_design",
    "sphinx_togglebutton",
    "sphinx_copybutton",
]

myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "fieldlist",
    "dollarmath",
    "amsmath",
    "html_image",
    "substitution",
    "attrs_inline",
]


# sphinx_gallery_conf = {
#     # path to your examples scripts
#     "examples_dirs": "Applications",
#     # path where to save gallery generated examples
#     "gallery_dirs": "auto_examples",
#     "backreferences_dir": "auto_examples/backreferences",
#     "doc_module": ("gallery",),
#     "backreferences_heading": False,
#     # directory where function granular galleries are stored
#     "download_section_examples": False,
#     "download_all_examples": False,
#     "min_reported_time": 100,
#     "show_code_section": False,
#     "default_thumb_file": "_static/no_image.png",
#     "thumbnail_size": (320, 280),
#     "is_egg_file": True,
# }


# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
source_suffix = [".rst", ".md"]

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = "en"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = [
    "_build",
    "README.md",
    "Thumbs.db",
    ".DS_Store",
    "exts",
    "auto_examples",
]

# The name of the Pygments (syntax highlighting) style to use.
highlight_language = "AnyScriptDoc"
pygments_style = "AnyScript"


current_year = os.environ.get("YEAR", datetime.now().year)

ams_version = os.environ.get("AMS_VERSION", "7.4.3")
if not re.match("^\d\.\d\.\d", ams_version):
    raise ValueError("Wrong format for AMS version, environment variable")
ams_version_short = ams_version.rpartition(".")[0]
ams_version_x = ams_version_short + ".x"


ammr_version = os.environ.get("AMMR_VERSION", None)
if ammr_version is None:
    AMMR_VERSION_RE = re.compile(r'.*AMMR_VERSION\s"(?P<version>.*)"')
    with open("../AMMR.version.any") as fh:
        match = AMMR_VERSION_RE.search(fh.read())
        if match:
            ammr_version = match.groupdict()["version"]
        else:
            raise Exception("Could not parse AMMR version")


if not re.match("^\d\.\d\.\d", ammr_version):
    raise ValueError("Wrong format for AMMR version, environment variable")

ammr_version_short = ammr_version.rpartition(".")[0]

# .. include:: /bm_config/Substitutions.txt

rst_epilog = f"""

.. |AMS| replace:: AnyBody Modeling System™
.. |AMS_VERSION_X| replace:: {ams_version_x}
.. |AMS_VERSION| replace:: {ams_version}
.. |AMS_VERSION_SHORT| replace:: {ams_version_short}
.. |AMMR_VERSION_SHORT| replace:: {ammr_version_short}
.. |AMMR_VERSION| replace:: {ammr_version}
.. |AMMR_DEMO_INST_DIR| replace:: :literal:`~/Documents/{ams_version_x}/AMMR.v{ammr_version}-Demo`
.. |CURRENT_YEAR| replace:: {current_year}
.. |WHAT_IS_NEW| replace:: :ref:`What's new in AMMR {ammr_version} <whats-new>`
.. |DOI| image:: https://zenodo.org/badge/DOI/10.5281/zenodo.1250764.svg
                 :target: https://doi.org/10.5281/zenodo.1250764
"""


myst_substitutions = {
    "AMS": "AnyBody Modeling System™",
    "AMS_VERSION_X": ams_version_x,
    "AMS_VERSION": ams_version_x,
    "AMS_VERSION_SHORT": ams_version_short,
    "AMMR_VERSION_SHORT": ams_version_short,
    "AMMR_VERSION": ammr_version,
    "CURRENT_YEAR": current_year,
    "AMMR_DEMO_INST_DIR": f"`~/Documents/{ams_version_x}/AMMR.v{ammr_version}-Demo`",
    "DOI": "[![DOI image](https://zenodo.org/badge/DOI/10.5281/zenodo.1250764.svg)](https://doi.org/10.5281/zenodo.1250764)",
    "WHAT_IS_NEW": f"{{ref}}`What's new in AMMR {ammr_version} <whats-new>`",
    "WHAT_IS_NEW2": f"{{material-outlined}}`update;1em` New in AMMR {ammr_version}",
}


no_index = """
.. meta::
   :robots: noindex
"""
myst_html_meta = {}

if tags.has("draft"):
    rst_epilog = rst_epilog + no_index
    myst_html_meta["robots"] = "noindex"


# Monkeypatch sphinx.domains.changeset.versionslabels dictionary
# highlight AMMR
# from sphinx.domains.changeset import versionlabels
from sphinx.locale import _
from sphinx.domains.changeset import versionlabels

versionlabels.update(
    {
        "versionadded": _("New in AMMR %s"),
        "versionchanged": _("Changed in AMMR %s"),
        "deprecated": _("Deprecated since AMMR %s"),
    }
)


# General information about the project.
project = "AMMR"
copyright = f"{current_year}, AnyBody Technology"
author = "AnyBody Technology"

github_doc_root = "https://github.com/AnyBody/ammr/tree/master/Docs"


# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = f"{ammr_version_short}"
# The full version, including alpha/beta/rc tags.
release = f"{ammr_version}"

if tags.has("draft") and not release.endswith("beta"):
    release = release + "-beta"


# suppress_warnings = ["ref.citation"]


# -- Options for HTML output ----------------------------------------------


# html_sidebars = {
#     "**": ["searchbox.html", "globaltoc.html"],  # 'sourcelink.html', ],
#     "using/windows": ["windowssidebar.html", "searchbox.html"],
# }

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_book_theme"


html_copy_source = False


html_title = "%s v%s Documentation" % (project, release)

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme = "redcloud"
# html_theme_options = {
#     'roottarget': index_doc,
#     'max_width': '1100px',
#     'minimal_width': '700px',
#     'borderless_decor': True,
#     'lighter_header_decor': False,
#     'sidebarwidth': "3.8in",
#     'fontcssurl': 'https://fonts.googleapis.com/css?family=Noticia+Text|Open+Sans|Droid+Sans+Mono',
#     'relbarbgcolor': '#999999',
#     'footerbgcolor': '#953337',
#     'sidebarlinkcolor': '#953337',
#     'headtextcolor': '#953337',
#     'headlinkcolor': '#953337',
# }


html_theme_options = {
    # 'single_page': True,
    #    "extra_navbar": "",
    #    "logo_only": True,
    "home_page_in_toc": False,
    "show_navbar_depth": 1,
    "use_download_button": False,
    # "default_mode": "dark",
    "pygment_light_style": "AnyScript",
    "pygment_dark_style": "stata-dark",
}


# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = "_static/AMMR.svg"

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = "_static/favicon.ico"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static", "body/_static"]

# Custom sidebar templates, maps document names to template names.
# html_sidebars = {'**': ['searchbox.html', 'globaltoc.html']}


# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = project

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',
    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',
    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',
    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    ("index", "AMMR.tex", "AMMR Documentation", "AnyBody Technology", "manual")
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [("index", "ammr", "AMMR Documentation", [author], 1)]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        "index",
        "AMMR",
        "AMMR Documentation",
        author,
        "AMMR",
        "One line description of project.",
        "Miscellaneous",
    )
]


intersphinx_mapping = {}
if tags.has("offline"):
    # Todo. Find a way to link to offline html versions.
    intersphinx_mapping["tutorials"] = ("https://anyscript.org/tutorials/", None)
else:
    if tags.has("draft"):
        intersphinx_mapping["tutorials"] = (
            "https://anyscript.org/tutorials/beta/",
            None,
        )
    else:
        intersphinx_mapping["tutorials"] = ("https://anyscript.org/tutorials/", None)


# -- Options for OpenGraph Ext. ----------------------------------------------
# settings to control how the OpenGraph extension generates meta tags
ogp_site_url = "https://anyscript.org/"
ogp_site_name = "AMMR Documentation"
ogp_image = "https://anyscript.org/ammr/_static/AMMR_Logo.png"
ogp_use_first_image = True  # if not found defaults to 'ogp_image'


# Generate gallery files
import jinja2
import frontmatter

gallery = {}
galleryfolders = [x for x in Path("Applications").iterdir() if x.is_dir()]
for folder in galleryfolders:
    gallery[folder] = []
    for file in sorted(folder.glob("*.md"), key=lambda x: x.name.upper()):
        post = frontmatter.load(file)
        if "gallery_title" in post:
            gallery[folder].append(
                {
                    "doc": file.with_suffix("").as_posix(),
                    "title": post["gallery_title"],
                    "image": post["gallery_image"],
                }
            )

with open("Applications/gallery.txt.jinja2") as fh:
    gallery_template = jinja2.Template(fh.read())

for folder, section in gallery.items():
    gallery_txt = folder / "gallery.txt"
    content = gallery_template.render(examples=section)
    with open(gallery_txt, encoding="utf8") as fh:
        previous_content = fh.read()
    if content != previous_content:
        with open(gallery_txt, "w", encoding="utf8") as fh:
            fh.write(content)

# Run the python file "tools/generate_class_template_docs.py"
# to generate the class template documentation
# class_template_gen =Path("tools/generate_class_template_docs.py")
# exec(class_template_gen.read_text())


import generate_class_template_docs
generate_class_template_docs.run_all()



linkcheck_ignore = [
    r".*linkcheck_ignore",
    "https://doi.org/10.1115/1.4037100",  # asme.org prevents the linkcheck
    "https://doi.org/10.1115/1.4052115",  # asme.org prevents the linkcheck
    "https://dx.doi.org/10.1115/1.4001678",  # asme.org prevents the linkcheck
    "https://dx.doi.org/10.1115/1.4029258",  # asme.org prevents the linkcheck
    "https://doi.org/10.1080/10255842.2020.1851367",  # tandfonline.com prevents the linkcheck
    "https://dx.doi.org/10.1002/jor.20255",  # wiley.com prevents the linkcheck
    "https://doi.org/10.1016/j.clinbiomech.2006.10.003",  # clinbiomech.com prevents the linkcheck
    "https://github.com/anybody/ammr",  # AMMR is not yet public
]

linkcheck_allowed_redirects = {
    "https://doi.org.*": ".*",
    "https://dx.doi.org.*": ".*",
    "https://www.anybodytech.com/download/anybodysetup.*": ".*",
}


def setup(app):
    app.add_css_file("theme_override.css")
    app.add_css_file("custom.css")
