box1 = [1, 1, 3, 3]
box2 = [2, 2, 3, 3]


def iou(box1, box2):
    # 计算y轴重叠
    in_h = min(box1[3], box2[3]) - max(box1[1], box2[1])
    # 计算x轴重叠
    in_w = min(box1[2], box2[2]) - max(box1[0], box2[0])
    # 计算xy重叠面积
    inner = 0 if in_w < 0 or in_h < 0 else in_w * in_h
    # 计算两个矩形并及
    union = (box1[2] - box1[0]) * (box1[3] - box1[1]) + (box2[2] - box2[0]) * (box2[3] - box2[1]) - inner
    # 计算iou
    iou = inner / union
    return iou

print(iou(box1,box2))