from fake_env import FakeEnv
api_key: str = "123123123"
project_name: str = "aaaa"
workspace: str = "zzzzz"

config = {"api_key": api_key,"project_name": project_name,"workspace": workspace}


env = FakeEnv(config)
ml_logger = env.comet_logger

# Gathering samples
count = 0
for epoch in range(10):  # 500 epochs
    for i in range(10):  # 500 steps per epoch
        reward = env.step(0)
        ml_logger.log_metrics({"test":   reward, "step": count})
    if epoch % 100 == 0:
        print("Gathering experiment results")
    count += 1

# Actual training
ml_logger.set_step(0)

count = 0
for epoch_i in range(11):
    for step_i in range(11):
        reward = env.step(None)
        ml_logger.log_metrics({"reward":   reward, "step": count})
        print("Logged to comet")
print("Done")
