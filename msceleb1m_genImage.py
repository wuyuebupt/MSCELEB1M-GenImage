import os,sys
import base64
import cv2

prefix = 'images/'
if __name__ == '__main__':
    file_name = sys.argv[1]
    count =0
    with open(file_name) as infile:
        for line in infile:
            # print line
            arr = line.strip().split('\t')
            dirname = arr[0]
            # imgid = arr[1]
            imgid = str(count)
            count += 1
            faceid = arr[-3]
            rect = arr[-2]
            imgbase64 = arr[-1]
            print dirname
            # print 'freebasemid', arr[0]
            # print 'face', imgbase64
            imgdata = base64.b64decode(imgbase64)
            # mkdir
            mid_dir = prefix + dirname
            if not os.path.exists(mid_dir):
                os.makedirs(mid_dir)
            # save file
            filename = mid_dir + '/' + imgid + '_' + faceid + '.jpg'
            print filename
            with open(filename, 'wb') as f:
                f.write(imgdata)
            #  img = cv2.imread(filename)
            # cv2.imshow('abc', img)
            # cv2.waitKey()

