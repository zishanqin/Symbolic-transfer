'''Main module for the paper's algorithm'''
#pylint:disable=C0103,R0913
import argparse
from collections import deque
import json
import os.path
import pickle
import numpy as np
import math
import tqdm

import gym
from gym import logger
from numpy.ma.core import left_shift, right_shift
from sklearn.model_selection import train_test_split
import tensorflow as tf

#pylint:disable=W0611
import cross_circle_gym
#pylint:enable=W0611
from components.autoencoder import SymbolAutoencoder
from components.state_builder import StateRepresentationBuilder
from components.agent import TabularAgent, DSRLAgent #, DDQNAgent

parser = argparse.ArgumentParser(description=None)
parser.add_argument('env_id', nargs='?', default='CrossCircle-MixedRand-v0',
                    help='Select the environment to run')
parser.add_argument('--load', type=str, help='load existing model from filename provided')
parser.add_argument('--episodes', '-e', type=int, default=1000,
                    help='number of DQN training episodes')
parser.add_argument('--load-train', action='store_true',
                    help='load existing model from filename provided and keep training')
parser.add_argument('--new-images', action='store_true', help='make new set of training images')
parser.add_argument('--enhancements', action='store_true',
                    help='activate own improvements over original paper')
parser.add_argument('--visualize', '--vis', action='store_true',
                    help='plot autoencoder input & output')
parser.add_argument('--save', type=str, help='save model to filename provided') # e.g. --save testsave.h5

args = parser.parse_args()

TRAIN_IMAGES_FILE = 'train_images.pkl'
NEIGHBOR_RADIUS = 25  # 1/2 side of square in which to search for neighbors

# You can set the level to logger.DEBUG or logger.WARN if you
# want to change the amount of output.
logger.setLevel(logger.INFO)



env = gym.make(args.env_id)
seed = env.seed(1)[0]


# ------- make training data for autoencoder -------
def make_autoencoder_train_data(num, min_entities=10, max_entities=30):
    '''Make training images for the autoencoder'''
    temp_env = gym.make('CrossCircle-MixedRand-v0')
    temp_env.seed(0)
    states = []
    for _ in range(num):
        states.append(temp_env.make_random_state(min_entities, max_entities))
    return np.asarray(states)


# generate images if no image exist yet
if not os.path.exists(TRAIN_IMAGES_FILE) or args.new_images:
    logger.info('Making test images...')
    images = make_autoencoder_train_data(10000, max_entities=30)
    with open(TRAIN_IMAGES_FILE, 'wb') as f:
        pickle.dump(images, f)
else:
    logger.info('Loading test images...')
    with open(TRAIN_IMAGES_FILE, 'rb') as f:
        images = pickle.load(f)


# -------- load saved model of autoencoder (or create) -------
#input_shape = images[0].shape + (1,)
input_shape = images[0].shape
if args.load:
    autoencoder = SymbolAutoencoder.from_saved(args.load,
                                               images[0].shape,
                                               neighbor_radius=NEIGHBOR_RADIUS)
else:
    autoencoder = SymbolAutoencoder(images[0].shape, neighbor_radius=NEIGHBOR_RADIUS)



# -------- train the autoencoder -------
if args.load_train or args.visualize or not args.load:
    logger.info('Splitting sets...')
    X_train, X_test = train_test_split(images, test_size=0.2, random_state=seed)
    X_train, X_val = train_test_split(X_train, test_size=0.2, random_state=seed)

    if args.load_train or not args.load:
        logger.info('Training...')
        autoencoder.train(X_train, epochs=50, validation=X_val)

    if args.visualize:
        #Visualize autoencoder
        vis_imgs = X_test[:10]
        autoencoder.visualize(vis_imgs)


# ------- save the autoencoder model -------
if args.save:
    autoencoder.save_weights(args.save)


# entities, found_types = autoencoder.get_entities(X_test[0])

state_builder = StateRepresentationBuilder()
# state = state_builder.build_state(entities, found_types)
# print(state)

# state_size = None # TODO


# ------- create a new model --------
action_size = env.action_space.n
# if args.enhancements:
#     agent = DDQNAgent(state_size, action_size)
# else:q


# agent = TabularAgent.from_saved("./tab_agent.h5", action_size)
# agent = TabularAgent(action_size, alpha=0.01, epsilon_decay=0.99995)
# agent = TabularAgent.from_saved("./tab_agent.h5", action_size)
agent = DSRLAgent()
# -------- load the saved agent model --------
done = False
batch_size = 32
time_steps = 100





# --------- probe policy ---------
#  TODO: Plug in the probe action function for probe episodes
#
TYPES = {}

def update_types(entities, reward, types):
    for entity in entities:
        overlap = (entity.position[0] - env.agent.centre()[0]) * (entity.position[1] - env.agent.centre()[1])
        if (overlap < 25):
            if entity.entity_type in types:
                types[entity.entity_type] += reward
            else:
                types[entity.entity_type] = reward
    return types


def env_step(action, entities, types):
    _, reward, _, _ = env.step(action)
    if reward != 0:
        types = update_types(entities, reward, types)
    return types



PROBE_EPO = 0
# ----------- identify TYPES -----------
for e in tqdm.tqdm(range(PROBE_EPO)):
    state_builder.restart()
    state = env.reset()
    state = np.reshape(state, input_shape)
    typed_entities, _ = autoencoder.get_entities(state)

    for entity in typed_entities:
        pos = entity.position * 2
        y_step = math.floor((pos[0] - env.agent.centre()[0])/10)
        x_step = math.floor((pos[1] - env.agent.centre()[1])/10)

        # step left ---
        if x_step < 0:
            action = 3 # left
        else:
            action = 1 # right
        for x in range(abs(x_step)):
            TYPES = env_step(action, typed_entities, TYPES)
            # env.render(wait=0.1)

        # step up |
        if y_step < 0:
            action = 2 # up
        else:
            action = 0 # down
        for x in range(abs(y_step)):
            TYPES = env_step(action, typed_entities, TYPES)
            # env.render(wait=0.1)

        # print([env.agent.left, env.agent.top])

print(TYPES)
# TYPES = {} finalised
for etype in TYPES:
    if TYPES[etype] > 0:
        TYPES[etype] = 'type1'
    elif TYPES[etype] < 0:
        TYPES[etype] = 'type2'
    elif TYPES[etype] == 0:
        TYPES[etype] = 'type3'




# SAVE types dictionary into json file
# a_file = open("types.json", "w")
# json.dump(TYPES, a_file)
# a_file.close()

# READ types dictrionay from json file
# TYPES = json.load(open("types.json"))
print(TYPES)


# ----------- train the agent with the autoencoder --------
# for e in range(args.episodes):
#     state_builder.restart()
#     state = env.reset()
#     state = np.reshape(state, input_shape)
#     state = state_builder.build_state(*autoencoder.get_entities(state))
#     score = 0
#     for time in range(time_steps):

#         # update the environment
#         env.render(wait=0.001)
#         action = agent.act(state, random_act=False)
#         next_state, reward, done, _ = env.step(action)
#         score += reward

#         # update the state representative by the symbolic representation
#         next_state = np.reshape(next_state, input_shape) # make it to img
#         # next_state = state_builder.build_state(*autoencoder.get_entities_new(next_state, TYPES))
#         next_state = state_builder.build_state(*autoencoder.get_entities(next_state))
#         agent.update(state, action, reward, next_state, done)
#         # print(state_builder.type_transition_matx.index)

#         state = next_state
#         if done:
#             break
#     # if args.enhancements:
#     #     agent.update_target_model()
#     print('episode: {}/{},'.format(e, args.episodes, agent.epsilon))
#     print("current ep score:", score)

#     # if len(agent.memory) > batch_size:
#     #     agent.replay(batch_size)
#     if e % 10 == 0:
#         agent.save('tab_agent.h5')




number_of_evaluations = 0
buffered_rewards = deque(maxlen=200)
summary_writer = tf.summary.create_file_writer('./logs')


for e in tqdm.tqdm(range(args.episodes)):
    state_builder.restart()
    state = env.reset()
    state = state_builder.build_state(*autoencoder.get_entities(state))
    total_reward = 0
    estate = state_builder.tracked_entities

    for t in range(time_steps):
        env.render(wait=0.001)
        # action = agent.act(state)
        action = agent.act(entities=estate, s_prob=0.3)
        next_state, reward, done, _ = env.step(action)
        total_reward += reward

        next_state = state_builder.build_state(*autoencoder.get_entities(next_state))
        next_estate = state_builder.tracked_entities
        agent.update(estate, action, next_estate, reward, env.agent.centre(), done)
        # agent.update(state, action, reward, next_state, done)
        state = next_state

        if done:
            print("Total reward of this ep:", total_reward)
            break

    buffered_rewards.append(total_reward)

    with summary_writer.as_default():
        tf.summary.scalar('Averaged Reward',np.mean(buffered_rewards),e)
        tf.summary.scalar('Epsilon',agent.epsilon,e)

    if e % 50 == 0:
        number_of_evaluations += 1
        # agent.save('tab_agent.h5')
        evaluation_reward = []
        with summary_writer.as_default():
            for i in range(10):
                done = False
                state_builder.restart()
                image = env.reset()
                state = state_builder.build_state(*autoencoder.get_entities(image, TYPES))
                estate = state_builder.tracked_entities
                total_reward = 0
                for t in range(time_steps):
                    env.render(wait=0.001)
                    action = agent.act(estate, 0, random_act=False)
                    # action = agent.act(state,random_act=False)
                    next_image, reward, done, _ = env.step(action)
                    if i==0:
                        tf.summary.image(f'Agent Behaviour {number_of_evaluations}',np.reshape(image,(1,)+image.shape),t)
                    total_reward += reward
                    next_state = state_builder.build_state(*autoencoder.get_entities(next_image))
                    state = next_state
                    image = next_image
                evaluation_reward.append(total_reward)

            tf.summary.scalar('Evaluation Reward',np.mean(evaluation_reward),number_of_evaluations)