# Generative adversarial transfer learning for symbolic representation in DRL
### Presentation url
Tut W10: https://youtu.be/i5gWM5KYeR8<br>
Tut W9: https://youtu.be/JaT9m5BhNh4<br>
Tut W8: https://youtu.be/r4dzfbB_w8Y<br>
Tut W7: https://youtu.be/r4mUwgBTt0k

# Mark:
1. (3 Minute Lecture talk, May24, 11am-1pm) 10 marks - 6 marks for presentation, 4 marks for slides
2. (15 minute tutorial presentation, including 3 minutes for questions) 10 marks – 6 marks for presentation, 4 marks for slides

# TODO
1. GAN configuration
2. Game configuration, selection, visualisation (compare to DQN) (Junming)
3. Symbolic extraction: read paper (Wei), Contrastive learning coding part (Zishan)
4. Combination of GAN and symbolic AI
5. Report

# Sub-TODO (Before 16 May)
1. Merge the code in 'towards' to have an Encoder
2. Create some target domains (with the same size)
3. Check the 'not-good' result and visualize
4. Add probe policy
5. Visualize
6. Make slide 
7. (Future work: Use GAN to generate target domain) 
8. (may explore the tranfer for different domains)

# Questions
1. Game suggestions for symbolic GAN

# Due date
1. Finish A3 questions (Q3 find paper) before 7 May
2. 10 May (week 10) prepare presentation
3. Presentation slide should be submitted by 4pm, 23 May
4. 24 May offline lecture presentation + May 26 tutorial presentaion

# Reference
### Symbolic: 
1. State of the art: https://github.com/taesungp/contrastive-unpaired-translation ISSUE: may not be compatible with the inverse GAN process<br>
2. Deep Feature Extraction for Sample-Efficient Reinforcement Learning: https://danielegrattarola.github.io/files/publications/2017_10_grattarola_master_thesis.pdf Chapter 4 <br>
3. Symbolic Reinforcement Learning with Common Sense: https://github.com/AimoreRRD/Reinforcement-Learning-Research

### Probe policy:
Single Episode Policy Transfer in Reinforcement Learning
https://arxiv.org/abs/1910.07719

### Possible RL techniques
1. Monte-Carlo Methods 
- model-free approaches, which means the target policy is optimized using samples of inter-actions with the environment, without requiring knowledge of the MDP’s transition dynamics. Monte-Carlo methods use samples of episodes to estimate the value of each state based on episodes starting from that state. Monte-Carlo methods can be off-policy, if the episodic samples are collected by a behavior policy which are different from the target policy considered by the current learning step. They can also be on-policy, when the samples are collected by following the target policy. Importance sampling is usually applied to the off-policy approaches in order to transform the expectation of returns from the behavior policy to the target policy [14], [15].
2. Temporal-Difference Learning, or TD-learning for short,
- an alternative to Monte-Carlo methods for solving the prediction problem. The key idea behind TD-learning is to learn the state quality function by bootstrapping, which means it updates its estimation of the function based on another estimation. It can also be extended to solve the control problem, so that both value function and policy can get improved. TD-learning is one of the most widely used RL frameworks due to its simplicity and general applicability.
Examples of on-policy TD-learning algorithms include SARSA [16], Expected SARSA [17], Actor-Critic [18] and its variant called A3C [19]. Examples of off-policy TD-leaning approaches are Q-learning [20] and its variants built with deep-neural networks, such as DQN [21], Double-DQN [21], and etc.

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
source /usr/local/anaconda3/etc/profile.d/conda.sh

conda create -n symbolenv python=3.6
```

### enter/exit virual environment
```
conda activate symbolenv

conda deactivate symbolenv
```

### install packages (!!watch out for `conda` and `pip`!!)
```
pip install pygame

pip install pandas==0.20.3

pip install xlrd==1.2.0

conda install matplotlib

conda install xlsxwriter
```

### for Copland computers
```
pip install gym

pip install tensorflow 

pip install scikit-image

pip install keras

pip install imageio

pip install sklearn

```
### run the plus and minus file
```
cd symblic_game/
python NEW_GAME.py
```
Press `G` to pause the game and plot graph. Close the graph to continue game playing.

### run the cross and circle file
```
cd PyDSRL/
python main.py
```
