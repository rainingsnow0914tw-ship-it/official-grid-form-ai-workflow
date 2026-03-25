# Solution S: Image-Space Rendering

Solution S is the most stable workflow we found for fixed-layout, grid-based official forms.

## Definition

**PDF → PNG → draw text cell-by-cell → export back to PDF**

---

## Why this is the recommended approach

This workflow avoids the most fragile parts of traditional document processing:

- Word reflow
- XML-style template internals
- PDF page object sharing
- multi-page `merge_page()` corruption
- OCR structure loss

Instead, it treats each page as an independent visual canvas.

---

## Workflow

### Step 1: Render base PDF pages to PNG
Use PyMuPDF (`fitz`) to render each page into an image.

### Step 2: Measure coordinates in image space
Find the grid origin, cell width, and cell height directly on the image.

### Step 3: Draw text cell-by-cell
Use Pillow to draw each character into the center of the correct grid cell.

### Step 4: Export all pages back into a PDF
Combine the final PNG pages into a single multi-page PDF.

---

## Why it is stable

Because each page is processed independently in image space:

- no shared PDF page resources
- no indirect object reuse
- no font/XObject merge collisions
- no visual drift from document reflow

This dramatically reduces the chance of page-to-page corruption.

---

## Recommended tools

### PyMuPDF (fitz)
Use for:
- rendering PDF pages into images

### Pillow (PIL)
Use for:
- drawing characters into the correct cells
- handling image composition

### CJK fonts
Use stable CJK fonts for Chinese/Japanese/Korean output.

Recommended examples:
- Noto Sans CJK
- IPA Gothic

---

## When to use this approach

Use Solution S when:

- the layout is fixed
- the form is grid-based
- visual correctness matters more than editable structure
- OCR/reflow has already failed
- PDF merge workflows are unstable
- the form behaves like a visual template rather than a real editable document

---

## One-sentence rule

> If the file looks editable but behaves like a rigid printed form, render it instead of editing it.
