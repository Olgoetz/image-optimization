import unittest
import pathlib
import os
from PIL import Image
from src.model import resize
# Current directory
HERE = pathlib.Path(__file__).resolve().parent


class ApplicationTests(unittest.TestCase):
    def test_resize(self):
        input_path = os.path.join(f"{HERE}/pics_src", "")
        output_path = os.path.join(f"{HERE}/pics_out", "")

        # Test fixed height
        resize(input_path, output_path, fixed_height=500,
               fixed_width=None, quality=90)

        for img in os.listdir(output_path):
            height = Image.open(output_path+img).size[1]
            self.assertEqual(height, 500)

        # Test fixed width
        resize(input_path, output_path, fixed_height=None,
               fixed_width=300, quality=90)

        for img in os.listdir(output_path):
            width = Image.open(output_path+img).size[0]
            self.assertEqual(width, 300)

        # Test fixed width AND fixed height
        resize(input_path, output_path, fixed_height=400,
               fixed_width=300, quality=90)

        for img in os.listdir(output_path):
            width = Image.open(output_path+img).size[0]
            height = Image.open(output_path+img).size[1]
            self.assertEqual(height, 400)
            self.assertEqual(width, 300)
