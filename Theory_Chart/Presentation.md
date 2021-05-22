Silde 1:<br>
Hi, everyone! I am xxx, today I am going to present our project to you. We are a team of three girls, our team members are xx, xx, and me. Our project is called Symbolic Transfer in Games in Deep Reinforcement Learning, supervised by Katya.<br>
Slide 2: <br>
Let me introduce the main idea of our project: the aim of our project is to tranfer the knowledge we have gained from one game, which is on the left, to the game on the right. As you can see it, the original game on the left wants to hit as many 'plus' objects as possible, and at the same time, avoiding the 'triangles', which represent the obstacles. We want to figure out a good way for utilizing the experience we gained from the original game into the new game, where the positive and negative obejcts are replaced into totally new symbols, crosses and circles.<br>
Slide 3: <br>
Transfer learning reuses prior knowledge, resulting in shorter training time, less data requirement, and better performance in neural networks. And also, by automatically extract symbols from pixels in the images, we could gain the benefits of saving spatial complexity, adaptable for more complex scenarios, easier for human to understand, and also a certain effect for denoising.  
Silde 4: <br>
We mainly have two highlighted innovations in our project. The first one is that we apply an unsupervised auto-encoder to extract auto-types from the image pixels. And the second point is that we use a few-shot probing strategy to classify the auto-types into pos. and neg. types.Therefore, within the same game rules, we could turn different games into the same representation such that the prior knowledge could be reused. <br>
Slide 5: <br>
This graph shows our experimental result. The light blue line represents our transfer method's result. Compared with the other three lines, our method achieved higher cummulated reward at early episodes, proving that our transferred knowledge did accelerate the learning. If we compare the dark blue line with the orange line which both trained from scratch, with a classificcation by probing gained a much better performance. <br>
Due to the limited time, we only trained for 500 episodes for the experiment, and the performance was not yet stable at the end of the 500th episode.<br> 
Slide 6: <br>
If you're interesting in our topic, please come to our tutorial presentation on wednesday 3-5pm.<br>
Thank you for you attention. <br>



# Tutorial
That's why we introduce a novel method, combining the advantages of unsupervised symbol extraction, and the optimized probing strategy. Initially, we apply the auto-encoder to extract symbols from the pixels of the game images. That's when we get the auto-types according to their positions and pixel values. After that, we let our agent go along some trajectories on the game, generating the corresponding rewards. Based on the rewards, we classify the types into two main types, one with positive reward and the other with negative reward. And we train the original policy on the two types, and play the game according to our generated trajectory.
