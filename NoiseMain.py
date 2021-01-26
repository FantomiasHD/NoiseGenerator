from PIL import Image, ImageDraw
from loadingBar import LoadingBar
import random


class Noise:
    def __init__(self, Asize, Aiteration, Aadd, Aroughness, Acolor):
        self.size = Asize
        self.iteration = Aiteration
        self.add = Aadd
        self.roughness = Aroughness
        if Acolor > 255:
            raise AttributeError("color not in defined spectrum. Range: 0-255")

        #create noise
        self.img = Image.new('L', (self.size, self.size), color=Acolor)
        self.pix = self.img.load()
        self.draw = ImageDraw.Draw(self.img)

    def seed(self, seed):
        random.seed(seed)


    def generate(self):
        state = 0
        goal = self.size / self.iteration * 2
        genLoad = LoadingBar("Base", 50, goal, 10)

        for x in range(0, self.size, self.iteration):
            for y in range(0, self.size, self.iteration):
                if random.random()>0.3:
                    self.pix[x, y] = int((random.random() * 255))
                else:
                    self.pix[x, y] = (random.randint(0, 1) * 255)
            state += 1
            genLoad.draw(state)

        for x in range(int(self.iteration-self.iteration/2), self.size, self.iteration):
            for y in range(int(self.iteration-self.iteration/2), self.size, self.iteration):
                if random.random()>0.3:
                    self.pix[x, y] = int((random.random() * 255))
                else:
                    self.pix[x, y] = (random.randint(0, 1) * 255)
                #progress
            state += 1
            genLoad.draw(state)
        genLoad.finish()
                

    def generateEllipse(self, height):
        if self.iteration < height:
            raise AttributeError("height < iterations")
        else:
            state = 0
            goal = self.size / self.iteration * 2
            drawLoad = LoadingBar("Ellipse", 50, goal, 10)

            for x in range(0, self.size, self.iteration):
                for y in range(0, self.size, self.iteration):
                    self.draw.ellipse([(x-height, y-height),(x+height, y+height)], fill=self.pix[x, y])
                state += 1
                drawLoad.draw(state)

            for x in range(int(self.iteration-self.iteration/2), self.size, self.iteration):
                for y in range(int(self.iteration-self.iteration/2), self.size, self.iteration):
                    self.draw.ellipse([(x-height, y-height),(x+height, y+height)], fill=self.pix[x, y])
                state += 1
                drawLoad.draw(state)
            drawLoad.finish()

    def generateRect(self, height):
        if self.iteration < height:
            raise AttributeError("height < iterations")
        else:
            state = 0
            goal = self.size / self.iteration * 2
            drawLoad = LoadingBar("Rectangle", 50, goal, 10)

            for x in range(0, self.size, self.iteration):
                for y in range(0, self.size, self.iteration):
                    self.draw.rectangle([(x-height, y-height),(x+height, y+height)], fill=self.pix[x, y])
                state += 1
                drawLoad.draw(state)

            for x in range(int(self.iteration-self.iteration/2), self.size, self.iteration):
                for y in range(int(self.iteration-self.iteration/2), self.size, self.iteration):
                    self.draw.rectangle([(x-height, y-height),(x+height, y+height)], fill=self.pix[x, y])
                state += 1
                drawLoad.draw(state)
            drawLoad.finish()

    def generatePie(self, height):
        if self.iteration < height:
            raise AttributeError("height < iterations")
        else:
            state = 0
            goal = self.size / self.iteration * 2
            drawLoad = LoadingBar("Pie", 50, goal, 10)

            for x in range(0, self.size, self.iteration):
                for y in range(0, self.size, self.iteration):
                    self.draw.pieslice([(x-height, y-height),(x+height, y+height)],random.randint(-45, 10), random.randint(11, 315), fill=self.pix[x, y])
                state += 1
                drawLoad.draw(state)

            for x in range(int(self.iteration-self.iteration/2), self.size, self.iteration):
                for y in range(int(self.iteration-self.iteration/2), self.size, self.iteration):
                    self.draw.pieslice([(x-height, y-height),(x+height, y+height)],random.randint(-45, 10), random.randint(11, 315), fill=self.pix[x, y])
                state += 1
                drawLoad.draw(state)
            drawLoad.finish()


    def smooth(self):
        #smoothing
        state = 0
        goal = self.iteration
        smoothLoad = LoadingBar("Smoothing", 50, goal, 10)
        smoothLoad.draw(state)
        for i in range(1, self.iteration):
            for y in range(i-1, self.size, self.iteration):
                for x in range(i, self.size, self.iteration):
                    if not x + self.iteration > self.size:
                        self.pix[x, y] = (int((self.pix[x - 1, y] + self.pix[x + 1, y]+self.add) / 2+self.roughness*random.random()*10))

            for x in range(self.size):
                for y in range(i, self.size, self.iteration):
                    if not y+self.iteration > self.size:
                        self.pix[x, y] = (int((self.pix[x, y-1] + self.pix[x, y+1]+self.add) / 2+self.roughness*random.random()*10))
            state += 1
            smoothLoad.draw(state)
        smoothLoad.finish()

    def show(self, title):
        self.img.show(title=title)

    def save(self,path, name):
        self.img.save(path+name+'.png')


