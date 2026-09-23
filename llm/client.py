import os
import google.generativeai as genai
from dotenv import load_dotenv
from llm.prompt import SYSTEM_PROMPT
from llm.parser import parse_response

load_dotenv()  # đọc .env vào os.environ


def analyze_conversation(conversation_text):
    """
    Gửi đoạn hội thoại lên Gemini và trả về dict gợi ý.

    Input : chuỗi hội thoại (output của format_conversation)
    Output: dict {"summary": ..., "suggestions": [...]}
            hoặc None nếu lỗi
    """
    key = os.getenv("GEMINI_API_KEY")
    if not key:
        raise ValueError("Thiếu GEMINI_API_KEY. Thêm vào .env hoặc truyền vào hàm.")

    genai.configure(api_key=key)
    model = genai.GenerativeModel(
        model_name="gemini-3.6-flash",
        system_instruction=SYSTEM_PROMPT,
    )

    response = model.generate_content(
        conversation_text,
        generation_config=genai.types.GenerationConfig(
            response_mime_type="application/json",
            temperature=0.6
        ),
    )

    return parse_response(response.text)
