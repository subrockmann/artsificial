#!python

import argparse

def get_args():
    '''
    Gets the arguments from the command line.
    '''
    parser = argparse.ArgumentParser("Run inference")

    # -- Add required and optional groups
    parser._action_groups.pop()
    required = parser.add_argument_group('required arguments')
    optional = parser.add_argument_group('optional arguments')

    # -- Create the arguments
    required.add_argument("--model", help=model_desc, required=True)
    
    optional.add_argument("--fps", default=15, type=int)
    optional.add_argument("--seconds", default=10, type=int)
    optional.add_argument("--img_size", default=200, type=int)
    optional.add_argument("--scale", default=0.3, type=float)
    optional.add_argument("--pattern_change_speed", default=0.5, type=float)
    optional.add_argument("--progress", action="store_true")
    optional.add_argument("--save_frames", action="store_true")
    
    args = parser.parse_args()

    return args


def main():
    args = get_args()


if __name__ == "__main__":
    main()