# '''
# ######################
# Courtesy: Special thanks codeBasic youtube channel for this knowledgeable DataScience Series
#
# Tutorial (youtube):https://www.youtube.com/playlist?list=PLeo1K3hjS3uvaRHZLl-jLovIjBP14QTXc
# Project-code(gitHub): https://github.com/codebasics/py/tree/master/DataScience/CelebrityFaceRecognition
#
# Disclaimer: I don't own the rights of this code/project. The code written is followed as shown
#            in the tutorial with reference to above.
#            P.S.: There are some changes in names of files and variables for personal reference
#            only, In case you are copy pasting this code , please look out for the syntax.
# ######################
#
# '''
import numpy as np
import pywt
import cv2

def w2d(img, mode='haar', level=1):
    imArray = img
    #Datatype conversions
    #convert to grayscale
    imArray = cv2.cvtColor( imArray,cv2.COLOR_RGB2GRAY )
    #convert to float
    imArray =  np.float32(imArray)
    imArray /= 255;
    # compute coefficients
    coeffs=pywt.wavedec2(imArray, mode, level=level)

    #Process Coefficients
    coeffs_H=list(coeffs)
    coeffs_H[0] *= 0;

    # reconstruction
    imArray_H=pywt.waverec2(coeffs_H, mode);
    imArray_H *= 255;
    imArray_H =  np.uint8(imArray_H)

    return imArray_H