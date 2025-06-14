import os
import PyPDF2
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import io

def create_watermark(user, font_path):
    # 注册NotoSansSC-Regular字体
    pdfmetrics.registerFont(TTFont("NotoSansSC", font_path))
    
    # 创建水印PDF
    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=letter)
    can.setFont("NotoSansSC", 40)  # 设置字体为NotoSansSC
    can.setFillColorRGB(0.2235, 0.7725, 0.7333, alpha=0.3)  # 设置为#39C5BB，透明度0.3
    can.rotate(45)
    can.drawString(100, 100, f"授权给 {user}，禁止外传")
    can.save()
    
    packet.seek(0)
    watermark = PyPDF2.PdfReader(packet)
    return watermark

def add_watermark_to_pdf(input_path, output_path, user, font_path):
    # 读取原始PDF
    pdf_reader = PyPDF2.PdfReader(input_path)
    pdf_writer = PyPDF2.PdfWriter()
    
    # 创建水印
    watermark = create_watermark(user, font_path)
    
    # 为每页添加水印
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        page.merge_page(watermark.pages[0])
        pdf_writer.add_page(page)
    
    # 保存输出PDF
    with open(output_path, 'wb') as output_file:
        pdf_writer.write(output_file)

def main():
    user = input("请输入授权用户名: ")
    current_dir = os.getcwd()
    output_dir = os.path.join(current_dir, "watermarked_pdfs")
    font_path = "NotoSansSC-Regular.ttf"  # 字体文件路径，替换为实际路径
    
    # 创建输出目录
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # 遍历当前目录下的所有PDF文件
    for filename in os.listdir(current_dir):
        if filename.lower().endswith('.pdf'):
            input_path = os.path.join(current_dir, filename)
            output_filename = f"watermarked_{filename}"
            output_path = os.path.join(output_dir, output_filename)
            
            try:
                add_watermark_to_pdf(input_path, output_path, user, font_path)
                print(f"已为 {filename} 添加水印，保存为 {output_filename}")
            except Exception as e:
                print(f"处理 {filename} 时出错: {str(e)}")

if __name__ == "__main__":
    main()
