import random
import time

count = int(input('Введите число карточек: '))
task = open("generated.txt", 'w')
for k in range(1, 10): #hhlj;lk;l
    for i in range(1, 10):
        task.write(str(k))
        task.write(" X ")
        task.write(str(i))
        task.write("\n")
        task.write("\n")

task.close()
