# Image Resizer

Script resizes chosen image with desired

# Installation

Run from console

`git clone https://github.com/moofspb/12_image_resize.git`

# Requirements

Script works with python 3, python 2 is not supported.

Install requirements running `pip install -r requirements.txt`

# Arguments

Positional arguments:

`input_path` - Path to a image file.

Optional arguments:

`'-w', '--width'` - Width of the output image.

`'-he', '--height'` - Height of the output image.

`'-s', '--scale'` - Scale of the output image. Scale can't be set
 with width/height at the same time.

`'-o', '--output_dir'` - Directory where output image will be saved.
 If isn't set image will be saved in the input path..

# Usage

Run the script from a command line, for example:

`python3 image_resize.py /home/user/test.jpg -s=2`

# Help

You can get help running `python3 image_resize.py -h`