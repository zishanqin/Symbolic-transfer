# Generative adversarial transfer learning for symbolic representation in DRL
### Presentation url
Tut W9: https://youtu.be/JaT9m5BhNh4<br>
Tut W8: https://youtu.be/r4dzfbB_w8Y<br>
Tut W7: https://youtu.be/r4mUwgBTt0k

# TODO
1. GAN configuration
2. Game configuration, selection, visualisation (compare to DQN) (Junming)
3. Symbolic extraction: read paper (Wei), Contrastive learning coding part (Zishan)
4. Combination of GAN and symbolic AI
5. Report

# Questions
1. Game suggestions for symbolic GAN

# Due date
1. Finish A3 questions (Q3 find paper) before 7 May
2. 10 May (week 10) prepare presentation
3. 17 May/ 24 May lecture presentation + 19 May/ 26 My lecture presentaion

# Reference
### Symbolic: 
1. State of the art: https://github.com/taesungp/contrastive-unpaired-translation ISSUE: may not be compatible with the inverse GAN process<br>
2. Deep Feature Extraction for Sample-Efficient Reinforcement Learning: https://danielegrattarola.github.io/files/publications/2017_10_grattarola_master_thesis.pdf Chapter 4 <br>
3. Symbolic Reinforcement Learning with Common Sense: https://github.com/AimoreRRD/Reinforcement-Learning-Research

### Probe policy:
Single Episode Policy Transfer in Reinforcement Learning
https://arxiv.org/abs/1910.07719

### Games: <br> 
1. Baselines (using DQN or PPO) https://openai.com/blog/openai-baselines-dqn/cs/
2. Seleted Games for the project (Enduro, Venture, Bowling?) http://gym.openai.com/envs/#classic_control <br>
3. Encountered problems: Atari games are complex domains, and the symbolic representations might not be easily underastandable. Change to easier domain as symbolic.3.

### Previous documentation 
url: https://anu365-my.sharepoint.com/:w:/g/personal/u6808226_anu_edu_au/EbjwMkLdK19KiLQwz_D9BZwB7MWk1nRQBs57UB8yXFS1eA?e=6hFOjz<br>
report link: https://anu365-my.sharepoint.com/:w:/g/personal/u6808226_anu_edu_au/EVur9NIUDHxNio0RT4jwvMYBo5k63a0kpeVr-Oio4YkJyA?e=gogCRB

---

## Installation

### create conda virtual env
```
conda create -n symbolenv python=3.6
```

### enter virual environment
```
conda activate symbolenv
```

### install packages (!!watch out for `conda` and `pip`!!)
```
pip install pygame

pip install pandas==0.20.3

pip install xlrd==1.2.0

conda install matplotlib

conda install xlsxwriter
```

### run the file
```
cd symbolic_game/
python NEW_GAME.py
```
Press `G` to pause the game and plot graph. Close the graph to continue game playing.
