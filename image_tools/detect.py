import cv2
import sys
import os.path
import os

def detect(directory, outputPath, cascade_file = "lbpcascade_animeface.xml"):
    if not os.path.isfile(cascade_file):
        raise RuntimeError("%s: not found" % cascade_file)

    cascade = cv2.CascadeClassifier(cascade_file)
    # reading images from directory
    images = []
    for filename in os.listdir(directory):
         img = cv2.imread(os.path.join(directory,filename))
         if img is not None:
             images.append(img)

    imagecounter = 0
    # for each image, recognize face and export as png. 
    for image in images:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray = cv2.equalizeHist(gray)

        faces = cascade.detectMultiScale(gray,
                                        # detector options
                                        scaleFactor = 1.1,
                                        minNeighbors = 5,
                                        minSize = (24, 24))
        for (x, y, w, h) in faces:
            imagecounter += 1
            filepath = outputPath + "%i.png" %imagecounter
            cv2.imwrite(filepath, cv2.resize(image[y:y+h,x:x+w], (256,256)))
    print("Done. Number of faces extracted: ", str(imagecounter))

if (len(sys.argv) != 3):
    print(len(sys.argv))
    sys.stderr.write("usage: detect.py <folder in> <folder out>\n")
    sys.exit(-1)

detect(sys.argv[1], sys.argv[2])

