from cross_circle_gym.envs.test_base import CrossCircleBase

class TestMixedGrid(CrossCircleBase):
    '''Environment providing a grid of circles (negative rewards)'''

    def setup_field(self):
        self.layout(random=False, mixed=True)