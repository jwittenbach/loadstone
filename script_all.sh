# install C compiler
sudo yum install -y gcc

# install miniconda and required packages
wget http://repo.continuum.io/miniconda/Miniconda-3.7.3-Linux-x86_64.sh -O miniconda.sh
bash miniconda.sh -b -p $HOME/miniconda
export PATH=$HOME/miniconda/bin:$PATH
conda update -y conda
conda install -y pip numpy scipy scikit-learn scikit-image matplotlib

# install thunder and related packages
pip install thunder-python
