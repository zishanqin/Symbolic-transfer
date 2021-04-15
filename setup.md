set up csit GPU lab environment

### init conda
```
source /usr/local/anaconda3/etc/profile.d/conda.sh
```

### create new conda environment
```
conda create -n myenv python=3.7
```

### enter new conda environment
```
conda activate myenv
```
Terminal should look like
```
(myenv) uid@partch:~$ 
```

### install tensorflow
```
pip uninstall tensorflow
conda uninstall tensorflow
conda install tensorflow-gpu==1.14
```
should work, verify:
```
(myenv) uid@partch:~$ python
Python 3.7.10 (default, time) 
[GCC 7.3.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import tensorflow
(...some warning messages...)
>>> 
```

### enter GPU
```
ssh uID@stugpu2.anu.edu.au
```

### init conda and enter myenv again
```
source /usr/local/anaconda3/etc/profile.d/conda.sh
conda activate myenv
```

### verify again just in case
```
(myenv) uid@stugpu2:~$ python
Python 3.7.10 (default, time) 
[GCC 7.3.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import tensorflow
>>> 
```

### install baselines
```
git clone https://github.com/openai/baselines.git
cd baselines
pip install -r requirements.txt
```
verify:
```
pip install pytest
pytest
```


### baselines
template:
```
python -m baselines.run --alg=<name of the algorithm> --env=<environment_id> [additional arguments]
```
algorithms:
`ppo1`
`ppo2`
`dqn`


#### random agent
```
python -m retro.examples.random_agent --game Airstriker-Genesis
```

#### interatctive agent
```
python -m retro.examples.interactive --game Airstriker-Genesis
```

#### DQN agent
training
```
python -m baselines.run --alg=ppo2 --env=PongNoFrameskip-v4 --num_timesteps=2e7 --save_path=~/models/pong_20M_ppo2
```
visualising
```
python -m baselines.run --alg=ppo2 --env=PongNoFrameskip-v4 --num_timesteps=0 --load_path=~/models/pong_20M_ppo2 --play
```


### clone repository from git
```
git clone ...
pip install -r requirements_1.txt
```


### plotting training result (DQN)
```
python -m baselines.run --alg=ppo2 --env=PongNoFrameskip-v4 --num_timesteps=2e7 --save_path=~/models/pong_20M_ppo2 --log_path=~/logs/Pong/
```
and run `dqn_result.ipynb`.


### remove conda env
```
conda remove --name myenv --all 
```

### enter conda
```
conda activate base
```


### show quota (disk space) left
```
quota -vs
```

### remove cache to free up quota
```
rm -rf ~/.cache/

```