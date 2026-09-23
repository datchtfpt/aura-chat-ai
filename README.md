# 💬 AuraChatAI — AI Gợi Ý Tin Nhắn Từ Ảnh Chụp Chat

> *Sếp: Anh kia cho tôi biết hình trong trang này code như nào? 

>Tôi: Hình... hình như em ấy có người yêu rồi sếp ạ*

---

## 🎯 Giới Thiệu
![alt text](<Screenshot 2026-09-22 at 14.57.59.png>)

**AuraChatAI** là một công cụ AI hỗ trợ soạn tin nhắn/ý tưởng thông minh, được xây dựng để giải quyết một vấn đề rất thực tế:

> *"Em ăn cơm chưa..."*

### Ứng dụng thực tế

| Tình huống | AuraChatAI giúp gì? |
|---|---|
| 💼 **Công việc** | Soạn tin nhắn chuyên nghiệp, lịch sự với sếp, đồng nghiệp, khách hàng |
| ❤️ **Tình cảm** | Gợi ý câu trả lời duyên dáng, đúng mood/style, đúng thời điểm |
| 🤝 **Xã giao** | Không bao giờ bị "seen không rep - bơ già dừa non" vì không biết nói gì tiếp theo hoặc tự đưa mình vào thế khó |

### Cách hoạt động

```
📷 Ảnh chụp màn hình chat
        ↓
🔍 OCR — Đọc toàn bộ chữ trong ảnh (EasyOCR)
        ↓
📐 Phân tích tọa độ — Xác định ai nói gì, theo thứ tự nào
        ↓
🧠 LLM — Phân tích ngữ cảnh & đề xuất các phương án trả lời
        ↓
✅ Kết quả JSON — Nội dung + phong cách + lý do
```

---

## ⚙️ Cài Đặt & Chạy

### Yêu cầu hệ thống
- Python **3.10+** (khuyến nghị)
- macOS / Linux / Windows

### Bước 1: Clone dự án

```bash
git clone https://github.com/your-username/AuraChatAI.git
cd AuraChatAI
```

### Bước 2: Tạo môi trường ảo

```bash
python3 -m venv venv
source venv/bin/activate        # macOS / Linux
# venv\Scripts\activate         # Windows
```

### Bước 3: Cài đặt thư viện

```bash
pip install easyocr pillow google-genai python-dotenv
```

> ⚠️ Lần đầu cài `easyocr` sẽ tải model nhận dạng tiếng Việt (~500MB). Vui lòng chờ.

### Bước 4: Cấu hình API Key

Tạo file `.env` trong thư mục gốc:

```env
GEMINI_API_KEY=your_api_key_here
```

Lấy API key miễn phí tại: [https://aistudio.google.com/apikey](https://aistudio.google.com/apikey)

---

## 🚀 Chạy Thử

### Demo nhanh (không cần ảnh)

Chạy `quick_win.py` với đoạn hội thoại mẫu đã có sẵn:

```bash
python quick_win.py
```

**Kết quả mẫu:**
```json
{
  "phan_tich_ngu_canh": "Cô ấy đang bận nhưng vẫn nhắn lại...",
  "goi_y": [
    { "noi_dung": "Cuối tuần mình đi cà phê nhé?", "phong_cach": "Nhẹ nhàng", "ly_do": "..." },
    { "noi_dung": "Anh book chỗ ngon rồi, em chỉ cần đến thôi 😄", "phong_cach": "Tự tin", "ly_do": "..." },
    { "noi_dung": "Hay mình đổi gió cho em xả stress?", "phong_cach": "Hài hước", "ly_do": "..." }
  ]
}
```

### Chạy với ảnh thực tế

1. Chụp màn hình cuộc hội thoại, lưu vào thư mục dự án (ví dụ: `screenshot.png`)
2. Sửa tên file trong `ocr_service.py`:
   ```python
   test_image = "screenshot.png"
   ```
3. Chạy:
   ```bash
   python ocr_service.py
   ```

**Kết quả:**
```
--- HỘI THOẠI ---
[ĐỐI PHƯƠNG] Dạo này bận lắm anh ơi
[MÌNH      ] Ừ nhớ ăn uống đầy đủ nha
[ĐỐI PHƯƠNG] Dạ em cảm ơn anh quan tâm :)
```

---

## 🛣️ Lộ Trình Phát Triển

- [x] OCR đọc chữ từ ảnh
- [x] Phân tích tọa độ, xác định người nói
- [x] Gom tin nhắn đa dòng
- [ ] Tích hợp LLM gợi ý tin nhắn từ ảnh thực
- [ ] REST API (FastAPI)
- [ ] Giao diện web upload ảnh
- [ ] Hỗ trợ nhiều nền tảng chat (Zalo, iMessage, Instagram...)

---

## 📄 License

MIT — Dùng thoải mái, miễn là sớm có người yêu. 💪
