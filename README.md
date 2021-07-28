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
1. [Towards deep symbolic reinforcement learning](https://arxiv.org/abs/1609.05518) Garnelo, M., Arulkumaran, K. and Shanahan, M., 2016.<br>
2. [Towards symbolic reinforcement learning with common sense](https://arxiv.org/abs/1804.08597) Garcez, A.D.A., Dutra, A.R.R. and Alonso, E., 2018.<br>
3. [Single Episode Policy Transfer in Reinforcement Learning](https://arxiv.org/abs/1910.07719) Yang, J., Petersen, B., Zha, H., & Faissol, D., 2019 <br>

## Contribution: 
1. [Contrastive Unpaired Translation (CUT)](https://github.com/taesungp/contrastive-unpaired-translation) <br>

<!-- 2. [Deep Feature Extraction for Sample-Efficient Reinforcement Learning: Chapter 4](https://danielegrattarola.github.io/files/publications/2017_10_grattarola_master_thesis.pdf ) <br> -->

2. [Symbolic Reinforcement Learning with Common Sense](https://github.com/AimoreRRD/Reinforcement-Learning-Research)<br>

3. [Why would symbolic AI be useful](https://innovature.ai/symbolic-artificial-intelligence/)<br>

4. [Symbolic game with autoencoder](https://github.com/ivegner/PyDSRL)<br>

## Contributor 
[Junming Zhang](https://github.com/flamingopink),[Taylor Qin](https://github.com/zishanqin),[Wei Zhou](https://github.com/weizhou1)

## License
This project is under the [MIT Licence](https://github.com/zishanqin/Symbolic-transfer/blob/main/LICENSE).
