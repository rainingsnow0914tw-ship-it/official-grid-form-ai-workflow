from pathlib import Path
import fitz  # PyMuPDF


def render_pdf_to_png(pdf_path: str, output_dir: str, dpi: int = 200) -> None:
    output = Path(output_dir)
    output.mkdir(parents=True, exist_ok=True)

    doc = fitz.open(pdf_path)
    scale = dpi / 72.0
    matrix = fitz.Matrix(scale, scale)

    for i, page in enumerate(doc):
        pix = page.get_pixmap(matrix=matrix, alpha=False)
        out_path = output / f"page_{i+1:03d}.png"
        pix.save(str(out_path))
        print(f"Saved: {out_path}")


if __name__ == "__main__":
    render_pdf_to_png("input/base.pdf", "output/png_pages", dpi=200)
