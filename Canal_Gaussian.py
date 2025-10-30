import numpy as np
from typing import List, Union

def p4(Px: float, N: float, W: float) -> float:
	return W * np.log2(1 + Px / N)