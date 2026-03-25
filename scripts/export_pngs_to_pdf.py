from pathlib import Path
from PIL import Image


def export_pngs_to_pdf(input_dir: str, output_pdf: str) -> None:
    paths = sorted(Path(input_dir).glob("*.png"))
    if not paths:
        raise FileNotFoundError("No PNG files found.")

    images = [Image.open(p).convert("RGB") for p in paths]
    first, rest = images[0], images[1:]

    first.save(output_pdf, save_all=True, append_images=rest)
    print(f"Saved PDF: {output_pdf}")


if __name__ == "__main__":
    export_pngs_to_pdf("output/drawn_pages", "output/final_output.pdf")
