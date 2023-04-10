from .model import resize
import argparse
import os


def main():
    global_parser = argparse.ArgumentParser(
        prog="image-optimizer",
        description="Tool to optimize for web application & saves them as .webp file.")

    # Some arguments
    global_parser.add_argument(
        "input_path", help="Input path for files to optimize")
    global_parser.add_argument(
        "output_path", help="Output path for files to be stored")

    # Some options
    global_parser.add_argument(
        "-fh", "--fixed-height",
        type=int,
        help="Set a fixed height of the resized image, but keep the aspect ratio + "
        "(default: 1000)")
    global_parser.add_argument(
        "-fw", "--fixed-width",
        type=int,
        help="Set a fixed width of the resized image, but keep the aspect ratio")
    global_parser.add_argument("-q", "--quality",
                               type=int,
                               default=90,
                               help="Set the quality of the image reduction + "
                               "(default: 90)")

    args = global_parser.parse_args()

    input_path = os.path.join(args.input_path, "")
    output_path = os.path.join(args.output_path, "")

    # Check for mandatory option
    if args.fixed_height is None and args.fixed_width is None:

        global_parser.exit(
            1, 'You must provide a fixed height or a fixed width or both!')

    resize(input_path, output_path,
           args.fixed_height, args.fixed_iwdh, args.quality)


if __name__ == '__main__':
    main()
