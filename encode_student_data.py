from imutils import paths
import face_recognition
import pickle
import cv2
import os


def encode_student_data(student_id_name):
    # get the input images in dataset
    #print("[INFO] quantifying faces..")
    student_image_path = "dataset/"+student_id_name
    imagePaths = list(paths.list_images(student_image_path))
    # initialis d list of known encodings and known names
    knownEncodings = []
    knownNames = []
    
    # loop over the image paths
    for (i, imagePath) in enumerate(imagePaths):
        # get person name from the image path
        name = imagePath.split(os.path.sep)[-2]
        print(name)
        # get image nd convert it from RGB to BGR
        image = cv2.imread(imagePath)
        rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        # detect the coordinates of face
        box = face_recognition.face_locations(rgb, model='hog')
        # encode
        encodings = face_recognition.face_encodings(rgb, box)
        # Loop over d encodings :
        for encoding in encodings:
            # add the values and names in lists
            knownEncodings.append(encoding)
            knownNames.append(name)

    if(os.path.isfile('encodings.pickle')):
        with open('encodings.pickle', 'rb') as f:
            old_data = pickle.load(f)
        old_data['encodings'] += knownEncodings
        old_data['names'] += knownNames
    else:
        old_data = {"encodings": knownEncodings, "names": knownNames}
    f = open("encodings.pickle", "wb")
    f.write(pickle.dumps(old_data))
    f.close()
