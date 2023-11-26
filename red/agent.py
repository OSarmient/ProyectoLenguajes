import simpy
import random

class Agent:
    def __init__(self, env, identificador):
        self.env = env
        self.id = identificador
        self.env.process(self.run())

    def run(self):
        while True:
            # Lógica del agente
            print(f"Agente {self.id} realizando acciones en el tiempo {self.env.now}")
            yield self.env.timeout(random.randint(1, 5))
