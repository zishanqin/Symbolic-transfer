# Symbolic Transfer in Games in DRL

 
In our project, our objective is to find an effective way to transfer knowledge between games with similar rules but different object representations. We denote the game that provides the knowledge as the ‘source game’, and the game that accepts the knowledge as the ‘target game’. The experience we gain by playing games in the source-game is stored as knowledge and would be transferred to the target game via our transfer method. 

![](https://github.com/zishanqin/Symbolic-transfer/blob/main/img/gameDisplay.png)
**Remark.** The left-hand-side game is the source domain, from which we gain the policy. The one on the right is the target domain, the one that uses the transferred policy for playing. 

We specifically selected the above source game and the target game for our project, as shown in the figure. In the source game on the left-hand-side, the positive objects are the plus signs, and the negative objects are the triangles. In the target game on the right-hand-side, the positive objects are the crosses; and the negatives objects are the circles. Our agent is marked as the diamond sign in both games. 

A Deep Reinforcement Learning (DRL) auto-agent reads the image pixels of the game as input and decides the movement action. To summarize, we aim to find a transfer method such that: if a ‘smart’ DRL agent knows how to move to achieve a best reward in the source game, then it should know how to play in the target game as well. 

## Game Rule
The rule of both source and target are the same. The agent is allowed to move around in the 84×84 2D-grid-space, while the other objects are fixed. The goal is to have the agent hit as many positive objects as possible, while avoid hitting negative symbols during the motion. Once the agent hits a positive object, one point is added to the game's score; if the agent hits a negative object, one point is deducted from the total score.  

## Installation

### Enter GPU if you are an ANU student
```
ssh uID@stugpu2.anu.edu.au
```
### Create conda virtual env
```
source /usr/local/anaconda3/etc/profile.d/conda.sh

conda create -n symbolenv python=3.6
```

### Enter/exit virual environment
```
conda activate symbolenv

conda deactivate symbolenv
```

### Install packages (!!watch out for `conda` and `pip`!!)
```
pip install pygame

pip install pandas==0.20.3

pip install xlrd==1.2.0

conda install matplotlib

conda install xlsxwriter
```

### Once-off installation for Copland computers (should be run inside the vscode terminal)
```
pip install gym

pip install tensorflow 

pip install scikit-image

pip install keras

pip install imageio

pip install sklearn

pip install tqdm
```
### Run the plus and minus file
```
cd symblic_game/

python NEW_GAME.py
```
Press `G` to pause the game and plot graph. Close the graph to continue game playing.

### Run the cross and circle file
```
cd PyDSRL/

python main.py
```
### Solve error for cross and circle file
```
pip list | grep tf

pip install tensorflow --upgrade --force-reinstall
```

## Previous Tut Presentation url
Tut W11: https://youtu.be/6pULjybU8aU<br>
Tut W10: https://youtu.be/i5gWM5KYeR8<br>
Tut W9: https://youtu.be/JaT9m5BhNh4<br>
Tut W8: https://youtu.be/r4dzfbB_w8Y<br>
Tut W7: https://youtu.be/r4mUwgBTt0k

## Reference
### Symbolic: 
1. State of the art: https://github.com/taesungp/contrastive-unpaired-translation ISSUE: may not be compatible with the inverse GAN process<br>

2.[Report: Deep Feature Extraction for Sample-Efficient Reinforcement Learning: Chapter 4 (https://danielegrattarola.github.io/files/publications/2017_10_grattarola_master_thesis.pdf ) <br>

3.[Report:Symbolic Reinforcement Learning with Common Sense](https://github.com/AimoreRRD/Reinforcement-Learning-Research)<br>
4. Why would symbolic AI be useful: https://innovature.ai/symbolic-artificial-intelligence/

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


