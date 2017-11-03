import argparse

from src.real_time_detect import detect

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('video_file', nargs='*')
    parser.add_argument('-i', '--images', action='store_true',
                        help='save images with detected face rectangle frame by frame')
    parser.add_argument('-p', '--prefix', help='prefix of detected output image files')
    parser.add_argument('-q', '--quiet', action='store_true', help='if set, will not show real time result window')
    argv = parser.parse_args()

    detect(video_file=argv.video_file, save_image=argv.images, prefix=argv.prefix, quiet=argv.quiet)
