import sys, os, re
from subprocess import call

trainingMessage = "Enter feature center-point (x,y) and feature diameter (d) in pixels\nor enter 'q' to quit\n\tExample: '50,50,10' (x=50, y=50, d=10 pixels)\n\n"

def addNewFeature(image):
    features = []
    feature = raw_input(trainingMessage)
    while(feature != 'q'):
        x,y,d = re.split('\W+', feature)
        feature = (int(x), int(y), int(d))
        features.append(feature)

        feature = raw_input(trainingMessage)

    if(len(features)):
        text = re.split('\W+', image)[-2]
        featurePoints = open('./training_data/%s.txt'%(text), 'w')
        features = sorted(features, key=lambda feature: feature[2])  #sort the feature points by radius
        for feature in features:
            featurePoints.write('%d,%d,%d\n'%(feature[0],feature[1],feature[2]))

        featurePoints.close()


def training(argv=None):
    Status = -1

    if((len(argv) > 1) and (argv[1] == '-h')):    #print the usage
        print("Usage: training.py [frame1.jpg ...]")
        return

    elif(len(argv) > 1):    #Case 1: selecting specific images to use for training
        images = argv[1:]
        for image in images:
            Status = call(['matlab','-nosplash','-nodesktop','-r','training(\'%s\')'%(str(image))])
            print("Selecting features from %s...\n"%(image))
            addNewFeature(image)

    else:                   #Case 2: selecing all images in the 'training_images' directory to use for training
        images = os.listdir(r'./training_images')
        for image in images:
            image = r'./training_images/' + image
            Status = call(['matlab','-nosplash','-nodesktop','-r','training(\'%s\')'%(str(image))])
            print("Selecting features from %s...\n"%(image))
            addNewFeature(image)

    if(Status == 0):
        print("Finished training")


if __name__ == "__main__":
    training(sys.argv)
