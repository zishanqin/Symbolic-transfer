# Tutorial
### Slide 1: <br>
Hi, everyone! I am xxx, today I am going to present our project with junming. Our research topic is Symbolic Transfer in Games in Deep Reinforcement,supervised by Katya. The other team menmber is taylor. <br>


### SLide 2:
For the 15 minutes talk today, we are going to brief introduce our project mainly in these four sections.
What our project is, what method we used, how we did the experiment and some discussion about it.


### Slide 3: <br>
So let's have a look at the game that we are using for the project.
We have three different kinds of objects in our game, an agent, and a bunch of positive and negative objects.
We have our agent here in the middle of our game, our agent can move aound. 
The game rule is to hit as many positive object as possible, while avoiding the negative objects. Hit a positive object , we can gain one more score, but hit negative object , we would lose one score. <br> 


### Slide 4: <br>
So that was about our game. what's the goal of our project??<br>
We aim to transfer between games with similar rules but different symbols.<br>
Here is our source domain where the positive object is "plus" and negative object is "triangle".<br>
Here is our target domain where the positive object is "cross" and negative object is "circle".<br>

Our goal is to find an effective transfer method,
such that once the agent develops the strategy to gain more reward in source domain,
we can reuse the strategy in the target domain.


### Slide 5
So why is our research interesting?
It's because we integrate the idea of symbolic extraction into transfer learning in deep reinforcement learning.


### Slide 6
So transfer learning has several advantages. Most of the time if we train from scratch in reinforcement learning,
we would need quite a lot of training time and data to do exploration at the beginning.

However, if we use transfer learning, we can reuse the knowledge from the source task.
For example in this project we let the agent reuse the Q-value table,
so in the target task we have this Q-value table for the agent already,
and no need to train from the scratch.

Therefore we need less training time and less training data since we have Q-value table. <br>
In the target domain, our task essentially change from training from scrach to adapting previous knowledgage.  <br>
Therefore transfer learning allows us to achieve a good result at early training stage. <br>
In the further training, we can acheive better performance.


### Slide 7
So that was about transfer learning.
And here are the advantages for symbolic extraction.
The first one is that the learning procedure for the agent has much less spacial complexity.
The agent algorithm only need to take the entities and their positions as input, instead of matrix of pixels with RGB colours from the image.

Also if the symbol is of some very complicated pattern,the agent only see it as a type with coordinate.
Agnet does't care about if the symbol is a complicated shape or not.


And symbols are much easier for human to understand. We can understand the stradgy of agent better. It aslo help us to debug.


Symbol extraction also has some denoising effect.
Because symbolic extraction outputs the most significant features (or types), then the noise would be filtered out.
That was about the overview of our project, Now my team member junming will talk about what methos we use.

### Slide 8
Now let's have a look at what method we used to achieve our goal in the project.

This is the structure of what we've done.

So for the source game, we first use an unsupervised auto-encoder to extract auto-types from the image pixels,
then use probe policy to classify the auto-types to positive and negative symbols.
Then we train the agent, and obtain a policy based on the positive and negative symbols.

We do the same stuff for the target game as well. However here we have different-looking symbol,
but after the classification we get the same positives and negatives.
Now we can just reuse the policy from the source game.


### Slide 9
let's step through the structure. We first have a look what the auto-encoder does.


### Slide 10
For the auto-encoder, it first encode some major features from the image,
and then reconstruct from the encoded information.
We get the auto-types and their coordinates out of this procedure.


### Slide 11
That's what we get, on the right hand side, just some auto-types with the coordinates, out of one image.
We compressed the information of one image into these auto-types.

Now imagine you are an agent and you want to learn the environment, the left-hand side would be much more complicated,
It has a matrix of 84* 84 * 3, which is huge a lot of information.

Compared to the pixels on the right hand side, the input on the right hand side is much smaller for the agent, 
for each step of the learning and decision making.


### Slide 12
And here is the denoising effect of the auto-encoder.
We added some random noise at the left-bottom corner here.

As we can see on the right, after the extraction, we no-long have noise.
It's because the auto-encoder only extracts the most significant features out of an image,
therefore the noise would be filtered out.


### Slide 13
Let's move on to the probe policy now.

Because the auto-coder is essentially extracting the features out of the image,
so we don't know if an auto-type is pos. or neg.

Also we might give us more than one auto-types for one symbol. Or less when if the symbols are distributed crowdedly together.

So we not necessarily going to have a one-to-one correspondence for the auto-types and the symbols.

That's why we need to classify them.


### Slide 14
Let's see how we classify the auto-types.
For example, here is our agent. There are two auto-types next to it, both of them might belong to one symbol.
We keep a record for the total score of each auto-type.

### Slide 15
After the agent hit these two auto-types, we have a reward feedback +1,

### Slide 16
so we add +1 to both types.


### Slide 17
We let the agent to detect for a few episodes so it can collect a total score for each type.
And then we can classify the auto-types into positive and negatives.
That's how we classify the symbol.


### Slide 18
After the classification, the agent then can do the learning on the pos. and neg. symbols.


### Slide 19
Here we just used the classic Q-learning. And this is our Q-value table.
We use this formula to update the Q-value after each learning step,
and use this formula to decide which action to take each step for the agent.

The Q-value table here has type1 for the pos., and typ2 for the neg.
We can then reuse the table for the target domain because they are using the same symbol representation space, pos. and neg.


### Slide 20
We ran the game over four experiment setups.
The random agent,
the traditional symbolic agent without the probing classification,
the symbolic agent with classification (that is our source domain),
and then the target domain where we transferred the knowledge.

Each of the setup was ran for 500 training episodes, and the measurement is just the accumulated award over the recent 200 episodes.


### Slide 21
This is the result of training from scratch. Our classification step via probing policy.
Even without the transfer, we can see that the classification step significantly improves the performance of training.


### Slide 22
And as for the transferred result, we can see that there is a significant improvement when the training just got started.
So it shows that our transferred method did accelerate the learning.

To summerise, from our experiment, we can say that our tranfer method is successful.
And our classification method is also successful.

We have a few drawbacks of our experiment though:
we probably didn't train the agent long enough, so the result is not stable or converging yet.
And also, we were doing the experiment on the grid setup only. 
Where the distribution of the symbols are regular, but not a random distribution.


### Slide 23
So here are some proposals for our future work of our project.
We can continue on the random dustribution symbol setup indead of grid set up.
And we can add more different kinds of symbols to our games to make our project more general.
Also we are using only the classic tabular Q-learning algorithm, so we can try DQN or some other reinforcement learning algorithms in the future work, to see if it works better or not..
And we can run more training episodes for longer to have a more general result, to see if it converging not.


### Slide 24
We think it's a quite meaningful project, and we learnt a lot from it.
We learnt how to do research as a team, to communicate and cooperate with each other.
We learnt research methodologies, like reading papers, selecting research topics, understanding models etc.
And we also learnt some more technical concepts, such as symbolic extraction from images, and transfer learning in deep reinforcement learning.

We think it was a fantastic experience.


### Slide 25
That's all for our presentation. Any question?


### Q-learning function 
The update rule for the interaction between objects of types i and j is given by:<br>

where α is the learning rate, γ is a temporal discount factor, and each state sij represents an interaction t
between object types i and j at time t. After learning, the values of the Qij functions are added, and the action with the largest sum is chosen as shown in Equation 2.

