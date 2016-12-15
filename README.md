# loadstone
CLI for setting up PySpark + Jupyter on a AWS cluster launched via Flintrock

# overview
Flintrock is a great tool for launching an AWS cluster with Spark installed and ready to go. However, if you want to use PySpark and the Jupyter Notebook to interact with Spark, then there is some more setup to be done. Loadstone is a command-line interface that automates this setup; it will have you in a Jupyter Notebook running PySpark in no time flat.

With everything configured correctly, launching a cluster with Flintrock can be as simple as
```bash
flintrock launch test-cluster
```
You can then install and configure the IPython stack + Jupyter notebook with
```bash
loadstone setup test-cluster
```
After that, you can install additional dependencies from PyPI or Anaconda
```bash
loadstone conda-install scikit-learn test-cluster
loadstone pip-install thunder test-cluster
```
And when you're ready, you can fire up the Jupyter Notebook server
```bash
loadstone notebook start test-cluster
loadstone notebook stop test-cluster
```
Of course at any time, you can do more advanced setup using Flintrock, or by logging into your master node
```
flintrock login test-cluster
```

# notes
Loadstone currently installs the following version of Python:
- Miniconda 3.7.3
Loadstone currently installs the following Python packages (and dependencies) during setup:
- Jupyter
- NumPy
- SciPy
- Matplotlib


# flintrock notes
Currently, Loadstone only works if you are using the default configuration file for Flintrock. To set this up, first run
```bash
flintrock configure
```
Then run
```bash
flintrock configure --locate
```
to determine where Flintrock has placed the default `config.yaml` file. You will need to edit this file to set any and all parameters for Flintrock, as Loadstone cannot currely pass parameters on to Flintrock. For detailed information on configuring and using Flintrock to launch your AWS instances with Spark, please see the [Flintrock repository](https://github.com/nchammas/flintrock)
