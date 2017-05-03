# opencv-cap

## simpleCvCap.py

This is simple OpenCV based still image capture program.

```
$ python ./simpleCvCap.py --help
Usage: simpleCvCap.py [options]

Options:
  -h, --help            show this help message and exit
  -c CAPTUREINDEX, --captureIndex=CAPTUREINDEX
                        Specify capture Index (set 0 if /dev/video0)
  -r RESOLUTION, --resolution=RESOLUTION
                        Specify resolution
  -s SKIPFRAME, --skip=SKIPFRAME
                        Specify skip frame
```

example

```
$ python ./simpleCvCap.py tmp.jpg
$ python ./simpleCvCap.py tmp.jpg --resolution=1280x720
$ python ./simpleCvCap.py tmp.jpg --resolution=1280x720 --skip=3
```
