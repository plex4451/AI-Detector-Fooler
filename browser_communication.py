#!/usr/bin/env python3
import struct
import sys
import json
from Algo.text_algo import *


def send_message(message):
    # Convert the message to a JSON-formatted string.
    json_message = json.dumps(message)

    # Write message size.
    sys.stdout.buffer.write(struct.pack('I', len(json_message)))

    # Write the message itself.
    sys.stdout.buffer.write(json_message.encode('utf-8'))
    sys.stdout.flush()


# Read the message length (first 4 bytes).
text_length_bytes = sys.stdin.buffer.read(4)
if len(text_length_bytes) == 0:
    sys.exit(0)

# Unpack message length as 4-byte integer.
text_length = struct.unpack('I', text_length_bytes)[0]

# Read the text (JSON object) of the message.
text_raw = sys.stdin.buffer.read(text_length).decode('utf-8')
text = json.loads(text_raw)["text"]

# Send the response directly as a JSON object.
response = {"response": change_text(text)}
send_message(response)
