"""Проверка картинки: OK или DEFECT."""

import argparse
from pathlib import Path

from PIL import Image


MIN_RED_SHARE = 0.25


def is_red_pixel(pixel: tuple[int, int, int]) -> bool:
    red, green, blue = pixel
    return red >= 140 and red - green >= 50 and red - blue >= 50


def check_image(path: Path) -> str:
    with Image.open(path) as source:
        image = source.convert("RGB")
        image.thumbnail((512, 512))

    pixels = image.load()
    width, height = image.size
    red_pixels = 0

    for y in range(height):
        for x in range(width):
            if is_red_pixel(pixels[x, y]):
                red_pixels += 1

    red_share = red_pixels / (width * height)
    if red_share >= MIN_RED_SHARE:
        return "DEFECT"
    return "OK"


def main() -> None:
    parser = argparse.ArgumentParser(description="Проверить картинку на дефект")
    parser.add_argument("image", type=Path, help="путь к картинке")
    args = parser.parse_args()

    try:
        print(check_image(args.image))
    except OSError as error:
        parser.exit(1, f"Не удалось открыть картинку: {error}\n")


if __name__ == "__main__":
    main()
