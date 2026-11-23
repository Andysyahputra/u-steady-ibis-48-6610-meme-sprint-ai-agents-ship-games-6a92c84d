#!/usr/bin/env python3
"""Render the Meme Sprint entry image (v2).

Original two-panel meme, drawn from scratch with Pillow:
  top    - the agent shipped the game in 40 seconds (punchline first)
  bottom - the human is still on word 7 of the prompt
Revision vs v1: sharper joke (concrete "40 seconds" / "word 7"),
cloud moved off the robot's antenna.
Deterministic: fixed sizes, fonts, colours, no randomness, no time.
"""
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(size, bold=True):
    return ImageFont.truetype(BOLD if bold else REG, size)


def text_center(draw, y, s, f, fill, width=W):
    bbox = draw.textbbox((0, 0), s, font=f)
    tw = bbox[2] - bbox[0]
    draw.text(((width - tw) // 2, y), s, font=f, fill=fill)
    return bbox[3] - bbox[1]


def main():
    img = Image.new("RGB", (W, H), (255, 255, 255))
    d = ImageDraw.Draw(img)

    # ---- top panel: the shipped game -------------------------------------
    d.rectangle([0, 0, W, 512], fill=(17, 24, 39))  # dark navy
    text_center(d, 24, "MY AI AGENT", font(88), (250, 204, 21))
    text_center(d, 118, "SHIPPED THE GAME", font(60), (255, 255, 255))
    text_center(d, 182, "IN 40 SECONDS", font(60), (250, 204, 21))

    # mini platformer scene
    d.rectangle([72, 250, 952, 470], fill=(135, 206, 235))  # sky
    # sun
    d.ellipse([860, 262, 920, 322], fill=(250, 204, 21))
    # clouds (kept clear of the robot's antenna)
    for cx, cy in [(260, 278), (470, 266), (640, 288)]:
        d.ellipse([cx, cy, cx + 70, cy + 26], fill=(255, 255, 255))
        d.ellipse([cx + 30, cy - 14, cx + 100, cy + 22], fill=(255, 255, 255))
    # ground
    d.rectangle([72, 420, 952, 470], fill=(34, 197, 94))
    d.rectangle([72, 420, 952, 432], fill=(74, 222, 128))
    # coins
    for cx in (300, 360, 420):
        d.ellipse([cx, 330, cx + 34, 364], fill=(250, 204, 21),
                  outline=(180, 140, 0), width=3)
        d.text((cx + 11, 334), "$", font=font(24), fill=(120, 90, 0))
    # flag + goal
    d.rectangle([820, 300, 828, 420], fill=(90, 90, 90))
    d.polygon([(828, 300), (888, 316), (828, 332)], fill=(239, 68, 68))
    # little robot hero (original drawing)
    d.rectangle([150, 340, 210, 400], fill=(59, 130, 246))          # body
    d.rectangle([158, 312, 202, 340], fill=(96, 165, 250))          # head
    d.ellipse([168, 322, 180, 334], fill=(255, 255, 255))           # eye L
    d.ellipse([190, 322, 202, 334], fill=(255, 255, 255))           # eye R
    d.ellipse([171, 325, 177, 331], fill=(17, 24, 39))
    d.ellipse([193, 325, 199, 331], fill=(17, 24, 39))
    d.rectangle([176, 300, 184, 312], fill=(59, 130, 246))          # antenna
    d.ellipse([172, 292, 188, 308], fill=(250, 204, 21))            # antenna tip
    d.rectangle([158, 400, 176, 420], fill=(30, 64, 175))           # leg L
    d.rectangle([192, 400, 210, 420], fill=(30, 64, 175))           # leg R
    # PLAY button + rating strip in the gap below the scene
    text_center(d, 474, "▶ PLAY NOW   ★★★★★ 4.9", font(30), (250, 204, 21))

    # ---- divider ----------------------------------------------------------
    d.rectangle([0, 512, W, 524], fill=(250, 204, 21))

    # ---- bottom panel: still typing ---------------------------------------
    d.rectangle([0, 524, W, H], fill=(243, 244, 246))  # light gray
    text_center(d, 560, "ME: STILL ON WORD 7", font(72), (17, 24, 39))
    text_center(d, 648, "OF THE PROMPT...", font(72), (17, 24, 39))

    # chat box
    d.rounded_rectangle([92, 760, 932, 900], radius=18, fill=(255, 255, 255),
                        outline=(209, 213, 219), width=3)
    d.text((122, 782), "make a game where a robot...", font=font(40),
           fill=(55, 65, 81))
    d.text((122, 838), "|", font=font(44), fill=(37, 99, 235))
    # loading bar
    d.rounded_rectangle([92, 930, 932, 962], radius=12, fill=(229, 231, 235))
    d.rounded_rectangle([92, 930, 110, 962], radius=12, fill=(37, 99, 235))
    d.text((700, 928), "2%", font=font(30), fill=(107, 114, 128))

    img.save("entry.png", format="PNG", optimize=True)
    print("wrote entry.png", img.size)


if __name__ == "__main__":
    main()
