**Introduction:**
 This Model has been initially build and trained on local windows 10 machine equipped with 12GB RAM (No GPU and TPU)and will be trained later on TPU via Colab

Model has been trained to detect the following objects from street:

- lane
- pedestrian
- sidewalk
- vehicle  
- 

**Local Environment Specifications**

- Windows 10 Enterprise
- python version(3.8.8)
- TensorFlow version(2.4.0) (Facing issues with 2.4.1)  
- 

**prerequisites**

- Installing Tensorflow object Detections API&#39;s you can refer to below link [Installation Guide](http://https/tensorflow-object-detection-api-tutorial.readthedocs.io/en/latest/install.html)
- Install wget on your machine to clone github repository

Note: As part of this installation many other dependencies need to be installed as well, please make sure to go through all installation steps, they are bit long and may you would face some challenges  

<br>

![Street Views](https://github.com/halhwadi/Instance-Segmentation---Tensorflow-Object-Detection-API-s/blob/main/videos/segemntation.gif)

<br>

**Clone the Github repository**  

type thr line of code in anaconda prompt  

git clone https://github.com/halhwadi/Instance-Segmentation---Tensorflow-Object-Detection-API-s.git  

<br>

**Downloading Images**  

 street images have been downloaded by using google map street view and stored under this path (images/resize)
 only 30 images have been downloaded to avoid overloading our modest machine  
 
<br> 

**Resizeing**

IF your workstation is not equipped with high RAM its highly recommended to resize the images
**Note: In pipleline.config file the size in image resizer should be match with resized images you use in this step**

You can resize the images in anaconda prompt by running the following line of code(make sure your images are available under
 this path (images/resize)...Width height

**resize.py 400 300 images/resize/**  


<br>

**Annotations**  


In this tutorial we will use [Labelme tools](https://github.com/wkentaro/labelme), you can install by running (conda install -c conda-forge labelme)
 Once its installed please type labelme on Anaconda prompt to open it

**Note: please avoid using circle as we faced issue while running create\_coco\_tf\_record script to create tfrecord, this script throws error when number of annontation points is 4**

Once annotation is done, please make sure to split images between train and test by moving them to &#39;images\train&#39; and &#39;images\test&#39; folders

**Note: make sure to move the images and their corresponding json files as well**  

<br>

**Creating COCO files**

We need to create the json files, one for training images and the other one for testing images, In order to create these files &quot;labels.txt&quot; files need to be generated, its txt file and you can create it manually ( **Note the ordering of classes in labels.txt file should be the same oredering in labelme desktop screen, you can review the labels.txt file for more details** )

type the following commands in Anaconda prompt:

python labelme2coco.py images\train train --labels labels.txt

python labelme2coco.py images\test test --labels labels.txt

**Sample of Annotated Images**

![](https://github.com/halhwadi/Instance-Segmentation---Tensorflow-Object-Detection-API-s/blob/main/images/Annoated.png)  

<br>

**Creating Label map:**

Refer to tutorial notebook for more details  

<br>

**Creating tfrecords:**
 running the below command in Anaconda prompt:

**python create\_coco\_tf\_record.py --logtostderr --train\_image\_dir=images/train --test\_image\_dir=images/test --train\_annotations\_file=train/annotations.json --test\_annotations\_file=test/annotations.json --output\_dir=tfrecords --include\_masks**  

<br>

**Downloading the mask\_rcnn model from Tensorflow model zoo:**

Refer to tutorial notebook for more details  

<br>

**Preparing the Configuration file pipeline.config**

**Its recommend to use the same pipeline config file under model folder because many changes have been applied to this file to facilitate the training on windows machine with modest RAM (Example: number of batches set to 1), you can modify the number of classes and keep the rest of details as is, otherwise you can use the master file from Tensorflow zoo and apply the required changes by your self(**Refer to tutorial notebook for more details**)**  

<br>

**Training**

Running the below line in Anaconda prompt:

**python model\_main\_tf2.py --model\_dir=model --pipeline\_config\_path=model\pipeline.config --num\_train\_steps=3000**  


<br>

**running in Anaconda prompt:**

the below line of code:
**tensorboard --logdir=model\train**

![](https://github.com/halhwadi/Instance-Segmentation---Tensorflow-Object-Detection-API-s/blob/main/images/tensorboard.jpg)  

<br>

**Inference:**

Refer to tutorial notebook for more details  

**Author:**  

**Husam Alhwadi**  
**halhwadi@yahoo.com**
