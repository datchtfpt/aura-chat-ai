from ocr_reader import extract_text
from line_merger import merge_same_line
from message_merger import merge_message
from get_side import get_image_width, label_sides
from pathlib import Path

if __name__ == "__main__":
    test_image = str(Path("images") / "screenshot_mess_01.png")

    blocks = extract_text(test_image)

    print("\n--- BƯỚC 1: KẾT QUẢ OCR THÔ ---")
    for b in blocks:
        tl = tuple(b["bbox"]["top_left"])
        tr = tuple(b["bbox"]["top_right"])
        br = tuple(b["bbox"]["bottom_right"])
        bl = tuple(b["bbox"]["bottom_left"])
        print(f"Text: '{b['text']}' | X_center: {b['x_center']} | Y_top: {b['y_top']} | Conf: {b['confidence']:.2f}")
        print(f"   Góc: TL{tl} → TR{tr} → BR{br} → BL{bl}")

    print("\n--- BƯỚC 2: GOM CÁC BLOCK CÙNG DÒNG NGANG (merge_same_line) ---")
    merged_lines = merge_same_line(blocks)
    for i, line in enumerate(merged_lines):
        print(f"[{i+1}] '{line['text']}' | Y: {line['y_top']} → {line['y_bottom']}")

    print("\n--- BƯỚC 3: GOM CÁC DÒNG THÀNH TIN NHẮN (merge_message) ---")
    messages = merge_message(merged_lines)
    for i, msg in enumerate(messages):
        print(f"[{i+1}] {msg['text']}")

    print("\n--- BƯỚC 4: GÁN NHÃN TRÁI/PHẢI ---")
    labeled = label_sides(merged_lines, get_image_width(test_image))
    labeled_msgs = merge_message(labeled)
    print("\n--- HỘI THOẠI ---")
    for lmsg in labeled_msgs:
        if lmsg["side"] == "timestamp":
            label = "== TIME =="
        elif lmsg["side"] == "right":
            label = "   MÌNH   "
        else:
            label = "ĐỐI PHƯƠNG"
        print(f"[{label}] {lmsg['text']}")