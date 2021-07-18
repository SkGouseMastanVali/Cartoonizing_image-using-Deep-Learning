# Cartoonizing_image

Its a deep learning project with the implementation of CNN ,GAN, Whitebox Representation. In this project we have to upload a picture as a input, once you upload and hit the cartoonize button, then it will perform the model and display the cartoonized picture.

In this project we have used the GAN (Generative Adversial Network),GAN has been widely used in conditional image generation tasks, such as image inpainting , style transfer , image cartoonization, image colorization. GAN’s most advanced method of neural networks. In this we are having two main neural networks that is generator and discriminator. GAN’s networks mainly used for generate synthetic information or fake data .here Generator main objective is to generate fake data from noise data .it is acts like DCNN network ,it will generate the images or text or videos. So, we can say that CNN is the one of the part of GAN’s network , where as GANs having both the networks CNN ad DCNN .

we have collected the the different types of images fron different datasets. we collected celebrities images from CelebA dataset, and remaining images fron DIV2k dataset and some more images from Microsoft COCO dataset. all these datasets are available in kaggle website.

we have implemented White Box Representation to convert the image into cartoon, which contain the surface,structural and textual representation. all these are used to smoothening the surface and edges, enhancing the colloring effects, and converting into black and white format and gives the finishing touch of cartoon effect.

we can execute this project by running cartoonize.py file and enter 'cmd' command in at the cartoonize.py file url. the main file of cartoonizing is cartoonize.py file. so run the cartoon.py file and once the server started go to web browser and enter localhost:5000 and hit the enter button. now select your desired image and cartoon it instantly. 
