#!python

import os
import sys
import cv2
import math
import argparse
import datetime
import numpy as np
import logging as log
import matplotlib.pyplot as plt
from openvino.inference_engine import IENetwork, IECore, IEPlugin


def get_args():
    '''
    Gets the arguments from the command line.
    '''
    parser = argparse.ArgumentParser("Run inference")
    # -- Create the descriptions for the commands
    model_desc = "The location of the model XML file"
    
    fps_desc = "Number of Frames Per Second for the video"
    seconds_desc = "The duration of the video in seconds"
    img_size_desc = "The width or height for the frame to be generated"
    scale_desc = "Scale factor for inputs"
    p_c_speed_desc = "The rate of flow/change of the pattern"
    progress_desc = "Display the progress of frame generation"
    save_frames_desc = "Save the individual frame generated as PNG images"

    # -- Add required and optional groups
    parser._action_groups.pop()
    required = parser.add_argument_group('required arguments')
    optional = parser.add_argument_group('optional arguments')

    # -- Create the arguments
    required.add_argument("--model", help=model_desc, required=True)
    
    optional.add_argument("--fps", help=fps_desc, default=15, type=int)
    optional.add_argument("--seconds", help=seconds_desc, default=10, type=int)
    optional.add_argument("--img_size", help=img_size_desc, default=200, type=int)
    optional.add_argument("--scale", help=scale_desc, default=0.3, type=float)
    optional.add_argument("--pattern_change_speed", help=p_c_speed_desc, default=0.5, type=float)
    optional.add_argument("--progress", help=progress_desc, action="store_true")
    optional.add_argument("--save_frames", help=save_frames_desc, action="store_true")
    
    args = parser.parse_args()

    return args



class Network:
    '''
    Load and store information for working with the Inference Engine,
    and any loaded models.
    '''

    def __init__(self):
        self.plugin = None
        self.network = None
        self.input_blob = None
        self.output_blob = None
        self.exec_network = None
        self.infer_request = None

    def load_model(self, model, device="GPU"):
        '''
        Load the model given IR files.
        Defaults to CPU as device for use in the workspace.
        Synchronous requests made within.
        '''
        model_xml = model
        model_bin = os.path.splitext(model_xml)[0] + ".bin"

        # Initialize the plugin
        self.plugin = IECore()

        # Read the IR as a IENetwork
        self.network = IENetwork(model=model_xml, weights=model_bin)

        # Load the IENetwork into the plugin
        self.exec_network = self.plugin.load_network(
            self.network, device_name=device)

        # Get the input layer
        self.input_blob = next(iter(self.network.inputs))
        self.output_blob = next(iter(self.network.outputs))

        return

    def get_input_shape(self):
        '''
        Gets the input shape of the network
        '''
        return self.network.inputs[self.input_blob].shape

    def async_inference(self, image):
        '''
        Makes an asynchronous inference request, given an input image.
        '''
        self.exec_network.start_async(
            request_id=0, inputs={self.input_blob: image})
        return

    def wait(self):
        '''
        Checks the status of the inference request.
        '''
        status = self.exec_network.requests[0].wait(-1)
        return status

    def extract_output(self):
        '''
        Returns a list of the results for the output layer of the network.
        '''
        return self.exec_network.requests[0].outputs[self.output_blob]


def main():
    args = get_args()


if __name__ == "__main__":
    main()