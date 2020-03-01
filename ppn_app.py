#!python

import argparse

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


def main():
    args = get_args()


if __name__ == "__main__":
    main()