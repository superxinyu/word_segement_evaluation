def to_region(split):
    regions = []
    start = 0
    for word in split:
        regions.append((start, start + len(word)))
    start += len(word)
    return regions


def evluate(pred_split, gold_split):
    pred_idx = set(to_region(pred_split))
    gold_idx = set(to_region(gold_split))
    correct_idx = pred_idx & gold_idx
    P = len(correct_idx) / len(pred_idx)
    R = len(correct_idx) / len(gold_idx)
    F1 = 2 * P * R / (P + R)
    return F1
