import numpy as np


def extract_rivers(accumulation, percentile=95):

    threshold = np.percentile(accumulation, percentile)

    rivers = accumulation >= threshold

    return rivers, threshold