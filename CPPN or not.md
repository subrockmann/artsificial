## CPPN or not?
We were having a lot of controversial discussion if the code we continued to work on would classify as CPPN or not.

The code from [PyTorch implementation of a CPPN](https://github.com/jtguibas/cppn-art) implements the createInputVec(z,x,y) function that is suggested in the paper "Kenneth O' Stanley, Compositional Pattern Producing Networks: A Novel Abstraction of Development" as a starting point for CPPNs. It is then adding an additional algorithm to shift the z parameter for changing the input vector to produce a sequence of evolving images in greyscale.  

The basic characteristics of a CPPN is producing images by mutating weights and / or model architecture. As the above mentioned code only changes the inputs to the ANN but does not change the weights or the model architecture, some members of the project do not consider this code as a CPPN.

### Feasibility of running CPPNs on openVINO

It would not be feasible to run CPPNs on openVINO because this would require to create a new ONNX model and a new IR model for every image. This might be possible, but one of our project goals was running the code on Raspberry Pi with NCS2. The openVINO installation on Raspi does not contain the model optimizer. We were also concerned about the required computational resources for running a complete CPPN implementation.

### Project history (continued)
As this project had to use OpenVINO we continued to focus on exploring the possibilities of generating transforming images with one model and transforming inputs. We are using a standard multi layer neural network with linear layers and activation functions. We then initialize the weights randomly and a export the model to ONNX without doing any training with the network. Then we create a input vector that is changed through an algorithm after each inference.

The following changes were added to the original code base:
* generating RGB images
* The original code is running a complete neural network to produce a single pixel and is very slow on inference. The implementation of batch computation for pixels increase the speed but generated images that become monochrome very quickly. Therefore additional parameters to influence the image creation were added.

### Implementation on Raspberry Pi
For running the code on Raspberry Pi the following code has to be changed
```
plugin.load_model("models/ppn-model-1.xml", "MYRIAD")  # was "CPU"
```
Known issues:
* torch.onnx.export() does not work on Raspberry Pi
* Due to a known error (https://software.intel.com/en-us/node/849460) in version 2020.1 the models must be converted to the previous version of IR format: '--generate_deprecated_IR_V7'
* The generated .avi files from notebook "4 - Model 2 - Inference.ipynb" are running on Windows but not on Raspberry Pi.

### Outlook
This is a work in progress. One of our big goals is to produce generative images on Raspberry Pi in real-time.