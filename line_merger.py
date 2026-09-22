def y_overlap_ratio(a, b):
    # Đoạn giao nhau theo trục Y của hai khung
    top = max(a["y_top"], b["y_top"])
    bottom = min(a["y_bottom"], b["y_bottom"])
    overlap = bottom - top

    if overlap <= 0:
        return 0.0   # không đè lên nhau chút nào

    # Chia cho khung THẤP hơn trong hai khung, để biết
    # "phần đè lên nhau chiếm bao nhiêu % khung nhỏ đó"
    height_a = a["y_bottom"] - a["y_top"]
    height_b = b["y_bottom"] - b["y_top"]
    min_height = min(height_a, height_b)

    return overlap / min_height


def merge_same_line(blocks, overlap_threshold=0.5):
    # Bước 1: lấy dữ liệu cần dùng, sắp theo x_left (trái → phải)
    items = []
    for b in blocks:
        items.append({
            "text": b["text"],
            "x_left": b["bbox"]["top_left"][0],
            "y_top": b["bbox"]["top_left"][1],
            "y_bottom": b["bbox"]["bottom_left"][1],
        })
    items.sort(key=lambda item: item["x_left"])

    # Bước 2: gom các khung chồng lấn nhau vào cùng một "hàng"
    rows = []
    for item in items:
        placed = False

        for row in rows:
            last = row[-1]
            if y_overlap_ratio(item, last) > overlap_threshold:
                row.append(item)
                placed = True
                break

        if not placed:
            rows.append([item])

    # Bước 3: sắp lại các hàng theo thứ tự từ trên xuống
    rows.sort(key=lambda row: row[0]["y_top"])

    # Bước 4: mỗi hàng nối chữ lại thành một dòng, tính khung bao cả hàng
    merged_lines = []
    for row in rows:
        text = " ".join(item["text"] for item in row)
        merged_lines.append({
            "text": text.strip(),
            "y_top": min(item["y_top"] for item in row),
            "y_bottom": max(item["y_bottom"] for item in row),
            "x_center": sum(item["x_left"] for item in row) // len(row),
        })

    return merged_lines