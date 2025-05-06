import re 
import unidecode


def generate_slug(text): #tạo url thân thiện thì google mới đưa đường dẫn lên top seo
    vb=unidecode.unidecode(text) #loại bỏ dấu tiếng việt chuyển sang ký tự không dấu ASCII
    chuthuong=vb.lower()#chuyển chữ cái hoa nếu có thành chữ thường
    #thay thế khoảng trắng bằng gạch (ngang) -, thay 1 dấu -- thành 1 dấu-
    bokhoangtrang=re.sub(r'\s+','-',chuthuong) 
    bohaigach=re.sub(r'-+','-',bokhoangtrang)
    #xóa các ký tự k phải chữ và số
    kytu=re.sub(r'[^a-z0-9-]','',bohaigach)
    chuoi=kytu.strip('-')#loại bỏ dấu gạch ngang ở đầu và cuối chuỗi
    return chuoi