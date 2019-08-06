import os


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

    def printWebps(self):
        for f in self.files:
            print(f)

    def convertFiles(self):
        

def main():
    tester = WebpToJpgConverter()
    tester.getPath()
    tester.findWebps()
    tester.printWebps()

if __name__ == '__main__':
    main()


