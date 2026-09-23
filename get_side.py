from PIL import Image
from block_filter import is_timestamp


def get_image_width(image_path):
    with Image.open(image_path) as img:
        return img.width


def get_side(line, image_width, threshold_ratio=0.55):
    """
    Dùng x_center để phân loại trái/phải.

    x_center = (x_left + x_right) / 2 — tâm thực sự của bounding box.
    Giá trị này ổn định hơn x_left hay x_right đơn lẻ vì nó trung hòa
    ảnh hưởng của tin nhắn dài.
    """
    mid = image_width * threshold_ratio
    if line["x_center"] > mid:
        return "right"
    return "left"


def label_sides(merged_lines, image_width, threshold_ratio=0.55):
    labeled = []
    for line in merged_lines:
        # Ưu tiên kiểm tra timestamp trước khi phân loại trái/phải
        if is_timestamp(line["x_left"], line["x_right"], image_width):
            side = "timestamp"
        else:
            side = get_side(line, image_width, threshold_ratio)
        labeled.append({**line, "side": side})
    return labeled