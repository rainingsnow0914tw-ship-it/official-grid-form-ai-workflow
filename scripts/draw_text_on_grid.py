from pathlib import Path
from PIL import Image, ImageDraw, ImageFont


def draw_text_on_grid(
    image_path: str,
    output_path: str,
    text_lines: list[str],
    start_x: int,
    start_y: int,
    cell_width: int,
    cell_height: int,
    font_path: str,
    font_size: int = 24,
) -> None:
    image = Image.open(image_path).convert("RGB")
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(font_path, font_size)

    for row_idx, line in enumerate(text_lines):
        for col_idx, ch in enumerate(line):
            x = start_x + col_idx * cell_width + cell_width // 2
            y = start_y + row_idx * cell_height + cell_height // 2

            bbox = draw.textbbox((0, 0), ch, font=font)
            text_w = bbox[2] - bbox[0]
            text_h = bbox[3] - bbox[1]

            draw.text(
                (x - text_w / 2, y - text_h / 2),
                ch,
                font=font,
                fill="black",
            )

    image.save(output_path)
    print(f"Saved: {output_path}")


if __name__ == "__main__":
    sample_lines = [
        "這是一個示例文字行",
        "每格一字逐格填入中",
    ]

    draw_text_on_grid(
        image_path="output/png_pages/page_001.png",
        output_path="output/drawn_pages/page_001.png",
        text_lines=sample_lines,
        start_x=200,
        start_y=300,
        cell_width=32,
        cell_height=38,
        font_path="fonts/NotoSansCJK-Regular.ttc",
        font_size=24,
    )
