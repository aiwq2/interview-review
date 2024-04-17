import math
import torch
import torch.nn as nn
import torch.nn.functional as F

class MultiHeadAttention(nn.Module):
    def __init__ (self,heads, d_model, dropout=0.1):
        super().__init__()
        self.d_model =d_model
        self.d_k=d_model // heads
        #每个“头”对应的维度
        self.h= heads #“头”的数量
        # 初始化线性层，用于生成 Q，K，V
        self.q_linear = nn.Linear(d_model, d_model)
        self.k_linear =nn.Linear(d_model,d_model)
        self.v_linear= nn.Linear(d_model,d_model)
        self.dropout = nn.Dropout(dropout)
        # 输出线性层
        self.out =nn.Linear(d_model,d_model)

    def attention(self,q,k,v,mask=None):
        # q,k,v: (batch_size,heads,sql_len,d_k)
        # 计算点积，并通过 sqrt(d_k)进行缩放
        scores =torch.matmul(q,k.transpose(-2,-1))/ math.sqrt(self.d_k)
        #如果有 mask，应用于 scores
        if mask is not None:
            scores =scores.maskedfill(mask==0,-1e9)
        #对scores 应用 softmax
        scores =F.softmax(scores,dim=-1)
        # 应用 dropout
        scores =self.dropout(scores)
        # 获取输出
        output =torch.matmul(scores,v)
        return output
    
    def forward(self,q,k,v,mask=None):
        # q,k,v: (batch_size,seq_len,d_model)
        batch_size=q.size(0)

        q=self.q_linear(q).view(batch_size,-1,self.h,self.d_k).transpose(1,2)
        k=self.k_linear(k).view(batch_size,-1,self.h,self.d_k).transpose(1,2)
        v=self.v_linear(v).view(batch_size,-1,self.h,self.d_k).transpose(1,2)
        # 进行多头注意力计算
        # score:(batch_size,head,sql_len,d_model)
        scores=self.attention(q,k,v,mask)

        concat=scores.transpose(1,2).contiguous().view(batch_size,-1,self.d_model)
        output=self.out(concat)

        return output
    
heads=4
d_model=128
droupout=0.1

model=MultiHeadAttention(heads,d_model,droupout)

batch_size=2
seq_len=5

q=torch.rand(batch_size,seq_len,d_model)
k=torch.rand(batch_size,seq_len,d_model)
v=torch.rand(batch_size,seq_len,d_model)

output=model(q,k,v)
print('output shape:',output.shape)

loss=output.mean()
loss.backward()

print('Backward pass completed.')


