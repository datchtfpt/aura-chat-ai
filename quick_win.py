import google.generativeai as genai
import json
import os

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))  

# Đây là đoạn hội thoại giả lập mà ta coi như đã quét được từ ảnh
conversation = """Cô ấy: Dạo này công việc em bận lắm, tối nào cũng về trễ
Mình: Vậy em nhớ ăn uống đầy đủ nha, đừng bỏ bữa
Cô ấy: Dạ em cảm ơn anh quan tâm :)
Mình: Cuối tuần này em có rảnh không?"""

# Xây dựng câu lệnh (Prompt) chỉ đạo cho AI
prompt = f"""Bạn là chuyên gia tư vấn giao tiếp, giúp đưa ra gợi ý tin nhắn tiếp theo.

Đoạn hội thoại gần đây:
{conversation}

Nhiệm vụ: Dựa vào ngữ cảnh, nhịp điệu và cảm xúc của đoạn hội thoại trên, đề xuất 3 phương án tin nhắn tiếp theo mà "Mình" có thể gửi để đối phương vui vẻ và có khả năng đồng ý đi chơi. Mỗi phương án có văn phong khác nhau (nhẹ nhàng / hài hước / tự tin), kèm lý do ngắn gọn.

Trả về ĐÚNG định dạng JSON, không thêm text nào khác. Format yêu cầu:
{{
  "phan_tich_ngu_canh": "...",
  "goi_y": [
    {{"noi_dung": "...", "phong_cach": "...", "ly_do": "..."}}
  ]
}}
"""

print("Đang gửi yêu cầu tới AI, vui lòng đợi...")
model = genai.GenerativeModel('gemini-3.6-flash')
# Gọi API GPT-4o
response = model.generate_content(
    prompt,
    generation_config=genai.types.GenerationConfig(
        response_mime_type="application/json",
    )
)
print("\n--- KẾT QUẢ TỪ AI (DẠNG JSON CHUẨN) ---")
# Gemini lấy kết quả cực kỳ đơn giản qua biến .text
ket_qua_json = response.text
print(ket_qua_json)

