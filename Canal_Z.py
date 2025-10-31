import numpy as np
from typing import List, Union

def h2(x):
	if(x == 0 or x == 1): return 0
	else: return (-x)*np.log2(x) - (1-x)*np.log2(1-x)
	
def p3(a: float) -> List[float]:
	i_alpha = h2(0.5 * a) - a
	c = 0
	p = 0
	for step in np.arange(0, 1, 0.001):
		i = h2(0.5 * step) - step
		if(i > c):
			p = step
			c = i


	return [i_alpha, c, p]
