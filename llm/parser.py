import re
import json


def parse_response(raw_text):
    """
    Parse chuỗi text trả về từ LLM thành dict Python.

    Xử lý cả trường hợp model trả về:
      - JSON thuần
      - JSON bọc trong ```json ... ```
    """
    # Loại bỏ markdown code fence nếu model lỡ thêm vào
    clean = re.sub(r"```json|```", "", raw_text).strip()

    try:
        return json.loads(clean)
    except json.JSONDecodeError:
        print("⚠️  Không parse được JSON. Output thô từ model:")
        print(raw_text)
        return None
