# opencv-haarcascade

Basics


Object Detection using Haar feature-based cascade classifiers is an effective object detection method proposed by Paul Viola and Michael Jones in their paper, "Rapid Object Detection using a Boosted Cascade of Simple Features" in 2001. It is a machine learning based approach where a cascade function is trained from a lot of positive and negative images. It is then used to detect objects in other images.

Creating cascade classifiers


Haar classifiers in opencv is a simple yet tricky method.
We often face problem in opencv for classifying objects and there are not image classifier of every object on internet. So the best method is to create our own classifier in opencv. The classification requires a large number of negative and positive images. Negatives do not contain the required object whereas the positives are the one that contain the object to be detected.

Softwares required 

We require the following softwares for the creation of your own classifier

1) OpenCV: The version I used is 3.4
2) Python: The version I used is 3.6(Spyder)

Moreover we require a webcam (of course :p)

Downloading the images

The first step is to take a clear picture of the object to be classified.

The size should not be very large as it takes larger time for the computer to process. I took 50 by 50 size for watch and 100 by 50 for calculator.
Then we download the negative and positive images. We can find them online. But we use the python code to download images from 'http://image-net.org'. There should be around 2000 neg images.
Then we convert the images to grayscale and to a normal size. This is also implemented in the code. The code also removes any faulty image.
By now our directory should contain the object image e.g watch5050.jpg neg images folder bg.txt file empty data folder
If data folder is not created, do it manually.

The python code is provided in the the .py file in grab_neg_images dir
 I am using Anaconda enviroment. So we need to open anaconda prompt as admin and go to our working dir and type the following commands
 
 opencv_createsamples -img watch5050.jpg -bg bg.txt -info info/info.lst -pngoutput info -maxxangle 0.5 -maxyangle 0.5 -maxzangle 0.5 -num 1950 
 
 This command is for creating the positive samples of the object 1950 exactly. Now your folder should contain a neg images folder, an info folder, a bg.txt file and an empty data folder.
 
 Now we need to create the positive vector file that provides the path to the positive images decsription file

Use the following command:
opencv_createsamples -info info/info.lst -num 1950 -w 40 -h 40 -vec positives.vec

By now the contents of the directory must be as follows:

--neg

----negimages.jpg

--info

--data

--positives.vec

--bg.txt

--watch5050.jpg(the required object image)

Training the classifier:
The final and the longest step.

Now we need to train the classifier and obtain the xml file.

Use the following command

opencv_traincascade -data data -vec positives.vec -bg bg.txt -numPos 1800 -numNeg 900 -numStages 10 -w 40 -h 40

One problem I faced during training is that it always ended the training saying required false alarm rate achieved.This happens because the classifier has reached its optimal and cannot be trained further. To avoid this increase the features of the image by increasing the pixels( i.e. the width and height) but increasing the pixel will lead to more training time and memory consumption. So decide wisely the pixels.

Now haarcascade is created It takes about few hours to complete. Open the data folder there you will find cascade.xml. This is the classifier that has been created and will be used to classify. You can rename it whatever you want.


Testing the Classifier:

After creating the classifier, lets check whether the classifier is working or not. Place the xml file in working directory of your python file.

I have created a few classifier like of calculator and watch. In the haarcascade directory all the neccessary xml files and python files are there.
 
 
 /// I would like to thanks Sentdex for this project. A lot of help has been taken from him. He has a youtube channel named sentdex. He trained the cascades on linux and I used Windows. Hence I faced a lot of problems while training. I have tried to simplify the steps as much as possible here. Thanks.///
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
