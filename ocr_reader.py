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