import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
import glob

#def augment_each_image():



if __name__=="__main__":
    all_images = np.array(
        [cv2.cvtColor(cv2.imread(image), cv2.COLOR_RGB2GRAY) for image in glob.glob("../../demo/*.jpg")])
    image=all_images[0,:,:]
    fig=plt.imshow(image,cmap='gray')
    plt.show()
    cropped_image=image[1:400,100:400]
    fig=plt.imshow(cropped_image,cmap='gray')
    plt.show()