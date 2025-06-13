from PIL import Image
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from .models import Job
import fitz     #PyMuPDF
import pytesseract
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

def recommend_jobs(resume_text, top_n=3):
    jobs = Job.objects.all()
    job_texts = [job.title + " " + job.company for job in jobs]
    corpus = [resume_text] + job_texts

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(corpus)
    similarty_scores = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()

    top_indices = similarty_scores.argsort()[::-1][:top_n]
    recommended = [(jobs[i], similarty_scores[i]) for i in top_indices]
    return recommended