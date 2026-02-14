from PIL import Image, ImageDraw, ImageFont
import os

def generate_thumbnail(title, image_path, output_path="output/thumbnail.jpg"):
    os.makedirs("output", exist_ok=True)

    img = Image.open(image_path).convert("RGB")
    img = img.resize((1280, 720))  

    draw = ImageDraw.Draw(img)

    overlay = Image.new("RGBA", img.size, (0, 0, 0, 120))
    img = Image.alpha_composite(img.convert("RGBA"), overlay)

    draw = ImageDraw.Draw(img)

    try:
        font = ImageFont.truetype(os.path.join("fonts","BrainzoopersonaluseBold-p7mLO.otf"), 80)

    except Exception :
        font = ImageFont.load_default()

    lines = []
    words = title.split()
    line = ""
    for word in words:
        if len(line + word) < 25:
            line += word + " "
        else:
            lines.append(line)
            line = word + " "
    lines.append(line)

    y_text = 250
    for line in lines:
        bbox = draw.textbbox((0, 0), line, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        x_text = (1280 - text_width) / 2
        draw.text((x_text, y_text), line, font=font, fill="white")
        y_text += text_height + 15

    img.convert("RGB").save(output_path)
    print(f"[INFO] Thumbnail saved at {output_path}")

    return output_path