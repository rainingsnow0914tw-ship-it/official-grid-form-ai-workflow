# Official Grid Form AI Workflow

A practical workflow for handling fixed-layout, grid-based official document templates with AI.

This repository documents a stable method for dealing with forms that:
- look like Word/PDF documents
- are not truly editable
- require one character per cell
- break under normal copy/paste, OCR, Word reflow, or PDF merge workflows

## Core idea

Do **not** treat these files as normal document editing tasks.

Treat them as **image-space rendering tasks**.

## Recommended workflow

PDF → PNG → draw text cell-by-cell → export back to PDF

## Why this works

This avoids:
- Word/XML layout drift
- PDF page-object sharing bugs
- merge_page resource corruption
- text-grid separation
- cross-device formatting inconsistency

## Best use case

- official grid forms
- postal/legal templates
- fixed-layout bureaucratic documents
- visually correct output prioritized over editable structure

## Status

This repo is being expanded with:
- examples
- workflow notes
- scripts
- masked before/after cases
