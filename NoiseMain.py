from PIL import Image, ImageDraw
import random


class Noise:
    def __init__(self, Asize, Aiteration, Aadd):
        self.size = Asize
        self.iteration = Aiteration
        self.add = Aadd

        #create noise
        self.img = Image.new('L', (self.size, self.size), color='white')
        self.pix = self.img.load()
        self.draw = ImageDraw.Draw(self.img)

    def seed(self, seed):
        random.seed(seed)


    def generate(self):
        for x in range(0, self.size, self.iteration):
            for y in range(0, self.size, self.iteration):
                if random.random()>0.3:
                    self.pix[x, y] = int((random.random() * 255))
                else:
                    self.pix[x, y] = (random.randint(0, 1) * 255)

    def generateEllipse(self, height):
        if self.iteration < height:
            raise AttributeError("height < iterations")
        else:
            for x in range(0, self.size, self.iteration):
                for y in range(0, self.size, self.iteration):
                    self.draw.ellipse([(x-height, y-height),(x+height, y+height)], fill=self.pix[x, y])

    def generateRect(self, height):
        if self.iteration < height:
            raise AttributeError("height < iterations")
        else:
            for x in range(0, self.size, self.iteration):
                for y in range(0, self.size, self.iteration):
                    self.draw.rectangle([(x-height, y-height),(x+height, y+height)], fill=self.pix[x, y])


    def smooth(self):
        #smoothing
        for i in range(1, self.iteration):

            for y in range(i-1, self.size, self.iteration):
                for x in range(i, self.size, self.iteration):
                    if not x + self.iteration > self.size:
                        self.pix[x, y] = (int((self.pix[x - 1, y] + self.pix[x + 1, y]) / 2+self.add*random.random()*10))


            for x in range(self.size):
                for y in range(i, self.size, self.iteration):
                    if not y+self.iteration > self.size:
                        self.pix[x, y] = (int((self.pix[x, y-1] + self.pix[x, y+1]) / 2+self.add*random.random()*10))

    def show(self, title):
        self.img.show(title=title)

    def save(self,path, name):
        self.img.save(path+name+'.png')


