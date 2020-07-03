## Install matplotlib to work on jupyterlab

Complete steps
Install nodejs, e.g. conda install nodejs.
Install ipympl, e.g. pip install ipympl.
[Optional, but recommended; update JupyterLab, e.g.
pip install --upgrade jupyterlab.]
[Optional, but recommended; for a local user installation, run:
export JUPYTERLAB_DIR="$HOME/.local/share/jupyter/lab".]
Install extensions:

jupyter labextension install @jupyter-widgets/jupyterlab-manager
jupyter labextension install jupyter-matplotlib
Enable widgets: jupyter nbextension enable --py widgetsnbextension.

Restart JupyterLab.
Decorate with %matplotlib widget.