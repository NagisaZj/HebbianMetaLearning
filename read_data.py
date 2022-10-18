import numpy as np
import matplotlib.pyplot as plt

file_names = ['/data2/zj/HebbianMetaLearning/heb_coeffs/1666004569/Fitness_values_1666004569_Walker2d-v2.npy']
# file_names = ['/data2/zj/HebbianMetaLearning/heb_coeffs/1666071466/Fitness_values_1666071466_AntBulletEnv-v0.npy']
# file_names = ['/data2/zj/HebbianMetaLearning/heb_coeffs/1666004571/Fitness_values_1666004571_Humanoid-v2.npy']
# file_names = ['/data2/zj/HebbianMetaLearning/heb_coeffs/1666004570/Fitness_values_1666004570_Ant-v2.npy']
# file_names = ['/data2/zj/HebbianMetaLearning/heb_coeffs/1666071627/Fitness_values_1666071627_HalfCheetah-v2.npy']
plt.figure()
for p in file_names:
    a=np.load(p)

plt.plot(np.arange(len(a)),a)
plt.show()