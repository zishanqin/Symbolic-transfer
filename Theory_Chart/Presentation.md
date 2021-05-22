Silde 1:<br>
Hi, everyone! I am xxx, today I am going to present our project to you. We are a team of three girls, our team members are xx, xx, and me. Our project is called Symbolic Transfer in Games in Deep Reinforcement Learning, supervised by Katya.<br>
Slide 2: <br>
Let me introduce the main idea of our project: the aim of our project is to tranfer the knowledge we have gained from one game, which is on the left, to the game on the right. As you can see it, the original game on the left wants to hit as many 'plus' objects as possible, and at the same time, avoiding the 'triangles', which represent the obstacles. We want to figure out a good way for utilizing the experience we gained from the original game into the new game, where the positive and negative obejcts are replaced into totally new symbols, crosses and circles.<br>
Slide 3: <br>
Transfer learning reuses prior knowledge, resulting in shorter training time, less data requirement, and better performance in neural networks. And also, by automatically extract symbols from pixels in the images, we could gain the benefits of saving spatial complexity, adaptable for more complex scenarios, easier for human to understand, and also a certain effect for denoising.  
Silde 4: <br>
That's why we introduce a novel method, combining the advantages of unsupervised symbol extraction, and the optimized probing strategy. Initially, we apply the auto-encoder to extract symbols from the pixels of the game images. That's when we get the auto-types according to their positions and pixel values. After that, we let our agent go along some trajectories on the game, generating the corresponding rewards. Based on the rewards, we classify the types into two main types, one with positive reward and the other with negative reward. And we train the original policy on the two types, and play the game according to our generated trajectory.<br>
Slide 5: <br>
The result of both classfication and transfer methods turned out to be pretty good, proving that our proposed method is useful. 
The classification significantly improves training efficiency, and transfer method accelarates the learning speed.
But the performance is not stable enough. 

If you're interesting in our topic, please come to our tutorial presentation on wednesday 3-5pm.
Thank you for you attention. 
