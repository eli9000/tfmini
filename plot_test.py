import matplotlib.pyplot as plt

f = open("tf_data.txt", "r")
data = []
fl = f.readlines()

for x in fl:
    num = int(x)
    data.append(num)

# print(data)
plt.plot(data)
# plt.ylabel('Numbers')
plt.show()
