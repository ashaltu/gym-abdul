from gym.envs.registration import register

register(
    id='abdul-v0',
    entry_point='gym_abdul.envs:AbdulEnv',
    kwargs = {'new_variables': False}
)