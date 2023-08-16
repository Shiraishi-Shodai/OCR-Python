import pyocr
from PIL import Image, ImageGrab
import pyperclip as pc

# OCRは画像内のテキストを認識し、テキストとして抽出するための技術
# pyocrのtesseractエンジンを使用する
pyocr.tesseract.TESSERACT_CMD = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
# pyocrの初期化
tools = pyocr.get_available_tools() #
tool = tools[0]

# img = Image.open('C:/Users/shodai/Pictures/Saved Pictures/tesserat_test.png')
img = ImageGrab.grabclipboard() #クリップボードから画像を取得
# TextBuilderは、テキスト抽出のためのカスタム設定を行うためのクラス
builder = pyocr.builders.TextBuilder(tesseract_layout=6) #tesseract_layoutはデフォルトでは3
# テキストを抽出する
text = tool.image_to_string(img, lang='jpn', builder=builder) #lang='jpn'で日本語で抽出することを指定

# print(text)
pc.copy(text)   #抽出したテキストをクリップボードに保存