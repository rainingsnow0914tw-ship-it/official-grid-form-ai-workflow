# Common Failure Modes

This page documents the most common ways these fixed-layout official templates fail under normal AI/document workflows.

---

## 1. Treating the file as a normal Word document

### What happens
- line breaks drift
- spacing changes
- grid alignment breaks
- cross-device rendering becomes inconsistent

### Why
Because the file is not behaving like a normal flowing text document. It is acting like a rigid visual form.

---

## 2. OCR + text reflow

### What happens
- some characters are lost
- content survives, layout does not
- text no longer sits correctly inside the original grid
- punctuation and spacing become unstable

### Why
OCR extracts semantic content, but not the exact structural relationship between text and grid.

---

## 3. Repeated PDF page merging

### What happens
- page 1 looks correct
- page 2+ begins to fail
- border lines stack or thicken
- text layers disappear
- page resources interfere with each other

### Why
Some PDF workflows reuse page objects, fonts, XObjects, or resource dictionaries in fragile ways.

Typical risky pattern:

- `copy.deepcopy(template_page)`
- repeated `merge_page()`
- multi-page overlay generation on the same shared base object

---

## 4. Moving only the text

### What happens
- text shifts
- the grid stays still
- the page becomes visually broken

### Why
The system misidentifies the unit of operation.

The correct unit is often:
- the whole visual block
- or the grid-aware image-space coordinate system

not “the text alone.”

---

## 5. Fighting the internal structure too long

### What happens
- endless attempts to fix Word
- endless attempts to fix PDF merge
- excessive manual tuning
- unstable results
- wasted time

### Why
Because the task is framed incorrectly.

The winning shift is:

> Stop treating the file as an editable document.
> Treat it as a fixed visual canvas.

---

## Summary

The most common root cause is not “bad prompting.”

It is:

> **wrong problem representation**

Once the task is reframed as image-space rendering, stability improves dramatically.
