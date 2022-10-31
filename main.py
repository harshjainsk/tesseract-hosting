import json

import pyperclip
from flask import Flask, request, jsonify, render_template, flash
import mouse
import pyautogui
from PIL import ImageGrab
import numpy as np
import cv2
import time
import pytesseract

app = Flask(__name__)
app.secret_key = "Can be set as random value"


@app.route('/')
def get_ss_to_text_to_clipboard():
    while True:
        """
            Sensing right click
        """
        if mouse.is_pressed(button='right'):
            print("right clicked")

            """
                if True:
                    press windows + shift + s
            """
            pyautogui.hotkey('win', 'shift', 's')

            mouse.wait(button='left', target_types=('up', 'down', 'double'))
            """
                Until left click is not sensed the code wont execute further
            """
            time.sleep(2)  # Look for a substitute value to handle the delay

            # Grabbing image from clipboard and converting to numpy array
            try:
                im = np.array(ImageGrab.grabclipboard())[:, :, 0:3]
                print(im.shape)
                print(type(im))
                print(im)
                # cv2.imwrite("mouse-module-output.PNG", im)

                # pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files\Tesseract-OCR\tesseract.exe"
                pytesseract.pytesseract.tesseract_cmd = "/app/.apt/usr/bin/tesseract"
                # img = cv2.imread('mouse-module-output.PNG')
                # print("image read successfully")

                np_img = 255 - im

                text = pytesseract.image_to_string(np_img, lang='eng')
                print(text)
                pyperclip.copy(text)
                # return f"{text}"

            except Exception as e:
                print("No image given as input")
                pyperclip.copy("No image given as input")
                # return "No image"


if __name__ == '__main__':
    print('Starting flask server for Grocery Store Management')
    app.run(port=5000, debug=True)

"""
    1. add error handling
    2. add right click detection for snipping ---> means if right click snesed then snip and extract
    3. javascript onClick function
    4. API call for onclick function
    5. Hosting API
"""
