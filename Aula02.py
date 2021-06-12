from matplotlib import pyplot as plt

langs = ['C', 'Java', 'Javascript', 'Python', 'PHP']
students = [17, 35, 40, 43, 22]

fig, ax = plt.subplots()
ax.pie(students, labels=langs)
ax.axis('equal')

plt.title("Quantidade de alunos por linguagem")
plt.legend(langs)
plt.show()