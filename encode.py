from imutils import paths
import face_recognition
import pickle
import cv2 
import os

# get the input images in our dataset
print("[INFO] quantifying faces..")
imagePaths = list(paths.list_images("dataset"))

# initial the list of known encodings and known names
knownEncodings = []
knownNames = []

# loop over the image paths
for (i, imagePath) in enumerate(imagePaths):
	#get person name from the image path
	print("[INFO] processing image {}/{}".format(i+1,len(imagePaths)))
	name = imagePath.split(os.path.sep)[-2]

	# get img nd convert it from BGR cv to RGB
	image = cv2.imread(imagePath)
	rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

	#detect the cordonnées of face
	box = face_recognition.face_locations(rgb, model = 'hog')

	# encode
	encodings = face_recognition.face_encodings(rgb, box)

	# loop over the encodings :
	for encoding in encodings:
		# add values and names in lists
		knownEncodings.append(encoding)
		knownNames.append(name)
# now save the list
print("[INFO] Serializing encodings..")
data = {"encodings": knownEncodings, "names": knownNames}
f = open("encodings.pickle","wb")
f.write(pickle.dumps(data))
f.close()
