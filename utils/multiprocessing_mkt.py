import pymannkendall as mkt
import numpy as np
import multiprocessing

def mkt_wrapper(arr):
    res = mkt.original_test(arr)
    return res.trend

def multi_mkt(observation_arr, pool=4):
    """_summary_
    Args:
        observation_arr (_type_): the array in shape (number of observations, length per observation).
        pool (int, optional): _description_. Defaults to 4.
    """

    with multiprocessing.Pool(pool) as p:
        results = p.map(mkt_wrapper, observation_arr)
    return results


def single_mkt(observation_arr):
    results = []
    for arr in observation_arr:
        results.append(mkt_wrapper(arr))

    return results