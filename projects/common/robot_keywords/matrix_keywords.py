# matrix_keywords.py
import numpy as np
import time
from robot.api import logger

def setup_matrix_library():
    # optional: set paths, env vars
    logger.info("Matrix library setup")

def create_random_matrix(rows, cols, seed=None):
    if seed is not None:
        np.random.seed(int(seed))
    mat = np.random.randn(int(rows), int(cols))
    # save to disk or register in a simple object store for other keywords
    return mat

def matrix_multiply_and_verify_against_numpy(mat_a, mat_b, tolerance=1e-6):
    # call your project implementation (import from ai_matrix)
    from ai_matrix.linalg import matrix_multiply as impl_mul
    start = time.time()
    res_impl = impl_mul(mat_a, mat_b)
    elapsed = (time.time() - start) * 1000
    res_np = np.dot(mat_a, mat_b)
    if not np.allclose(res_impl, res_np, atol=float(tolerance)):
        raise AssertionError("Matrix multiply mismatch")
    logger.info(f"Matrix multiply OK, elapsed_ms={elapsed}")

