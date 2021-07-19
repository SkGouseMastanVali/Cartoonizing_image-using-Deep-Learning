# Cartoonizing_image

Its a deep learning project with the implementation of CNN ,GAN, Whitebox Representation. In this project we have to upload a picture as a input, once you upload and hit the cartoonize button, then it will perform the model and display the cartoonized picture.

In this project we have used the GAN (Generative Adversial Network),GAN has been widely used in conditional image generation tasks, such as image inpainting , style transfer , image cartoonization, image colorization. GAN’s most advanced method of neural networks. In this we are having two main neural networks that is generator and discriminator. GAN’s networks mainly used for generate synthetic information or fake data .here Generator main objective is to generate fake data from noise data .it is acts like DCNN network ,it will generate the images or text or videos. So, we can say that CNN is the one of the part of GAN’s network , where as GANs having both the networks CNN ad DCNN .

we have collected the the different types of images fron different datasets. we collected celebrities images from CelebA dataset, and remaining images fron DIV2k dataset and some more images from Microsoft COCO dataset. all these datasets are available in kaggle website.

we have implemented White Box Representation to convert the image into cartoon, which contain the surface,structural and textual representation. all these are used to smoothening the surface and edges, enhancing the colloring effects, and converting into black and white format and gives the finishing touch of cartoon effect.

==========================
HOW TO EXECUTE THE PROJECT 
==========================

To execute this project First we need to open the command promt and naviagte to the project folder where app.py file exists. Here we need to execute two commands to run this project.

First we need to run this command 'pip install -r requirements.txt', by running this command we get the all the required packages to for this project.

Once all the required packages are installed then run the command 'python app.py', then server get starts

The moment server gets starts, Go to WebBrowser and enter the url 'localhost:5000',as it is the default local host for the flask. 

Now you can select your desired picture and hit the cartoon button to get the cartoonized image. 
