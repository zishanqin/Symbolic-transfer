## Lecture Pres.
### Silde 1:<br>
Hi, everyone! I am xxx, today I am going to present our project to you. <br>
Our team members are xx, xx, and me. <br>
We are team **num**. 
Our project is Symbolic Transfer in Games in Deep Reinforcement Learning, supervised by Katya. Thank you Katya.<br>
### Slide 2: <br>
The objective of our project is to tranfer the knowledge we have gained from the game on the left to the one on the right. <br>
The original game wants to hit as many 'plus' objects as possible, and at the same time, avoiding the 'triangles'. <br>
We aims to find a good way for reusing the experience we gained into a new game, where the positive and negative obejcts are replaced into new symbols, crosses and circles.<br>
### Slide 3: <br>
Why is our project interesting? <br>
Well it's because we integrate the symbolic extraction idea in transfer learning.<br>
Transfer learning could reuse previous knowledge, so we need less training time and data, and therefore better performance.<br>
Furthermore, since we're processing symbols instead of pixels, auto symbolic extraction brings us the benefits in spatial complexity, applicability, interpretability, and also a certain denoising effect.  <br>
### Silde 4: <br>
So this is the structure of our method. <br>
We mainly have two highlights here. <br>
The first one is that we apply an unsupervised auto-encoder to extract auto-types from the image pixels. <br>
The second one is that we use a few-shot probing strategy to classify the auto-types into pos. and neg. symbols. <br>
Thus, we represent different games applying the same game rules in one symbolic latent space, so that previous knowledge can be transferred and reused.<br>
### Slide 5: <br>
This is our experimental result on 500 episodes. <br>
The light blue line represents our transfer method's result.<br> 
Comparing to the other three lines, it achieved higher cummulated reward at early episodes, proving that our transferred knowledge did accelerate the learning. <br>
Comparing the dark blue line to the orange one, even though both are trained from scratch, classification by probing clearly obtained a better performance. <br>
However, our performance was not yet stable at the moment.<br> 
### Slide 6: <br>
That's all the introduction.<br> 
If you're interested in our project, please come to our tutorial presentation on wednesday 3-5pm.<br>
Thank you for your attention. <br>



# Tutorial
That's why we introduce a novel method, combining the advantages of unsupervised symbol extraction, and the optimized probing strategy. Initially, we apply the auto-encoder to extract symbols from the pixels of the game images. That's when we get the auto-types according to their positions and pixel values. After that, we let our agent go along some trajectories on the game, generating the corresponding rewards. Based on the rewards, we classify the types into two main types, one with positive reward and the other with negative reward. And we train the original policy on the two types, and play the game according to our generated trajectory.