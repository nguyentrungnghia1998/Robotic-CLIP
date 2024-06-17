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
parser.add_argument("--depth", type=int, help="Depth")
args = parser.parse_args()


# Count all trajectory in a directory

def debug_count_all_trajectory(input_path, depth):
    count_all = 0
    paths = glob.glob(os.path.join(input_path, *("*" * (depth - 1))))
    for path in paths:
        subdirs = os.listdir(path)
        for subdir in subdirs:
            if re.match(r"\d{4}-\d{2}-\d{2}_\d{2}-\d{2}-\d{2}", subdir):
                trajectory_dir = os.path.join(path, subdir, "raw/traj_group0")
                count = len(os.listdir(trajectory_dir))
                count_all += count
                
    print(f"Total trajectory: {count_all}")
    
# Test

debug_count_all_trajectory(args.input_path, args.depth)