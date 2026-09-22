from PIL import Image

def get_image_width(image_path):
    with Image.open(image_path) as img:
        return img.width

def get_side(line, image_width, threshold_ratio=0.55):
    mid = image_width * threshold_ratio
    if line["x_center"] > mid:
        return "right"
    return "left"

def label_sides(merged_lines, image_width, threshold_ratio=0.55):
    labeled = []

    for line in merged_lines:
        side = get_side(line, image_width, threshold_ratio)
        labeled.append({**line, "side":side})

    return labeled