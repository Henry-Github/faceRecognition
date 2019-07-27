import face_recognition
import cv2
import time

known_image = face_recognition.load_image_file('lib/raw.jpg')
cv2.imshow('known_image', known_image)

known_face = face_recognition.face_encodings(known_image)[0]

unknown_image = face_recognition.load_image_file('lib/pujing.jpg')

unknown_face = face_recognition.face_encodings(unknown_image)[0]

results = face_recognition.compare_faces([known_face], unknown_face)

if results[0]:
    print('yes')
else:
    print('no')

# count = 20
# while count > 0:
#     time.sleep(1)
#     count -= 1


# if __name__ == '__main__':
#     pass
