# install and configure Jupyter notebook
pip install jupyter
jupyter notebook --generate-config
echo "
c = get_config()

c.IPKerneyApp.pylab = 'inline'

import os
home = os.path.expanduser('~')

#c.NotebookApp.certfile = home + u'/certs/mycert.pem'
c.NotebookApp.ip = '*'
c.NotebookApp.open_browser = False
c.NotebookApp.port = 9999" >> .jupyter/jupyter_notebook_config.py

