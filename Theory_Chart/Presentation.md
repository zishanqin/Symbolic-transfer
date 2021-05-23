## Lecture Pres.
### Silde 1:<br>
Hi, everyone! Here is group **14**. I am Taylor.<br> 
Today I am going to present our project, **Symbolic Transfer in Games** in Deep Reinforcement Learning, to you. <br>
Our team members are Junming, Wei, and me. And this project was supervised by Katya. Thank you Katya.<br>
### Slide 2: <br>
The **goal of our project** is to **tranfer the knowledge** , from the game on the left, <br>
to the game on the right. <br>
The original game wants to hit as many **'plus' objects** as possible, while avoiding the 'triangles'. <br>
We aim to find an **efficient** way to **reuse** the training experience, in a new game, <br>
where the positive and negative objects are **replaced** into new symbols, <br>
crosses and circles.<br>
### Slide 3: <br>
So why is our project interesting? <br>
Well it's because we **integrate** the auto symbolic extraction idea in **transfer learning**.<br>
Transfer learning could **reuse** previous knowledge, so we need **less data**, **less training time**, <br>
and **better performance**.<br>
Furthermore, since we're processing **symbols** instead of image pixels, <br>
symbolic extraction also brings us benefits, <br>
such as **readability, spatial complexity, and applicability**. <br>
And it works better with noise.  <br>
### Silde 4: <br>
So this is the **structure** of our method. <br>
We mainly have **two** innovative ideas: <br>
The first one is an **unsupervised** auto-encoder to get **auto-types** from the image pixels; <br>
The second one is a few-shot **probing** strategy to classify the **auto-types** into pos. and neg. symbols. <br>
Therefore, we represent different games in **one symbolic** latent space, <br>
so that previous knowledge can be transferred and reused.<br>
### Slide 5: <br>
This is our result in the first 500 episodes, although it is not yet converged. <br>
The **cyan** (si-an) line represents our **transfer** method's result.<br> 
Comparing to the other three lines, it achieved **higher** reward **at early** episodes. <br>
It indicates that our **transferre**d knowledge **did** accelerate the learning. <br>
Comparing the **dark** blue line, to the **orange** one, <br>
even though both are trained from **scratch**, <br>
classification clearly obtained a **better** performance. <br>
### Slide 6: <br>
Well, that's all of the introduction for our project.<br> 
If you're **interested**, please come to our tutorial presentation on wednesday 3-5pm in the afternoon.<br>
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
