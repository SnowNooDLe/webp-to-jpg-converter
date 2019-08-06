import os
from PIL import Image



class WebpToJpgConverter():

    def __init__(self):
        self.files = []
        self.path = ''

    def getPath(self):
        self.path = input('Type the directory where webps are : ')

    def findWebps(self):
        # r=root, d=directories, f = files
        for r, d, f in os.walk(self.path):
            for file in f:
                if '.webp' in file:
                    self.files.append(os.path.join(r, file))

        if len(self.files) == 0:
            return False

        return True

    def convertFiles(self):
        for filename in self.files:
            print('found: ' + os.path.splitext(filename)[0])
            print('converting to: ' + os.path.splitext(filename)[0] + '.jpg')
            im = Image.open(filename).convert("RGB")
            im.save(os.path.splitext(filename)[0] + '.jpg', "jpeg")
            print('done converting…')


def main():
    tester = WebpToJpgConverter()
    tester.getPath()
    # if webp files are found, do converting otherwise nothing
    if tester.findWebps():
        tester.convertFiles()

if __name__ == '__main__':
    main()


