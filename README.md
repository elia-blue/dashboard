# Dashboard Project

> A simple, extensible Dashboard written in Python and HTML

The main logic is written in Python 3 and uses Flask as the web framework. The main view are so-called *widgets*,
seperate Python classes in `dashboad/widgets.py` and corresponding HTML / Jinja2 templates (in `dashboard/templates`) 
for rendering in browsers.

Widget classes are always names `<Name>Widget` (e.g. `PingWidget`) and can take a bunch of arguments at initialisation time.
Widget templates, on the other hand, are named `widget_<name>.html` (e.g. `widget_ping.html`) and stored in seperate files in the
`dashboard/templates` directory. Every widget has to contain a `template` and a `name` attribute. The `template` is the full name
of the HTML template file (*name*, not *path*) and `name` should be the human-readable version of the widget's name.
At last, every widget which should be used, has to be initialized in the `widgets` list in `dashboard/__init__.py`.

## Technology used

- `flask` as the web framework for Python
- `scss` for the main application styles (different layouts, colors, fonts, etc.)
- `venv` for reproducability (see `requirements.txt` and [Getting Started](#getting-started))

## Layout

- `.vscode` - Configuration for debugging / running in development
- `dashboard` - Main module containing all templates, styles, widgets and source code
  - `dashboard/scss` - contains all style source code, written in SCSS
  - `dashboard/templates` - contains all Jinja2 templates used, for widgets, as well as for basic layout
  - `dashboard/static` - contains static files (e.g. compiled SCSS)
  - `dashboard/widgets.py` - contains all the widgets (seperate classes)
  - `dashboard/__init__.py` - contains the code for glueing it all together
  - `dashboard/__main__.py` - runs the app if called as a stand-alone module
- `Makefile` - contains most common actions as scripts

## Getting started

0. Clone
1. Initialize virtual environment: `python3 -m venv env` and `source ./env/bin/activate`
2. Install required packages from PyPI: `pip3 install -r requirements.txt`
3. Start the `dashboard` module via CLI (`python3 -m dashboard`) or via VS Code (use launch configuration)