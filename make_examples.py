"""Создать две картинки для проверки программы."""

from pathlib import Path

from PIL import Image


folder = Path(__file__).resolve().parent
Image.new("RGB", (256, 256), (40, 170, 70)).save(folder / "ok.png")
Image.new("RGB", (256, 256), (220, 45, 45)).save(folder / "defect.png")
