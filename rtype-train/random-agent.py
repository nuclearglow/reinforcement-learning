import retro
import os
import matplotlib.pyplot as plt

# Get path of script
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))


#def main():

# Add custom integration
retro.data.Integrations.add_custom_path(
            os.path.join(SCRIPT_DIR, "scenarios")
    )

# Create gym environment with retro using custom integration
print("scenario1" in retro.data.list_games(inttype=retro.data.Integrations.ALL))
env = retro.make("scenario1", inttype=retro.data.Integrations.ALL)
print(env)

# Reset environment
obs = env.reset()


rews = []
# Loop...
for t in range(1000):
    obs, rew, done, info = env.step(env.action_space.sample())
    rews.append(rew)
    #env.render()
    if done:
        obs = env.reset()
env.close()

print(rews)

# Plot obs
a = plt.imshow(obs[:,:,0], cmap='gray')
b = plt.imshow(obs[:,:,1], cmap='gray')
c = plt.imshow(obs[:,:,2], cmap='gray')

# Loop...
# while True:
#     obs, rew, done, info = env.step(env.action_space.sample())
#     env.render()
#     if done:
#         obs = env.reset()
# env.close()


#if __name__ == "__main__":
#    main()
