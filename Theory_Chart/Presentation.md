## Lecture Pres.
### Silde 1:<br>
Hi, everyone! Here is group **num**. <br>
I am Taylor Qin, today I am going to present our project, Symbolic Transfer in Games in Deep Reinforcement Learning, to you. <br>
Our team members are Junming, Wei, and me. And this project was supervised by Katya. Thank you Katya.<br>
### Slide 2: <br>
The goal of our project is to tranfer the knowledge we have gained, from the game on the left, to the one on the right. <br>
The original game wants to hit as many 'plus' objects as possible, and to avoid the 'triangles'. <br>
We aim to find an efficient way to reuse the experience we gained before, in a new game, where the positive and negative obejcts are replaced into new symbols, crosses and circles on the right.<br>
### Slide 3: <br>
So why is our project interesting? <br>
Well it's because we integrate the symbolic extraction idea in transfer learning.<br>
Transfer learning could reuse previous knowledge, so we need less training time and data, and therefore better performance.<br>
Furthermore, since we're processing symbols instead of pixels, auto symbolic extraction brings us the benefits in spatial complexity, applicability, interpretability, and also a certain denoising effect.  <br>
### Silde 4: <br>
So this is the structure of our method. We mainly have two highlights here. <br>
The first one is that we apply an unsupervised auto-encoder to extract auto-types from the image pixels. <br>
The second one is that we use a few-shot probing strategy to classify the auto-types into pos. and neg. symbols. <br>
Thus, we represent different games applying the same game rules in one symbolic latent space, so that previous knowledge can be transferred and reused.<br>
### Slide 5: <br>
This is our experimental result on 500 episodes. <br>
The light blue line represents our transfer method's result.<br> 
Comparing to the other three lines, it achieved higher cummulated reward at early episodes, showing that our transferred knowledge did accelerate the learning. <br>
Comparing the dark blue line, to the orange one, even though both are trained from scratch, classification by probing clearly obtained a better performance. <br>
However, our performance was not yet stable at the moment.<br> 
### Slide 6: <br>
Well, that's all of the introduction for our project.<br> 
If you're interested, please come to our tutorial presentation on wednesday 3-5pm.<br>
Thank you for your attention. <br>



# Tutorial
### Slide 1: <br>
Hi, everyone! I am xxx, today I am going to present our project to you. <br>
Our team members are xx, xx, and me. <br>
Our reseach topic is Symbolic Transfer in Games in Deep Reinforcement Learning, supervised by Katya. Thank you Katya.<br>
### Slide 2: <br>
So let's have a look at the game that we are using for the project. The game rule is to hit as many as positive object as possible, while avoiding the negative objects. 指ppt上的 Agent，Postive 和 Negative.<br> 介绍正负reward。
### Slide 3: <br>
So that's our game. what's the goal of our project??<br>
We aim to transfer between games with simialr rules but different symbols.<br>
Here is our source domain where the postive object is "plus" and negetive object is "triangle".<br>
Here is our target domain where the postive object is "cross" and negetive object is "circle".<br>
Our goal is to find an effective transfer method such that once the agent develeops the strategy to gain more reward in source domain, we can reuse the strategy in the target domain. Where the target domain has different symbol representation.  
### Slide 4: <br>



That's why we introduce a novel method, combining the advantages of unsupervised symbol extraction, and the optimized probing strategy. Initially, we apply the auto-encoder to extract symbols from the pixels of the game images. That's when we get the auto-types according to their positions and pixel values. After that, we let our agent go along some trajectories on the game, generating the corresponding rewards. Based on the rewards, we classify the types into two main types, one with positive reward and the other with negative reward. And we train the original policy on the two types, and play the game according to our generated trajectory.
