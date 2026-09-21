import easyocr

print("Đang tải model OCR, vui lòng đợi (chỉ lâu ở lần đầu tiên)...")

reader = easyocr.Reader(["vi", "en"])

def extract_text(image_path):
    print(f"\nĐang quét ảnh: {image_path}...")

    results = reader.readtext(image_path)

    blocks = []

    for bbox, text, conf in results:
        x_center = sum(point[0] for point in bbox) / 4
        y_top = bbox[0][1]

        # Ép kiểu sang int thuần của Python để không còn chữ np.int32
        top_left = [int(v) for v in bbox[0]]
        top_right = [int(v) for v in bbox[1]]
        bottom_right = [int(v) for v in bbox[2]]  # Góc 2 là Dưới - Phải
        bottom_left = [int(v) for v in bbox[3]]   # Góc 3 là Dưới - Trái

        blocks.append({
            "text": text,
            "x_center": int(x_center),
            "y_top": int(y_top),
            "confidence": float(conf),
            "bbox": {
                "top_left": top_left,
                "top_right": top_right,
                "bottom_right": bottom_right,
                "bottom_left": bottom_left
            }
        })

    return blocks

def get_y_top(line):
    return line["y_top"]

def merge_message(blocks, gap_ratio=0.5):

    if not blocks:
        return []

    # Chuẩn bị list các dòng với đúng key từ cấu trúc dữ liệu của extract_text()
    lines = []
    for b in blocks:
        line = {
            "text":   b["text"],                    # text nằm thẳng trong b
            "y_top":  b["y_top"],                   # y_top nằm thẳng trong b
            "y_bottom": b["bbox"]["bottom_left"][1] # Y của cạnh dưới lấy từ bbox
        }
        lines.append(line)

    # Sắp xếp từ trên xuống dưới theo y_top
    lines.sort(key=get_y_top)

    # Tính chiều cao trung vị (median) của các dòng để làm ngưỡng
    heights = [line["y_bottom"] - line["y_top"] for line in lines]
    heights.sort()
    normal_height = heights[len(heights) // 2]
    threshold = gap_ratio * normal_height

    merged_message = []
    current = [lines[0]]  #  current là LIST, không phải dict

    for i in range(1, len(lines)):
        gap = abs(lines[i - 1]["y_bottom"] - lines[i]["y_top"])
        if gap < threshold:
            current.append(lines[i])  #  Dòng gần nhau → gom vào cùng nhóm
        else:
            merged_message.append(current)
            current = [lines[i]]      # Khởi nhóm mới cũng là list

    merged_message.append(current)  # Thêm nhóm cuối cùng

    # Nối text các dòng trong cùng một nhóm lại
    messages = []
    for msg in merged_message:
        text = " ".join(line["text"] for line in msg)
        messages.append(text.strip())

    return messages


if __name__ == "__main__":
    test_image = "screenshot1.png"
    blocks = extract_text(test_image)

    print("\n--- BƯỚC 1: KẾT QUẢ OCR THÔ ---")
    for b in blocks:
        print(f"Text: '{b['text']}' | X_center: {b['x_center']} | Y_top: {b['y_top']} | Conf: {b['confidence']:.2f}")
    
    print("\n--- BƯỚC 2: SAU KHI GOM TIN NHẮN ---")
    messages = merge_message(blocks)
    for i, msg in enumerate(messages):
        print(f"[{i+1}] {msg}")