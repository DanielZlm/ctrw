# Monte Carlo Simulation of uncoupled Continuous-time random walks 

This is a python implementation of the algorithm purposed in a Paper of <i>D. Fulger et. al </i> in 2008.

<p align="center"><img  src="example.png" alt="Example of a CTRW realization"></p>

## References
<ul>
<li>Fulger, D., Scalas, E., & Germano, G. (2008). Monte Carlo simulation of uncoupled continuous-time random walks yielding a stochastic solution of the space-time fractional diffusion equation. Physical Review E - Statistical, Nonlinear, 
and Soft Matter Physics, 77(2), 1–7. <a href="https://doi.org/10.1103/PhysRevE.77.021122">https://doi.org/10.1103/PhysRevE.77.021122</a>
</li>
</ul>

## Dependencies
Just numpy. 
## Install
Just move the ctrw folder to a subdirectory of your python script where you want to use it. Then import it e.g. as 
```python
from ctrw import CTRW
```

## Usage
<p>Run example_ctrw.py without any arguments to create a two dimensional CTRW and plot it versus time.</p>
<p><b>Note:</b> You have to have matplotlib installed to run the example</p>

```python
import ctrw
import matplotlib.pyplot as plt

process = ctrw.CTRW(100,gamma_x=1,gamma_t=1,alpha=2,beta=1,ndim=2)
x = process.get_samples()
t = process.times(2e-3)
plt.title(ctrw.__copyright__)
plt.plot(t,x)
plt.show()

```
