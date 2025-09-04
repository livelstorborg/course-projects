import numpy as np
from collections.abc import Callable


def mesh_function(f: Callable[[float], float], t: np.ndarray) -> np.ndarray:

    mesh_values = np.zeros(len(t))
    for i in range(len(t)):
        mesh_values[i] = f(t[i])

    return mesh_values


def func(t: float) -> float:
    
    if t <= 3:
        return np.exp(-t)
    if t <= 4:
        return np.exp(-3*t)


def test_mesh_function():
    t = np.array([1, 2, 3, 4])
    f = np.array([np.exp(-1), np.exp(-2), np.exp(-3), np.exp(-12)])
    fun = mesh_function(func, t)
    assert np.allclose(fun, f)

if __name__ == "__main__":
    test_mesh_function()
