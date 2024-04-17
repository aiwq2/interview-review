labels=[0,0,1,1,1]
preds=[0.7,0.2,0.5,0.6,0.2]
def naive_auc(labels,preds):
    """
    最简单粗暴的方法
　　　先排序，然后统计有多少正负样本对满足：正样本预测值>负样本预测值, 
      再除以总的正负样本对个数。复杂度 O(NlogN), N为样本数
    """
    n_pos = sum(labels)
    n_neg = len(labels) - n_pos
    total_pair = n_pos * n_neg

    labels_preds = zip(labels,preds)
    labels_preds = sorted(labels_preds,key=lambda x:x[1])
    accumulated_neg = 0
    satisfied_pair = 0
    for i in range(len(labels_preds)):
        if labels_preds[i][0] == 1:
            satisfied_pair += accumulated_neg
        else:
            accumulated_neg += 1

    return satisfied_pair / float(total_pair)

print(naive_auc(labels,preds))