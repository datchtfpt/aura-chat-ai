def format_conversation(messages):
    """
    Chuyển danh sách tin nhắn đã gán nhãn thành chuỗi hội thoại để đưa vào LLM.

    Input : output của merge_message() — list[{text, side}]
             side có thể là: 'right' (mình), 'left' (đối phương), 'timestamp'
    Output: chuỗi hội thoại dạng:
             Tôi: ...
             Đối phương: ...
    """
    lines = []
    for m in messages:
        if m["side"] == "timestamp":
            continue  # bỏ qua mốc thời gian, không đưa vào ngữ cảnh

        speaker = "Tôi" if m["side"] == "right" else "Đối phương"
        lines.append(f"{speaker}: {m['text']}")

    return "\n".join(lines)
