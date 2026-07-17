---
name: "markdown-to-pdf-generator"
description: "Generates styled PDF files from Markdown using the shared Python converter. Invoke when the user asks to export, convert, or generate a PDF from a Markdown document."
---

# Markdown to PDF Generator

Use this skill to convert a Markdown document into a styled PDF by calling the bundled Python helper at [generate-pdf.py](file:///Users/indranugraha/Codes/skills/personal/markdown-to-pdf-generator/generate-pdf.py).

## When to invoke

Invoke this skill when:
- the user asks to convert a `.md` file into `.pdf`
- the user asks to export documentation, report, or spec as PDF
- an agent flow needs a repeatable Markdown-to-PDF generation step

Do not invoke this skill when:
- the source document is not Markdown
- the user only wants HTML or plain text output
- the user is asking to edit the Markdown content rather than export it

## Required inputs

Provide these inputs before running the converter:
- Absolute path to the Markdown file
- Optional output PDF path
- Optional title
- Whether TOC is needed
- Optional diagram mappings in `NAME=DOT_FILE` format

## Execution steps

1. Confirm the source Markdown file exists.
2. Decide the output PDF path. Default to the same basename as the Markdown file.
3. Run the converter:

```bash
python3 /Users/indranugraha/Codes/skills/personal/markdown-to-pdf-generator/generate-pdf.py "/absolute/path/to/input.md" \
  --output "/absolute/path/to/output.pdf" \
  --title "Document Title" \
  --toc
```

4. If the Markdown contains diagram placeholders, add one or more `--diagram` flags:

```bash
python3 /Users/indranugraha/Codes/skills/personal/markdown-to-pdf-generator/generate-pdf.py "/absolute/path/to/input.md" \
  --output "/absolute/path/to/output.pdf" \
  --diagram architecture=/absolute/path/to/architecture.dot \
  --diagram flow=/absolute/path/to/flow.dot
```

## Markdown diagram placeholder contract

The Markdown file may include placeholders like:

```html
<!-- DIAGRAM: architecture -->
<!-- ENDDIAGRAM -->
```

Each placeholder name must match a `--diagram NAME=DOT_FILE` argument.

## Standard output format

After running the converter, respond using this format:

```text
PDF generated successfully.
- Source: /absolute/path/to/input.md
- Output: /absolute/path/to/output.pdf
- Title: <resolved title>
- TOC: enabled|disabled
- Diagrams: none|name1, name2
```

If generation fails, respond using this format:

```text
PDF generation failed.
- Source: /absolute/path/to/input.md
- Output: /absolute/path/to/output.pdf
- Failed step: validation|pandoc|graphviz|weasyprint
- Error: <short error message>
```

## Notes

- The shared helper already injects default styling and uses WeasyPrint for PDF rendering.
- Use `--keep-html` only when the user explicitly wants the intermediate HTML artifact.
- Keep the process deterministic: do not modify Markdown content unless the user asks.
