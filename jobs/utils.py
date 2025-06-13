import fitz     #PyMuPDF
import pytesseract
from PIL import Image
import io

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text_from_pdf(file_path):
    text = ""

    with fitz.open(file_path) as doc:
        for page in doc:
            # 嘗試用文字方式擷取
            page_text = page.get_text().strip()
            if page_text:
                text += page_text + "\n"
            else:
                # 若是圖片 PDF ，自動改用 OCR 擷取
                pix = page.get_pixmap(dpi=300)
                img = Image.open(io.BytesIO(pix.tobytes("png")))
                text += pytesseract.image_to_string(img, lang="chi_tra") + "\n"

    return text.strip()