# Generative Adversarial Networks (GANs)
Notebooks for different variations of GAN networks. The purpose of this repository is primarily for self education. 
## GANs for MNIST
I developed two GANs in collaboration with my peer Búgvi Benjamin Magnussen for a university project.  Both versions are implemented exclusively with barebone tensorflow (no keras).
The first version uses dense networks for both the discriminator and the generator network. (Closely follows the original GAN paper https://arxiv.org/abs/1406.2661)  
The second version is a DCGAN inspired by the official tensorflow tutorial. (https://www.tensorflow.org/tutorials/generative/dcgan)
![DCGAN with 500 epochs](https://github.com/NikolajBl/GAN/blob/main/gifs/mnist.gif)
- DCGAN across 500 epochs using the MNIST dataset 
## Advanced DCGAN with Keras for generating drawn Faces
This version is more sophisticated compared to the other two versions. It has many more layers and uses residual blocks. (inspired by https://arxiv.org/pdf/1609.04802.pdf)
It also generates images in higher resolution (256x256).  
The dataset used for training is selfmade. I primarily used faces from Kyoto Animations. The dataset can not be shared due to copyright reasons.  
![Advanced DCGAN with 120 epochs](https://github.com/NikolajBl/GAN/blob/main/gifs/face.gif)  
- Advanced  DCGAN across 120 epochs using a custom face dataset.  

Note that unfortunately the colouring is off as i accidentally saved the images in grayscale. Rerunning the network however is quite tedious (4 minutes per epoch), so I decided not to. 
