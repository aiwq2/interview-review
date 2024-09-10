import numpy as np
r=np.array([1,0,0,1,0])
dcg = r[0] + np.sum(r[1:] / np.log2(np.arange(2, r.size + 1)))
r_s = sorted(r,reverse=True)
r_s = np.array(r_s)
dcg_max = r_s[0] + np.sum(r_s[1:] / np.log2(np.arange(2, r_s.size + 1)))
print(dcg,dcg_max)
print(dcg/dcg_max)
