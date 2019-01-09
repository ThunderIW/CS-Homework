import matplotlib.pyplot as plt
susceptible=0
infected=0.1
recoverd=0
beta=0.11
gamma=0.10
steps=100
graph_susceptible = []
graph_infected = []
graph_recovered = []
graph_steps = []

for i in range(0,steps):
    new_infected=beta*infected*susceptible
    new_recoverd=gamma*infected
    susceptible-=new_infected
    infected+=(new_infected-new_recoverd)
    recoverd+=new_recoverd


    graph_susceptible.append(susceptible)
    graph_steps.append(i)
    graph_recovered.append(recoverd)
    graph_infected.append(infected)






plt.figure()
plt.plot(graph_steps,graph_susceptible,label='Susceptible')
plt.plot(graph_steps,graph_infected,label='infected ')
plt.plot(graph_steps,graph_recovered,label='recovered')
plt.legend(loc='upper right')
plt.show()