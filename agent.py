'''
MIT License

Copyright (c) 2017 Keon Kim

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

SOURCE: https://github.com/keon/deep-q-learning/blob/master/ddqn.py
'''
import pickle
import random
import pandas as pd
import numpy as np

actions = ['up', 'down', 'right', 'left']
actions_dict = {'up':0, 'down':1, 'right':2, 'left':3}


class Obj:
    def __init__(self, tp, loc):
        self.tp = tp
        self.loc = loc


class DSRLAgent():
    def __init__(self):
        m_index = pd.MultiIndex(levels=[[''], [""]],
                                labels=[[], []],
                                names=['state', 'actions'])
        # tabular q-value
        self.model = pd.DataFrame(index=m_index)
        # inital position of the agent
        self.pos = [50.0, 50.0]
        self.pre_pos = [50.0, 50.0]
        self.alfa = 1
        self.gamma = 0.9

    def relation_obj_list(self, entities):
        rel_list = []
        xA = self.pos[0]
        yA = self.pos[1]
        # print("xA", xA)
        # print("yA", yA)
        for entity in entities:
            xB = entity.position[0]*2
            yB = entity.position[1]*2
            x = xA - xB
            y = yA - yB
            loc_dif = (x, y)
            # loc_dif = (x[0], y[0])
            tp = entity.entity_type
            obj = Obj(tp, loc_dif)
            rel_list.append(obj)
        return rel_list


    def act(self, entities, s_prob, random_act=True):
        x = random.random()  # E greedy exploration
        if (x < s_prob) and (random_act):
            n_action = random.choice(actions)
            print('Random Act:')
            return actions_dict[n_action]
        else:
            print('Chosen Act:')

        a_v_list = []
        d = {}
        rel_list = self.relation_obj_list(entities)
        new_state = rel_list

        for obj in new_state: # FOR ALL OBJECTS SEEN
            tp_n_c = str(obj.tp) # GET THE TYPE FROM THE NEW STATE
            s_n_c = str(obj.loc) # GET THE LOCATION FROM THE NEW STATE
            if tp_n_c not in self.model.columns:
                # print("tp_n_c not in model.columns", tp_n_c)
                self.model[tp_n_c] = 0
            if s_n_c not in self.model.index:
                # print("s_n_c not in model.index", s_n_c)
                m_index = pd.MultiIndex(levels=[[s_n_c], actions],
                                        labels=[[0, 0, 0, 0], [0, 1, 2, 3]],
                                        names=['state', 'actions'])
                df_zero = pd.DataFrame(index=m_index)
                self.model = self.model.append(df_zero)
                self.model = self.model.fillna(0)

            Qts_a = self.model[tp_n_c].loc[s_n_c]
            a_v = [(value, key) for value, key in Qts_a.items()]
            # print("Qts_a - NEW", Qts_a)
            a_v_list.append(a_v) # Append Q-value

            for element in a_v_list:
                for a in element:
                    act = a[0] # Action
                    val = a[1] # Value
                    d[act] = d.get(act, 0) + val # Sum values for each Q

            if d != {}: # BE CAREFUL THIS IS A DICT (argmax does not work as usual)
                inverse = [(value, key) for key, value in d.items()] # CALCULATE ALL KEYS
                n_action = max(inverse)[1] # Choose the max argument

                if max(d.values()) == 0: zero = True
            else:
                n_action = "down"

            print(n_action)
            return actions_dict[n_action]


    # state: tracked entities
    def update(self, state_t, action, state_t1, reward, new_pos, done):
        '''update the Q-value table'''
        max_value = 0
        action = str(action)

        rel_list = self.relation_obj_list(state_t)
        old_state = rel_list

        self.pos = new_pos
        rel_list = self.relation_obj_list(state_t1)
        new_state = rel_list

        for i in range(len(old_state)):
            # Check all items in old state
            obj_prev = old_state[i]
            tp_prev = str(obj_prev.tp)
            s_prev = str(obj_prev.loc)
            # Check all items in new state
            obj_new = new_state[i]
            tp_new = str(obj_new.tp)
            s_new = str(obj_new.loc)

            if tp_new not in self.model.columns: # If type is new, then add type
                self.model[tp_new] = 0
            if s_new not in self.model.index: # If state is new, then add state
                m_index = pd.MultiIndex(levels=[[s_new], actions],
                                        labels=[[0, 0, 0, 0], [0, 1, 2, 3]],
                                        names=['state', 'actions'])
                df_zero = pd.DataFrame(index=m_index)
                self.model = self.model.append(df_zero)
                self.model = self.model.fillna(0)

            max_value = max(self.model[tp_new].loc[s_new])
            if done == False:
                Q_v = self.model[tp_prev].loc[s_prev, action]
                self.model[tp_prev].loc[s_prev, action] = Q_v + self.alfa * (reward + (self.gamma * max_value) - Q_v)
            else:
                self.model[tp_prev].loc[s_prev, action] = reward



class TabularAgent:
    '''RL agent as described in the DSRL paper'''
    def __init__(self, action_size, alpha, epsilon_decay, neighbor_radius=25):
        self.action_size = action_size
        self.alpha = alpha
        self.epsilon = 1
        self.epsilon_decay = epsilon_decay
        self.epsilon_min = 0.1
        self.gamma = 0.95
        self.neighbor_radius=neighbor_radius
        self.offset = neighbor_radius*2
        self.tables = {}

    def act(self, state, random_act=True):
        '''
        Determines action to take based on given state
        State: Array of interactions
               (entities in each interaction are presorted by type for consistency)
        Returns: action to take, chosen e-greedily
        '''
        if not random_act:
            action = np.argmax(self._total_rewards(state))
            #print("choosen action:", action)
            return action

        if np.random.rand() <= self.epsilon:
            #print('random action, e:', self.epsilon)
            if self.epsilon > self.epsilon_min:
                self.epsilon *= self.epsilon_decay
            action = random.randrange(self.action_size)
            #print("random action:", action)
            return action

        if self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decay
        action = np.argmax(self._total_rewards(state))
        #print("choosen action:", action)
        return action  # returns action

    def update(self, state, action, reward, next_state, done):
        '''Update tables based on reward and action taken'''
        for interaction in state:
            type_1, type_2 = interaction['types_before'] # TODO resolve: should this too be types_before?
            table = self.tables.setdefault(type_1, {}).setdefault(type_2, self._make_table())
            id1,id2 = interaction['interaction']
            interaction_next_state = [inter for inter in next_state if inter['interaction']==(id1,id2)]
            if len(interaction_next_state) == 0:
                continue
            elif len(interaction_next_state)>1:
                raise ValueError('This should not happen')
            else:
                # update Q-value
                interaction_next_state = interaction_next_state[0]
                interaction['loc_difference'] = \
                (interaction['loc_difference'][0]+self.offset,interaction['loc_difference'][1]+self.offset)
                interaction_next_state['loc_difference'] = \
                (interaction_next_state['loc_difference'][0]+self.offset,interaction_next_state['loc_difference'][1]+self.offset)
                next_action_value = table[interaction_next_state['loc_difference']]
                if done:
                    table[interaction['loc_difference']][action] = reward
                else:
                    table[interaction['loc_difference']][action] += \
                     self.alpha*(reward + self.gamma * np.max(next_action_value) - table[interaction['loc_difference']][action])


    def _total_rewards(self, interactions):
        action_rewards = np.zeros(self.action_size)
        for interaction in interactions:
            type_1, type_2 = interaction['types_before']
            table = self.tables.setdefault(type_1, {}).setdefault(type_2, self._make_table())
            action_rewards += table[interaction['loc_difference']]  # add q-value arrays
        return action_rewards

    def _make_table(self):
        '''
        Makes table for q-learning
        3-D table: rows = loc_difference_x, cols = loc_difference_y, z = q-values for actions
        Rows and cols added to as needed
        '''
        return np.zeros((self.neighbor_radius * 8, self.neighbor_radius * 8, self.action_size),
                        dtype=float)

    def save(self, filename):
        '''Save agent's tables'''
        with open(filename, 'wb') as f_p:
            pickle.dump(self.tables, f_p)

    @staticmethod
    def from_saved(filename, action_size):
        '''Load agent from filename'''
        with open(filename, 'rb') as f_p:
            tables = pickle.load(f_p)
            ret = TabularAgent(action_size, alpha=0.01, epsilon_decay=0.99995)
            assert len(list(list(tables.values())[0].values())[0][0, 0]) == action_size, \
                   'Action size given to from_saved doesn\'t match the one in the tables'
            ret.tables = tables
        return ret
