#!/usr/bin/env python3
import base64
from pandocfilters import toJSONFilter, Image
from PIL import Image as PILImage
import io
import os

def encode_image(key, value, format, meta):
    if key == 'Image':
        attrs, alt_text, [image_path, title] = value
        if os.path.isfile(image_path):
            with open(image_path, 'rb') as image_file:
                image_data = image_file.read()
            image_b64 = base64.b64encode(image_data).decode()
            # PILで画像ファイルの形式を確認
            image_format = PILImage.open(io.BytesIO(image_data)).format.lower()
            # 'src' 属性をBase64データに更新
            return Image(attrs, alt_text, [f"data:image/{image_format};base64,{image_b64}", title])

if __name__ == "__main__":
    toJSONFilter(encode_image)

