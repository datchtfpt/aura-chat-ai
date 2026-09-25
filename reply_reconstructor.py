from difflib import SequenceMatcher


def text_similarity(a, b):
    return SequenceMatcher(None, a, b).ratio()


def find_match(text, candidates, threshold):
    """Kiểm tra text có trùng với bất kỳ candidate nào không."""
    return any(
        text_similarity(text, c["text"]) > threshold
        for c in candidates
    )


def reconstruct_replies(messages):
    """
    Dùng phương pháp thụt lề (Indentation) X_left / X_right để phát hiện Reply.
    - Tin rời rạc: Các bong bóng xếp thẳng tắp lề trái hoặc phải.
    - Tin Reply: 
        + Bên trái: Khối Quote bị thụt vào do vướng thanh dọc `|` (quote_x_left > reply_x_left).
        + Bên phải: Nhãn (Label) bị thụt vào do vướng icon mũi tên (label_x_right < reply_x_right).
    """
    result = []
    i = 0
    n = len(messages)

    while i < n:
        if i + 2 < n:
            label_msg = messages[i]
            quote_msg = messages[i + 1]
            reply_msg = messages[i + 2]

            side = label_msg.get("side")
            same_side = (
                side == quote_msg.get("side") == reply_msg.get("side")
            )

            # Label thường ngắn
            is_short_label = len(label_msg.get("text", "")) < 40
            
            has_x_coords = all(k in label_msg and k in quote_msg and k in reply_msg for k in ["x_left", "x_right"])

            if same_side and is_short_label and has_x_coords:
                is_reply = False
                
                # Kiểm tra thụt lề (Indentation)
                if side == "left":
                    # Mép trái của quote lớn hơn mép trái của reply (thụt vào > 10px)
                    indent = quote_msg["x_left"] - reply_msg["x_left"]
                    if indent > 10:
                        is_reply = True
                elif side == "right":
                    # Mép phải của label nhỏ hơn mép phải của reply (thụt vào > 10px)
                    indent = reply_msg["x_right"] - label_msg["x_right"]
                    if indent > 10:
                        is_reply = True

                if is_reply:
                    result.append({
                        "side": side,
                        "label": label_msg["text"],
                        "quoted": quote_msg["text"],
                        "text": reply_msg["text"],
                        "y_top": label_msg.get("y_top"),
                        "y_bottom": reply_msg.get("y_bottom"),
                        "x_left": min(label_msg["x_left"], quote_msg["x_left"], reply_msg["x_left"]),
                        "x_right": max(label_msg["x_right"], quote_msg["x_right"], reply_msg["x_right"])
                    })
                    i += 3
                    continue

        result.append(messages[i])
        i += 1

    return result
