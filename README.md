# Face detection demo
This is a demo in usage of Haar Feature-based Cascade Classifiers

## Dependencies
- python2.7
- opencv-python=3.3.0.10
- numpy=1.13.3

## How to setup
You'd better to use a virtual env and run:
```
pip install -r requirements.txt
```
## How to use
- Detect a single image
```
python detect.py src_image.jpg detected.jpg
```
- Detect faces from a video files
```
python detect.py $PATH_to_VIDEO_FILE -i -p detected
```
```
python main.py $PATH_to_VIDEO_FILE -i -p detected
```
