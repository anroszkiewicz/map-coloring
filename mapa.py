import numpy
import matplotlib.pyplot as plt
import colorsys

def hsv2rgb(h, s, v):
    return colorsys.hsv_to_rgb(h, s, v)

def gradient_hsv(h,v):
    return hsv2rgb(1/3-1/3*h, 1, v)

if __name__ == '__main__':
    #read data from file into numpy array
    with open("big.dem") as file:
        header = file.readline().split()
        w = int(header[0])
        h = int(header[1])
        dist = int(header[2])

    points = numpy.loadtxt("big.dem",skiprows=1)

    #normalize points to 0-1 range
    points = (points - numpy.min(points))/(numpy.max(points)-numpy.min(points))

    #vector to light source
    s = [0.5,1.5,3]
    norm = numpy.linalg.norm(s)
    s = s/norm

    #calculate normal vectors
    angle = numpy.zeros((h,w))
    
    for i in range(0,h):
        for j in range(0,w):
            if i>0:
                differencetoleft = points[i-1,j] - points[i,j]
            else:
                differencetoleft = 0
            if j>0:
                differencetoup = points[i,j-1] - points[i,j]
            else:
                differencetoup = 0

            vectortoleft = [dist,0,differencetoleft*100000]
            vectortoup = [0,dist,differencetoup*100000]

            v = numpy.cross(vectortoleft,vectortoup)
            v = v / numpy.linalg.norm(v)

            #calculate angle between s and v
            angle[i,j] = numpy.dot(s,v)
    
    angle = (angle - numpy.min(angle))/(numpy.max(angle)-numpy.min(angle))

    #create an array with corresponding rgb values
    img = numpy.zeros((h, w, 3))
    for i in range(h):
        for j in range(w):
            img[i,j,:] = gradient_hsv(points[i,j],angle[i,j])

    plt.imshow(img)
    plt.tick_params(bottom='True',top='True',left='True',right='True',direction='in')
    plt.show()