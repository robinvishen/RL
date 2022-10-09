import gym

env = gym.make("MountainCar-v0")
env.reset()

done = False

while not done:
   action = 2
   # print(env.step(action))
   # np.array(self.state, dtype=np.float32), reward, terminated, False, {} = env.step(action)
   new_state, reward, status, done, _ = env.step(action)
   env.render()

env.close()
