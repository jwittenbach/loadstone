# configure Jupyter notebook
jupyter notebook --generate-config

echo "
c = get_config()

c.NotebookApp.ip = '*'
c.NotebookApp.open_browser = False
c.NotebookApp.port = 9999
import os
c.NotebookApp.notebook_dir = os.path.expanduser('~')
" >> .jupyter/jupyter_notebook_config.py

# configure Python for Spark workers
echo 'PYSPARK_PYTHON=$HOME/miniconda/bin/python' >> spark/conf/spark-env.sh

# install tmux
sudo yum install tmux
