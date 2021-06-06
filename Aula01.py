from matplotlib import pyplot as plt

langs = ['C', 'Java', 'Javascript', 'Python', 'PHP']
students = [17, 35, 40, 43, 22]
ax = plt.bar(langs, students)
ax[0].set_color('#1e1e1e')
ax[1].set_color('#1a1a1a')
ax[2].set_color('#1e1e1e')
ax[3].set_color('#1a1a1a')
ax[4].set_color('#1e1e1e')
plt.title("Quantidade de alunos por linguagem")
plt.legend(['Linguagens'])
plt.show()
