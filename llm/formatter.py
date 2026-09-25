def format_conversation(messages):
    """
    Chuyển danh sách tin nhắn thành chuỗi hội thoại để đưa vào LLM.

    Hỗ trợ 2 loại message:
        - Tin thường:   {"text": "...", "side": "left/right"}
        - Tin reply:    {"text": "...", "side": "...", "label": "...", "quoted": "..."}
    """
    lines = []
    for m in messages:
        if m["side"] == "timestamp":
            continue

        speaker = "Tôi" if m["side"] == "right" else "Đối phương"

        if m.get("label"):
            lines.append(f'{speaker}: {m["label"]}: {m["quoted"]} -> {m["text"]}')
        else:
            lines.append(f"{speaker}: {m['text']}")

    return "\n".join(lines)
