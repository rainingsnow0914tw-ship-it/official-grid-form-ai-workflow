# Problem Background

Many official templates are technically distributed as Word or PDF files, but functionally they are neither ordinary Word documents nor ordinary editable PDFs.

They often behave like:

- fixed-layout visual forms
- one-character-per-cell grids
- printing-first templates
- pseudo-editable shells rather than normal documents

This creates a mismatch between the file format and the user's expectations.

A user sees:
- `.docx`
- `.pdf`
- visible text
- visible boxes

and naturally assumes:
- normal editing should work
- copy/paste should work
- text replacement should work
- export between Word and PDF should be straightforward

But these assumptions often fail.

The real constraints are:

- the layout must remain visually identical
- each character may need to stay centered inside a cell
- content structure is less important than output geometry
- the file may contain multiple internal layers or unstable formatting logic

This is why many users lose hours trying:
- Word reconstruction
- OCR text extraction and replacement
- page overlay workflows
- manual formatting adjustments

The core problem is not “how to edit a document.”

The core problem is:

> **how to preserve a rigid visual grid while inserting new content safely**

That is why these tasks are better framed as rendering problems rather than document-editing problems.
