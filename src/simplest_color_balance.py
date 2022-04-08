import numpy as np

def scb(img, s0=0.015, s1=0.015):
    dt = img.dtype
    threshold_0 = np.quantile(img, s0)
    threshold_1 = np.quantile(img, 1-s1)
    img = (img - threshold_0) / (threshold_1 - threshold_0)
    img = np.clip(img, 0, 1)
    if not np.issubdtype(dt, float):
        img = np.round(img * np.iinfo(dt).max).astype(dt)
    return img