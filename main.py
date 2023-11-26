import simpy
from red.agent import Agent
from red.topologia import NetworkTopology

def main():
    env = simpy.Environment()
    agents = [Agent(env, i) for i in range(10)]
    network = NetworkTopology(env, 10)
    env.run(until=30)

if __name__ == "__main__":
    main()
