import os
import argparse
from PIL import Image


def get_script_args():
    parser = argparse.ArgumentParser(
        description="""Script resizes image with desired sizes. You can specify:
        1. Width/height only. In this case proportions will be saved.
        2. Width and height.
        3. Scale relative to input file (can be less than 1).
           If scale is specified, width/height can\'t be set.""")
    parser.add_argument('input_path', help='Path to a image file')
    parser.add_argument('-w', '--width', nargs='?', type=int, default=None,
                        help='Width of the output image')
    parser.add_argument('-he', '--height', nargs='?', type=int, default=None,
                        help='Height of the output image')
    parser.add_argument('-s', '--scale', nargs='?', type=float, default=None,
                        help='Scale of the output image')
    parser.add_argument('-o', '--output_dir', nargs='?', default=None,
                        help='Directory where output image will be saved')
    args = parser.parse_args()
    return args


def check_args(input_path, width, height, scale):
    original_image = Image.open(input_path)
    original_proportions = original_image.width / original_image.height
    if width and height:
        result_proportions = width / height
        if original_proportions != result_proportions:
            print('ATTENTION! Current proportion differs from original!')
    if scale:
        if width or height:
            raise Exception("Error! Scale and width/height can't be set at the same time!")


def resize_image(input_path, width, height, scale, output_dir):
    original_image = Image.open(input_path)
    result_width, result_height = get_sizes(input_path, width, height, scale)
    result_image = original_image.resize((result_width, result_height))
    result_path = get_result_path(input_path, result_width, result_height, output_dir)
    return result_image, result_path


def get_sizes(input_path, width, height, scale):
    original_image = Image.open(input_path)
    original_proportions = original_image.width / original_image.height
    if scale:
        return int(original_image.width * scale), int(original_image.height * scale)
    if width and height:
        return width, height
    if width:
        return width, int(width / original_proportions)
    if height:
        return int(height * original_proportions), height


def get_result_path(input_path, width, height, output_dir):
    original_dir, original_name = os.path.split(input_path)
    name, extension = original_name.split('.')
    result_name = '{}__{}x{}.{}'.format(name, width, height, extension)
    if not original_dir:
        return result_name
    if not output_dir:
        return '{}/{}'.format(original_dir, result_name)

    else:
        return '{}/{}'.format(output_dir, result_name)


def save_image(image_data):
    image, path = image_data
    image.save(path)


if __name__ == '__main__':
    params = get_script_args()
    input_path = params.input_path
    width = params.width
    height = params.height
    scale = params.scale
    output_dir = params.output_dir
    check_args(input_path, width, height, scale)
    new_image = resize_image(input_path, width, height, scale, output_dir)
    save_image(new_image)
