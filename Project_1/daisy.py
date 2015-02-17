import sys, os, re
from subprocess import call


def callDaisy(frame):

    features = []
    with open(frame) as data:
        for feature in data:
            x,y,d = re.split('\W+', feature)[:3]
            feature = (int(x), int(y), (int(d) + 1) / 2)
            features.append(feature)

    current_radius = 0
    image = r'./training_images/' + re.split('\W+', frame)[-2] + r'.jpg'
    for feature in features:
        call(['matlab','-nosplash','-nodesktop','-r','callDaisy(\'%s\', %d, %d, %d, %d)'%(str(image), feature[0] - 1, feature[1] - 1, feature[2], 1)])
        while(True):
            return


    # while(feature != 'q'):
    #     call(['matlab','-nosplash','-nodesktop','-r','callDaisy(\'%s\')'%(str(frame))])

    # if(len(features)):
    #     descriptor = re.split('\W+', frame)[-2]
    #     featurePoints = open('./training_data/%s.txt'%(text), 'w')
    #     features = sorted(features, key=lambda feature: feature[2])  #sort the feature points by radius
    #     for feature in features:
    #         featurePoints.write('%d,%d,%d\n'%(feature[0],feature[1],feature[2]))

    #     featurePoints.close()


def daisy(argv=None):

    if((len(argv) > 1) and (argv[1] == '-h')):    #print the usage
        print("Usage: daisy.py")
        return

    else:           #Selecing all features in 'training_data' directory to use for daisy
        frames = os.listdir(r'./training_data')
        for frame in frames:
            frame = r'./training_data/' + frame
            print("Calculating features listed in %s...\n"%(frame))
            callDaisy(frame)

    print("Finished getting DAISY descriptors")


if __name__ == "__main__":
    daisy(sys.argv)
