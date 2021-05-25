# Tutorial
### Slide 1: <br>
Hi, everyone! I am xxx, Our team members are xx, xx, and me.
Today we are going to present our project.
Our reseach topic is Symbolic Transfer in Games in Deep Reinforcement Learning, supervised by Katya. <br>


### SLide 2:
For the 15 minutes talk today, we are going to brief introduce our project mainly in these four sections.
What our project is, what method we used, how we did the experiment and some discussion about it.


### Slide 3: <br>
So let's have a look at the game that we are using for the project.
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
we would need quite a lot of training time and data to do exploration in the beginning.

However, if we use transfer learning, we can reuse the knowledge from the source task.
For example in this project we let the agent reuse the Q-value table,
so in the target task we have this Q-value table for the agent already,
and no need to train from the scratch.

Therefore we need less training time and less training data since we have Q-value table.
In the target domain, our task essentially change from training from scrach to adapting previous knowledgage. 
And this allows us to achieve a good result at early training stage.
We can train further to improve the performance.


### Slide 7
So that was about transfer learning.
And here are the advantages for symbolic extraction.
The first one is that the learning procedure for the agent has much less spacial complexity.
The agent algorithm only need to take the entities and their positions as input, instead of a whole 100 by 100 pixels from the image.

Also if the symbol is of some very complicated pattern, for the agent it would be just a coordinate with a type.
We don't care about if the symbol is a complicated shape or not.

And symbols are much easier for human to understand, about how the learning actually works.
If it's an algorithm about image pixels it would be almost impossible for human to understand what is going on with the learning.

It also has some denoising effect.
Because symbolic extraction outputs the most significant features (or types), then the noise would be filtered out.


### Slide 8
So for the source game, we first use the auto-encoder to extract auto-types from the image pixels,
then use probe policy to classify the auto-types to positive and negative symbols.
Then we train the reinforcement learning algorithm, and obtain a policy based on the positive and negative symbols.

We do the same stuff for the target game as well. So here we have different-looking symbol,
but after the classification we get the same positives and negatives.
Now we can just reuse the policy from the source game.


### Slide 9
So now let's have a look at how it actually works.


### Slide 10
Here is what the auto-encoder does. It first encode some major features from the image,
and then reconstruct from the encoded information.
We get the auto-types and their coordinates out of this procedure.


### Slide 11
That's what we get, on the right hand side, just some auto-types with the coordinates.
Compared to the pixels, the input for the agent is much less, for each step of the learning and decision making.


### Slide 12
And here is the denoising effect.
If we add some random noise at the corner here, the auto-encoder would filter them out when extracting the symbols.


### Slide 13
Let's move on to the probe policy now.
After we got the auto-types from the auto-encoder, we use the probe policy to classify them into positive and negative symbols.
Because the auto-coder is essentially extracting the feature patterns out of the image,
so it might give us more than one auto-types for one symbol. Or less when it comes to dense areas.
So we not necessarily going to have a one-to-one correspondence for the auto-types and the pos. and neg. symbols.
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

We can then reuse the table for the target domain because they are using the same symbol representation space, pos. and neg.


### Slide 20
We ran the game over four experiment setups.
The random agent,
the traditional symbolic agent without the probing classification,
the symbolic agent with classification (that is our source domain),
and then the target domain where we transferred the knowledge.

Each of the setup was ran for 500 training episodes, and the measurement is just the accumulated award over the recent 200 episodes.


### Slide 21
This is the result of training from scratch.
Even without the transfer, we can see that the classification step significantly improves the performance of training.


### Slide 22
And as for the transferred result, there is a significant improvement when the training just got started.
So it shows that our transferred method did accelerate the learning.

We have a few drawbacks of our experiment though:
we probably didn't train the agent long enough, so the result is not stable or converging yet.
And we were also doing the experiment on the grid setup only.


### Slide 23
So here are some proposals for our future work of our project.
We can continue on the random symbol setup.
And we can add more different kinds of symbols to our games.
Also we are using only the classic tabular Q-learning algorithm, so we can try DQN or some other reinforcement learning algorithms in the future work.
And we run more training episodes for longer to have a more general result.



### Slide 24
We think it's a quite meaningful project, and we learnt a lot from it.
We learnt how to do research as a team, to communicate and cooperate with each other.
We learnt research methodologies, like reading papers, selecting research topics, understanding models etc.
And we also learnt some more technical concepts, such as symbolic extraction from images, and transfer learning in deep reinforcement learning.

We think it was a fantastic experience.


### Slide 25
That's all for our presentation. Any question?