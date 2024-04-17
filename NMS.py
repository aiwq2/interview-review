import numpy as np
boxes = np.array([[100, 100, 210, 210, 0.72],
                  [250, 250, 420, 420, 0.8],
                  [220, 220, 320, 330, 0.92],
                  [100, 100, 210, 210, 0.72],
                  [230, 240, 325, 330, 0.81],
                  [220, 230, 315, 340, 0.9]])


def nms(bboxs, thr):
    x1 = bboxs[:, 0]
    y1 = bboxs[:, 1]
    x2 = bboxs[:, 2]
    y2 = bboxs[:, 3]
    score = bboxs[:, 4]
    areas = (x2 - x1 + 1) * (y2 - y1 + 1)
    order = np.argsort(score)
    print(order)
    keep = []
    while order.size > 0:
        index = order[-1]
        keep.append(index)
        inner_x1 = np.maximum(x1[index], x1[order[:-1]])
        inner_x2 = np.minimum(x2[index], x2[order[:-1]])

        inner_y1 = np.maximum(y1[index], y1[order[:-1]])
        inner_y2 = np.minimum(y2[index], y2[order[:-1]])
        in_w = np.maximum(0.0, inner_x2 - inner_x1 + 1)
        in_h = np.maximum(0.0, inner_y2 - inner_y1 + 1)
        inner = in_w * in_h
        # 利用相交的面积和两个框自身的面积计算框的交并比, 将交并比大于阈值的框删除 对应第4步
        ratio = inner / (areas[index] + areas[order[:-1]] - inner)
        left = np.where(ratio < thr)  # left里面对应的就是<thr的索引
        order = order[left]  # 将所有<thr的索引取出来
    
    return keep

print(nms(boxes,0.7))
