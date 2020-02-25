>#  artsificial
## Generating art with neural networks

This project uses the [OpenVINO™ toolkit](https://docs.openvinotoolkit.org/) to deploy a deep learning solution for Art Generation 
with Compositional Pattern Producing Networks, while exploring the possibilities for the different patterns and color palletes that 
can be produced.

### Project's story

All of us had the chance to be selected for the Intel® Edge AI Scholaship Challenge at Udacity.
Before that we had won the Secure and Private AI Scholarship Challenge by Facebook AI and were selected for a follow up 
Nanodegree Scholarship at Udacity, during which we successfuly graduated from the Computer Vision Nanodegree.

During the Intel® Edge AI Scholaship Challenge, along with other scholars from the Secure and Private AI Scholarship, we formed a study group on Slack and kept communicating and sharing ideas, resources and concerns.

After the announcement for the [Prject Showcase Challenge](https://sites.google.com/udacity.com/intel-edge-ai-scholarship/community/project-showcase?authuser=0), we started exploring the idea of creating a project in the Arts category.
A source of inspiration was the [Computer Vision Art Gallery](https://computervisionart.com/), along with other other impressive projects of Contemporary Art which use AI.

We were impressed by the Compositional Pattern Producing Networks and, since we hadn't any previous experience, we started learning more about them from the published resources while exploring their possibilities. Finally, we agreed to use as a base source a [PyTorch implementation of a CPPN](https://github.com/jtguibas/cppn-art), and modify it according to our desired outputs.

### Tests & Example Outputs

![GIF with Compositional Pattern Images](images/Webp.net-gifmaker.gif)

## Getting Started

In order to get a copy of this project up and running on your local machine for development and testing purposes, please follow the instructions below.

### Prerequisites

#### For Windows 10

* Microsoft Visual Studio* with C++ 2019, 2017, or 2015 with MSBuild
* CMake 3.4 or higher 64-bit
* Python 3.6.5 64-bit

### Installation

* Install the respective Intel® Distribution of OpenVINO™ toolkit for Windows 10 / Mac OS / Linux, following all the required steps on the [documentation guide](https://docs.openvinotoolkit.org/latest/index.html).

## How to run the project

## Built with

* [PyTorch](https://pytorch.org/) - For AI model development
* [ONNX](https://onnx.ai/) - To convert the model for use with the Inference Engine
* [OpenVINO™ toolkit](https://docs.openvinotoolkit.org/) - For the application development


## Contributing

Please read CONTRIBUTING.md for details on our code of conduct, and the process for submitting pull requests to us.

## Authors

>[Evi Giannakou](https://github.com/evigian),
>[Susanne Brockmann](https://github.com/subrockmann),
>[Kapil Chandorikar](https://github.com/kapilchandorikar)

> Connect with us on LinkedIn

## Licence

This project is licensed under the MIT License - see the LICENSE.md file for details

## Aknowledgements

* Intel® Edge AI Scholaship Challenge at Udacity, for the chance to study within an amazing community.
* John Guibas, for his PyTorch implementetion of CPPNs.
* Mariia Denysenko, for the administration of the #sg_spaic and the presentation of CPPNs to the study group.


