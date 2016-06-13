# install C compiler
sudo yum install -y gcc

# install miniconda
wget http://repo.continuum.io/miniconda/Miniconda-3.7.3-Linux-x86_64.sh -O miniconda.sh
bash miniconda.sh -b -p $HOME/miniconda
export PATH=$HOME/miniconda/bin:$PATH
conda update -y conda

# install thunder and related packages
conda install jupyter scikit-image
pip install thunder-python
