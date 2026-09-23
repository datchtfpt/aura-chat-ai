def is_timestamp(x_left, x_right, image_width, margin_ratio=0.2):
    margin = margin_ratio * image_width
    distance_from_left = x_left
    distance_from_right = image_width - x_right

    return distance_from_left > margin and distance_from_right > margin


def filter_blocks(blocks, image_width, min_confidence=0.4):
    result = []
    for b in blocks:
        if b["confidence"] < min_confidence:
            continue

        x_left = b["bbox"]["bottom_left"][0]
        x_right = b["bbox"]["bottom_right"][0]

        if is_timestamp(x_left, x_right, image_width):
            continue

        result.append(b)
    return result
