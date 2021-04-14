# RL-GAN: Transfer Learning for Related Reinforcement Learning Tasks via Image-to-Image Translation
RL-GAN is an official implementation of the paper: Transfer Learning for Related Reinforcement Learning Tasks via Image-to-Image Translation.

## Paper
[Shani Gamrian, Yoav Goldberg, "Transfer Learning for Related Reinforcement Learning Tasks via Image-to-Image Translation"](https://arxiv.org/abs/1806.07377)

```
@article{DBLP:journals/corr/abs-1806-07377,
  author    = {Shani Gamrian and
               Yoav Goldberg},
  title     = {Transfer Learning for Related Reinforcement Learning Tasks via Image-to-Image
               Translation},
  journal   = {CoRR},
  volume    = {abs/1806.07377},
  year      = {2018},
  url       = {http://arxiv.org/abs/1806.07377},
  archivePrefix = {arXiv},
  eprint    = {1806.07377},
  timestamp = {Mon, 13 Aug 2018 16:48:23 +0200},
  biburl    = {https://dblp.org/rec/bib/journals/corr/abs-1806-07377},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
```

### Videos:

[Breakout](https://youtu.be/4mnkzYyXMn4)

[RoadFighter](https://youtu.be/KCGTrQi6Ogo)

## Installation
- The code was tested on Ubuntu 16.04 with Python 3.6
- Install packages by typing the command: `pip install -r requirements.txt`.
- For Road Fighter, clone and install the repo: https://github.com/ShaniGam/retro

## Getting Started
### Breakout Examples
- Train Breakout from scratch:
```
python -m breakout_a3c.main --num-processes 32 --variation 'standart'
```
- Transfer from standart to diagonals variation and fine-tune the model:
```
python -m breakout_a3c.main --num-processes 32 --variation diagonals --ft-setting full-ft --test
```

- Collect images for UNIT training:
```
python -m breakout_a3c.main --collect-images --num-collected-imgs 100000 --variation diagonals --num-processes 1
```
- Train UNIT:
```
python -m unit.train --trainer UNIT --config unit/configs/breakout-diagonals.yaml
```
- Run Breakout with UNIT:
```
python -m breakout_a3c.main --variation diagonals --test --ft-setting full-ft --test-gan --gan-dir breakout-diagonals --num-processes 0
```

### Road Fighter Examples
- Train level 1 of Road Fighter
```
python -m roadfighter_a2c.main --num-processes 84
```

- Collect images for UNIT training:
```
python -m roadfighter_a2c.main -level 1 --collect-images --num-collected-imgs 100000 --num-processes 1
python -m roadfighter_a2c.main -level 2 --collect-images --num-collected-imgs 100000 --num-processes 1
```
- Train UNIT:
```
python -m unit.train --trainer UNIT --config unit/configs/roadfighter-lvl2.yaml
```
- Run Road Fighter with UNIT:
```
python -m roadfighter_a2c.main --load --level 2 --test-gan --gan-dir roadfighter-lvl2-kl01 --num-processes 1
```

- Run Road Fighter with UNIT and Imitation Learning:
```
python -m roadfighter_a2c.main_imitation --load --gan-dir roadfighter-lvl2-kl01 --gan-imitation-file '00320000' --log-name lvl2.log --super-during-rl --level 2 --det-score 5350
```

### Acknowledgments
The code was written by Shani Gamrian and is based on the repositories: [pytorch-a3c](https://github.com/ikostrikov/pytorch-a3c), [pytorch-a2c](https://github.com/ikostrikov/pytorch-a2c-ppo-acktr), [UNIT](https://github.com/mingyuliutw/UNIT)

### TO-DO
- Add links for pretrained models.
- Create videos.
