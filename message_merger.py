def get_y_top(line):
    return line["y_top"]

def merge_message(lines, gap_ratio=0.5):
    # Nhận input là output của merge_same_line:
    # mỗi phần tử đã có sẵn 'text', 'y_top', 'y_bottom' → không cần parse thêm

    if not lines:
        return []

    # Đảm bảo đã sắp xếp từ trên xuống dưới theo y_top
    lines = sorted(lines, key=get_y_top)

    # Tính chiều cao trung vị (median) của các dòng để làm ngưỡng gap
    heights = sorted(line["y_bottom"] - line["y_top"] for line in lines)
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