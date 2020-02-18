import ctrw
import matplotlib.pyplot as plt

process = ctrw.CTRW(100,gamma_x=1,gamma_t=1,alpha=2,beta=1,ndim=2)
x = process.get_samples()
t = process.times(2e-3)
plt.title(ctrw.__copyright__)
plt.plot(t,x)
plt.show()

print(process)
