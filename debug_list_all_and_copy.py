# Kiểm tra xem tất cả các subdirectories trong một directory có dạng YYYY-MM-DD_HH-MM-SS không tại depth = 4
# Nghĩa là {input_path}/*/*/*/YYYY-MM-DD_HH-MM-SS/
# Show ra các subdirectories không phải dạng YYYY-MM-DD_HH-MM-SS

import os
import glob
import argparse
import re

# Create argument parser
parser = argparse.ArgumentParser(description="Debug check folder")
parser.add_argument("--input_path", type=str, help="Input path")
parser.add_argument("--output_path", type=str, help="Depth")
args = parser.parse_args()


# Count all trajectory in a directory

def debug_count_and_copy(input_path, output_path):
    count_all = 0
    # List all sub directories in input_path have ".*traj[0-9]" pattern
    paths = glob.glob(f'{input_path}/**/traj[0-9]*', recursive=True)
    print(len(paths))
    
debug_count_and_copy(args.input_path, args.output_path)