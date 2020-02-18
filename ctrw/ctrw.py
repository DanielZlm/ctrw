import numpy as np

class CTRW(object):

	def __init__(self, n, gamma_x=1,gamma_t=1, alpha =2, beta=1, ndim=1):
		self.n = n
		self.gamma_x = gamma_x
		self.gamma_t = gamma_t
		self.alpha = alpha
		self.beta = beta
		self.ndim = ndim

	def __str__(self):
		return ("".join([" CTRW (",
				'n = ', str(self.n),
				', gamma_x = ',str(self.gamma_x),
				', gamma_t = ',str(self.gamma_t),
				', alpha = ',str(self.alpha),
				', beta = ',str(self.beta),
				', ndim = ',str(self.ndim),
				")"]))

	def times(self,dt):
		T  = (self.n-1)*dt
		return np.linspace(0, T, self.n)


	def get_samples(self):

		def get_CTRW_timestep(gamma_t,beta,N=1):
			u = np.random.rand(N)
			v = np.random.rand(N)
			a2 = np.sin(beta*np.pi)/np.tan(beta*np.pi*v)-np.cos(beta*np.pi)
			tau = - gamma_t* np.log(u)*np.power(a2,1/beta)
			return tau

		def get_CTRW_spatialstep(gamma_x,alpha,N=1,ndim=1):
			u = np.random.rand(N,ndim)
			v = np.random.rand(N,ndim)
			phi = np.pi*(v-0.5)
			a1 = - (np.log(u)*np.cos(phi))/(np.cos((1-alpha)*phi))
			xi =  gamma_x*np.power(a1,1-(1/alpha))*np.sin(alpha*phi)/np.cos(phi)
			return xi

		x = np.zeros([self.n,self.ndim])
		stop  = 0
		while(stop<self.n):
			start = stop

			stop += int(get_CTRW_timestep(self.gamma_t,self.beta,N=1))
			x[start:stop,:] =  x[start-1,:]+get_CTRW_spatialstep(self.gamma_x,self.alpha,N=1,ndim=self.ndim)

		return x
