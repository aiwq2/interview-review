import numpy as np
class MyBN:
    def __init__(self, momentum=0.01, eps=1e-5, feat_dim=2):
        """
        初始化参数值
        :param momentum: 动量，用于计算每个batch均值和方差的滑动均值
        :param eps: 防止分母为0
        :param feat_dim: 特征维度
        """
        # 均值和方差的滑动均值
        self._running_mean = np.zeros(shape=(feat_dim, ))
        self._running_var = np.ones(shape=(feat_dim, ))
        # 更新self._running_xxx时的动量
        self._momentum = momentum
        # 防止分母计算为0
        self._eps = eps
        # 对应Batch Norm中需要更新的beta和gamma，采用pytorch文档中的初始化值
        self._beta = np.zeros(shape=(feat_dim, ))
        self._gamma = np.ones(shape=(feat_dim, ))

    def batch_norm(self, x):
        """
        BN向传播
        :param x: 数据
        :return: BN输出
        """
        if self.training:
            x_mean = x.mean(axis=0)
            x_var = x.var(axis=0)
            # 对应running_mean的更新公式
            self._running_mean = (1-self._momentum)*x_mean + self._momentum*self._running_mean
            self._running_var = (1-self._momentum)*x_var + self._momentum*self._running_var
            # 对应论文中计算BN的公式
            x_hat = (x-x_mean)/np.sqrt(x_var+self._eps)
        else:
            x_hat = (x-self._running_mean)/np.sqrt(self._running_var+self._eps)
        return self._gamma*x_hat + self._beta