import pyocr
from pathlib import Path
from PIL import Image, ImageGrab
import pyperclip as pc


# img = Path("./colors-poster.png")
# print(img)
# a = Image.open(img)
# a.show()
# print(type(Image.open(img)))


img = ImageGrab.grabclipboard()
pyocr.tesseract.TESSERACT_CMD = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
tools = pyocr.get_available_tools() #利用可能なエンジンをリストで取得
tool = tools[0] #オブジェクトを作成

builder = pyocr.builders.TextBuilder(tesseract_layout=6)    #読み取りオプション
text = tool.image_to_string(img, lang='eng', builder=builder)

# 文字列をクリップボードにコピー
pc.copy(text)
print(text)