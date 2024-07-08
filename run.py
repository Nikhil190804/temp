from flask import Flask
import face_recognition
import dlib

app = Flask(__name__)


def run_me():
    try:
        obama_image = face_recognition.load_image_file("profile_photo.jpeg")
        obama_face_encoding = face_recognition.face_encodings(obama_image)[0]
        return len(obama_face_encoding)
    except:
        return 0


@app.route('/')
def hello_name():
    ans=run_me()
    if(ans==128):
        return "<h1>done</h1>"
    else:
        return "<h1>bye</h1>"

   

if __name__ == '__main__':
   app.run(debug=False)
