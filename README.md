# Official Grid Form AI Workflow

A practical, stable workflow for handling fixed-layout, grid-based official document templates with AI.

This repository documents a repeatable solution for forms that:

- look like Word/PDF documents
- are not truly editable in normal ways
- require one character per cell
- break under copy/paste, OCR reflow, Word reflow, or PDF page merge workflows
- prioritize visual correctness over editable document structure

---

## Why this exists

Some official templates are not really "documents" in the everyday sense.

They are closer to **fixed-layout visual forms**:
- rigid grids
- one-character-per-cell constraints
- formatting-sensitive output
- high risk of corruption when treated like normal Word/PDF files

If you try the usual routes, things often break:
- Word reflow destroys alignment
- OCR preserves content but loses structure
- PDF overlay/merge works on page 1 and fails later
- text moves but the grid stays still
- multi-page output becomes unstable

The key insight is:

> **This is not a normal document-editing task.**
>  
> **It is an image-space rendering task.**

---

## Recommended workflow

### Solution S (most stable)

**PDF → PNG → draw text cell-by-cell → export back to PDF**

### Pipeline

1. Render each base PDF page to PNG
2. Measure coordinates in image space
3. Draw text into the correct grid cells
4. Export all final images back into a multi-page PDF

---

## Why this works

This avoids:

- Word/XML layout drift
- fragile copy/paste behavior in pseudo-editable templates
- PDF page object sharing bugs
- `merge_page()` resource corruption
- text/grid separation
- cross-device formatting inconsistencies

Each page is treated independently in image space, which dramatically reduces rendering instability.

---

## Best use cases

This workflow is especially suitable for:

- official grid forms
- postal/legal templates
- fixed-layout bureaucratic documents
- forms where visual correctness is more important than editable structure
- one-character-per-cell templates

---

## What not to do

Avoid treating these files as ordinary editable documents.

### Common failure routes

- Rebuilding the file as a normal Word document
- OCR and reflowing the text
- Using `copy.deepcopy(template_page)` and repeatedly merging the same PDF page object
- Using `pypdf merge_page()` as the core rendering engine for multi-page fixed-layout forms
- Moving only the text while leaving the grid unchanged

---

## Core principle

### Do not edit the monster.
### Render it.

---

## Repository structure

docs/
  problem-background.md
  common-failure-modes.md
  solution-s-image-space-rendering.md

examples/
  before_masked.png
  after_masked.png
  workflow_diagram.png

scripts/
  render_pdf_to_png.py
  draw_text_on_grid.py
  export_pngs_to_pdf.py

## Minimal prompt for new AI sessions

If you want to hand this problem to another AI or toolchain, use this prompt:

Use Solution S: render the base PDF into PNG pages with PyMuPDF/fitz, draw text cell-by-cell onto each PNG using Pillow, then export all pages back into a PDF. Measure coordinates in image space. Treat each page independently. Do not use normal Word editing logic, OCR reflow, or repeated PDF page deep-copy/merge workflows.

## Current status

This repository contains:

the problem framing
common failure modes
the stable workflow
example placeholders
starter scripts

It is intended as an open method so that this pain does not remain private expert knowledge.
