#!/Users/loukielhorn/anaconda3/bin/python3

import struct
import sys
import json
import logging
import os

python_executable_path = os.path.dirname(sys.executable)
libraries_path = os.path.join(python_executable_path, 'lib', 'site-packages')
sys.path.append(libraries_path)

logging.basicConfig(filename='native_messaging_host.log', level=logging.DEBUG)

try:
    logging.debug('Versuche externe Bibliotheken zu importieren.')
    logging.debug(python_executable_path)
    logging.debug(libraries_path)
    import base64
    import numpy as np
    import cv2
    from Algo.text_algo import change_text
    from Algo.image_algo import use_alog_on_image, save_image
    logging.debug('Externe Bibliotheken erfolgreich importiert.')
except Exception as e:
    logging.error(f'Fehler beim Importieren von einer externen Bibliothek: {str(e)}')


def send_message(message):
    # Convert the message to a JSON-formatted string.
    json_message = json.dumps(message)

    # Write message size.
    sys.stdout.buffer.write(struct.pack('I', len(json_message)))

    # Write the message itself.
    sys.stdout.buffer.write(json_message.encode('utf-8'))
    sys.stdout.flush()


def base64_to_cv2(base64_string):
    # Decode the base64 string into bytes
    img_data = base64.b64decode(base64_string)

    # Convert bytes to a NumPy array
    np_arr = np.frombuffer(img_data, np.uint8)

    # Decode the NumPy array into an OpenCV image
    img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

    return img


# Read the message length (first 4 bytes).
message_length_bytes = sys.stdin.buffer.read(4)
if len(message_length_bytes) == 0:
    sys.exit(0)

# Unpack message length as 4-byte integer.
message_length = struct.unpack('I', message_length_bytes)[0]

# Read the text (JSON object) of the message.
message_raw = sys.stdin.buffer.read(message_length).decode('utf-8')
message_json = json.loads(message_raw)


if 'text' in message_json:
    text = message_json["text"]

    # Send the response directly as a JSON object.
    response = {"text_response": change_text(text)}
    send_message(response)
elif 'image' in message_json:
    image_base64 = message_json["image"]
    image = base64_to_cv2(image_base64)
    modified_image = use_alog_on_image(image)
    modified_image_path = save_image(modified_image)

    # Send the response directly as a JSON object.
    response = {"image_response": change_text(modified_image_path)}
    send_message(response)
