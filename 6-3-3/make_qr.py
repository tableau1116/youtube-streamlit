import qrcode
import qrcode.image.svg

class MakeQR:
    def __init__(self, output):
        self.url = ""
        self.output = output
        
    def make(self):
        factory = qrcode.image.svg.SvgImage
        img = qrcode.make(self.url, image_factory=factory)
        img.save(self.output)
        
    def run(self):
        url = input("URLを入力してください:")
        if not url.startswith("http"):
            print("入力された文字列が、httpから始まっていません")
            return
        self.url = url
        self.make()
                
        
if __name__ == '__main__':
    import sys
    args = sys.argv
    output = args[1]    
    app = MakeQR(output)
    app.run()
    