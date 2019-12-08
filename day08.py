import math



class Layer:
    def __init__(self, source):
        self.pixels = source

    def countChars(self, charToSearch):
        count = 0
        for c in self.pixels:
            if c == charToSearch:
                count += 1
        return count

class SpaceImage:
    def __init__(self, x, y, layers):
        self.layers = layers
        self.width = x
        self.height = y
        self.finalPixels = []

    def calcImage(self):
        # Calculate the image by looking pixel by pixel and
        # find the pixel that 'shines through'
        for i in range(len(self.layers[0].pixels)):
            self.finalPixels.append(self.findPixelColor(i))


    def findPixelColor(self, pixelIndex):
        # Search for the first non-2 pixel
        for l in self.layers:
            if l.pixels[pixelIndex] != '2':
                return l.pixels[pixelIndex]
        return 2

    # Gets a string representation of this image by replacing
    # All "1"s in the image with #, and all "0"s with spaces
    def getImageString(self):
        self.calcImage()
        outputString = ''
        index = 0
        for y in range(self.height):
            for x in range(self.width):
                if self.finalPixels[index] == '1':
                    outputString += '#'
                elif self.finalPixels[index] == '0':
                    outputString += ' '
                index += 1
            outputString += '\n'
        return outputString



def star1():
    print("Star 1")
    layers = []
    with open('puzzles/day8.txt', 'r') as f:
        layerString = f.read(25*6)
        layer = Layer(layerString)
        layers.append(layer)
        leastZeros = 99999
        leastZerosIndex = 0
        while layerString:
            layerString = f.read(25 * 6)
            if layerString:
                layer = Layer(layerString)
                layers.append(layer)
    for i in range(len(layers)):
        # Need to count 0s
        # and then count 1s and 2s
        zerosInThisLayer = layers[i].countChars('0')
        if zerosInThisLayer < leastZeros:
            leastZeros = zerosInThisLayer
            leastZerosIndex = i
    print("Least zeros: {0} in layer {1}".format(leastZeros, leastZerosIndex))
    print(layers[leastZerosIndex].countChars('1') * layers[leastZerosIndex].countChars('2'))
    image = SpaceImage(25, 6, layers)
    return image

def star2(image):
    print("Star 2")
    print(image.getImageString())



layers = star1()
star2(layers)