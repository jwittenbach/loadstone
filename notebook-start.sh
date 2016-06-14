tmux new-session -d -s notebook
tmux send -t notebook IPYTHON_OPTS=notebook SPACE ./spark/bin/pyspark ENTER
