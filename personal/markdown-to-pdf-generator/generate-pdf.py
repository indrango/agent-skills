#!/usr/bin/env python3
"""General Markdown-to-PDF converter for agent skills.

Usage:
    python generate-pdf.py input.md
    python generate-pdf.py input.md --output output.pdf
    python generate-pdf.py input.md --title "Report Title" --toc
    python generate-pdf.py input.md --diagram architecture=architecture.dot

Diagram placeholders in Markdown:
    <!-- DIAGRAM: architecture -->
    <!-- ENDDIAGRAM -->
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

import graphviz
from weasyprint import HTML

DEFAULT_CSS = """
@page {
    size: A4;
    margin: 2.35cm 1.95cm 2.1cm 1.95cm;

    @top-left {
        content: string(document-title);
        font-size: 9pt;
        font-weight: 600;
        color: #56625d;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }

    @bottom-center {
        content: "Page " counter(page) " of " counter(pages);
        font-size: 9pt;
        color: #7a847f;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }
}

:root {
    --text: #343936;
    --muted: #6a736f;
    --line: #dfe4da;
    --panel: #f4f1e9;
    --panel-strong: #f8f6f0;
    --primary: #2b463c;
    --secondary: #688f4e;
    --highlight: #b1d182;
    --paper: #ffffff;
    --soft-accent: #eef4e4;
    --code-bg: #f6f4ee;
    --code-block-bg: #34423d;
    --code-block-border: #4b6258;
    --code-block-text: #f4f1e9;
}

html {
    color: var(--text);
    font-size: 11.2pt;
    background: var(--paper);
}

body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Inter, Arial, sans-serif;
    font-size: 10.8pt;
    line-height: 1.78;
    color: var(--text);
    background: var(--paper);
    letter-spacing: 0.002em;
}

h1, h2, h3, h4 {
    page-break-after: avoid;
    letter-spacing: -0.01em;
}

h1:first-of-type {
    string-set: document-title content();
    font-size: 24pt;
    line-height: 1.18;
    font-weight: 740;
    color: var(--primary);
    margin: 0 0 12pt 0;
    padding: 0 0 12pt 0;
    border-bottom: 2px solid #d8e4c7;
}

h2 {
    font-size: 15.5pt;
    font-weight: 700;
    color: var(--primary);
    margin: 30pt 0 12pt 0;
    padding-bottom: 4pt;
    border-bottom: 1px solid #dfe7d0;
}

h3 {
    font-size: 12.4pt;
    font-weight: 700;
    color: #4f6f42;
    margin: 20pt 0 7pt 0;
}

h4 {
    font-size: 11pt;
    font-weight: 650;
    color: #5b645f;
    margin: 15pt 0 5pt 0;
}

p {
    margin: 8pt 0;
}

hr {
    display: none;
}

ul, ol {
    margin: 10pt 0 12pt 0;
    padding-left: 20pt;
}

li {
    margin: 4pt 0;
}

li > ul,
li > ol {
    margin: 5pt 0 6pt 0;
    padding-left: 16pt;
}

li > ul > li > ul,
li > ul > li > ol,
li > ol > li > ul,
li > ol > li > ol {
    padding-left: 14pt;
}

ul.task-list,
ol.task-list {
    list-style: none;
    padding-left: 0;
    margin: 12pt 0 14pt 0;
}

ul.task-list > li,
ol.task-list > li,
li.task-list-item {
    list-style: none;
    margin: 5pt 0;
    padding: 2pt 0;
}

ul.task-list > li::marker,
ol.task-list > li::marker,
li.task-list-item::marker {
    content: "";
}

ul.task-list > li > label,
ol.task-list > li > label,
.task-line {
    display: block;
    position: relative;
    padding-left: 1.5em;
    color: #39423e;
}

ul.task-list input[type="checkbox"],
ol.task-list input[type="checkbox"],
.task-line input[type="checkbox"] {
    position: absolute;
    left: 0;
    top: 0.32em;
    width: 0.92em;
    height: 0.92em;
    margin: 0;
    accent-color: #688f4e;
}

.task-text {
    display: inline;
}

.task-line.checked .task-text {
    color: #66706b;
}

li.task-list-item p {
    margin: 5pt 0 0 1.35em;
}

blockquote {
    margin: 16pt 0;
    padding: 13pt 15pt;
    border-left: 3px solid #8eaf68;
    background: var(--panel);
    border-radius: 10px;
}

blockquote p {
    margin: 0;
    color: #42514b;
}

code {
    font-family: "SFMono-Regular", Menlo, Consolas, monospace;
    font-size: 8.8pt;
    background: var(--code-bg);
    color: #355146;
    padding: 1.5pt 5pt;
    border-radius: 5px;
}

pre {
    margin: 14pt 0;
    padding: 14pt 15pt;
    background: var(--code-block-bg);
    color: var(--code-block-text);
    border-radius: 12px;
    border: 1px solid var(--code-block-border);
    font-family: "SFMono-Regular", Menlo, Consolas, monospace;
    font-size: 8.6pt;
    line-height: 1.6;
    white-space: pre-wrap;
    word-break: break-word;
    page-break-inside: avoid;
}

pre code {
    background: transparent;
    color: inherit;
    padding: 0;
}

table {
    width: 100%;
    border-collapse: collapse;
    margin: 16pt 0 20pt 0;
    font-size: 9.35pt;
    border: 1px solid var(--line);
    border-radius: 12px;
    overflow: hidden;
    page-break-inside: avoid;
}

thead th {
    background: var(--soft-accent);
    color: var(--primary);
    font-weight: 700;
    text-align: left;
    padding: 9pt 11pt;
    border-bottom: 1px solid #d6e3c0;
}

tbody td {
    padding: 9pt 11pt;
    border-bottom: 1px solid var(--line);
    vertical-align: top;
    color: #3b433f;
}

tbody tr:nth-child(even) td {
    background: #fcfbf8;
}

tbody tr:last-child td {
    border-bottom: none;
}

a {
    color: #557945;
    text-decoration: none;
}

svg {
    max-width: 100%;
    height: auto;
}

.diagram-wrapper {
    margin: 18pt 0 20pt 0;
    padding: 14pt;
    background: var(--panel);
    border: 1px solid var(--line);
    border-radius: 14px;
    text-align: center;
    page-break-inside: avoid;
}

#TOC {
    margin: 20pt 0 26pt 0;
    padding: 15pt 17pt;
    background: var(--panel-strong);
    border: 1px solid var(--line);
    border-radius: 14px;
}

#TOC::before {
    content: "Table of Contents";
    display: block;
    font-size: 11.2pt;
    font-weight: 700;
    color: var(--primary);
    margin-bottom: 9pt;
}

#TOC ul {
    margin: 0;
    padding-left: 16pt;
}

#TOC li {
    margin: 3pt 0;
    color: var(--muted);
}

#TOC a {
    color: #56625d;
}

h2, h3, .diagram-wrapper, pre, table {
    page-break-inside: avoid;
}
"""


def run_pandoc(markdown_file: Path, html_file: Path, title: str, toc: bool, toc_depth: int) -> None:
    command = [
        "pandoc",
        str(markdown_file),
        "-f",
        "markdown",
        "-t",
        "html5",
        "--standalone",
        "--metadata",
        f"title={title}",
        "-o",
        str(html_file),
    ]

    if toc:
        command.extend(["--toc", "--toc-depth", str(toc_depth)])

    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode != 0:
        print("Pandoc error:", result.stderr, file=sys.stderr)
        sys.exit(1)


def parse_diagram_arg(value: str) -> tuple[str, Path]:
    if "=" not in value:
        raise argparse.ArgumentTypeError("diagram must use NAME=DOT_FILE format")

    name, dot_file = value.split("=", 1)
    name = name.strip()
    path = Path(dot_file).expanduser().resolve()

    if not name:
        raise argparse.ArgumentTypeError("diagram name cannot be empty")
    if not path.exists():
        raise argparse.ArgumentTypeError(f"diagram file not found: {path}")

    return name, path


def render_diagrams(diagrams: list[tuple[str, Path]], output_dir: Path) -> list[tuple[str, str]]:
    if not diagrams:
        return []

    svg_dir = output_dir / "_diagrams"
    svg_dir.mkdir(parents=True, exist_ok=True)
    rendered: list[tuple[str, str]] = []

    for name, dot_file in diagrams:
        svg_path = svg_dir / f"{name}.svg"
        source = graphviz.Source(dot_file.read_text(encoding="utf-8"), format="svg")
        source.render(filename=str(svg_dir / name), cleanup=True)

        svg_content = svg_path.read_text(encoding="utf-8")
        svg_content = re.sub(r"<\?xml[^>]*>\s*", "", svg_content)
        svg_content = re.sub(r"<!DOCTYPE[^>]*>\s*", "", svg_content)
        rendered.append((name, svg_content))
        print(f"  Rendered diagram: {name}")

    return rendered


def embed_diagrams(html_content: str, diagrams: list[tuple[str, str]]) -> str:
    for name, svg in diagrams:
        marker = f"<!-- DIAGRAM: {name} -->"
        end_marker = "<!-- ENDDIAGRAM -->"
        wrapped = f'<div class="diagram-wrapper">\n{svg}\n</div>'
        pattern = re.escape(marker) + r".*?" + re.escape(end_marker)
        html_content = re.sub(pattern, wrapped, html_content, count=1, flags=re.DOTALL)
    return html_content


def normalize_task_lists(html_content: str) -> str:
    def replace_task_item(match: re.Match[str]) -> str:
        li_open, checkbox, checked_attr, text, rest, li_close = match.groups()
        checked_class = " checked" if checked_attr else ""
        return (
            f'{li_open}<span class="task-line{checked_class}">{checkbox}'
            f'<span class="task-text">{text}</span></span>{rest}{li_close}'
        )

    pattern = (
        r'(<li class="task-list-item">)\s*'
        r'(<input[^>]*type="checkbox"([^>]*)>)\s*'
        r'<p>(.*?)</p>'
        r'(.*?)'
        r'(</li>)'
    )
    return re.sub(pattern, replace_task_item, html_content, flags=re.DOTALL)


def inject_styles(html_content: str, css: str) -> str:
    html_content = re.sub(
        r'<style type="text/css">.*?</style>',
        "",
        html_content,
        count=1,
        flags=re.DOTALL,
    )
    html_content = re.sub(
        r"<style>.*?</style>",
        "",
        html_content,
        count=1,
        flags=re.DOTALL,
    )
    return html_content.replace("</head>", f"<style>\n{css}\n</style>\n</head>", 1)


def convert_markdown_to_pdf(
    markdown_file: Path,
    pdf_file: Path | None = None,
    *,
    title: str | None = None,
    css_file: Path | None = None,
    keep_html: bool = False,
    toc: bool = False,
    toc_depth: int = 2,
    diagrams: list[tuple[str, Path]] | None = None,
) -> Path:
    markdown_file = markdown_file.expanduser().resolve()
    if not markdown_file.exists():
        raise FileNotFoundError(f"Markdown file not found: {markdown_file}")

    pdf_file = (pdf_file or markdown_file.with_suffix(".pdf")).expanduser().resolve()
    output_dir = pdf_file.parent
    output_dir.mkdir(parents=True, exist_ok=True)

    html_file = pdf_file.with_suffix(".html")
    document_title = title or markdown_file.stem.replace("-", " ").replace("_", " ").title()
    css = css_file.expanduser().resolve().read_text(encoding="utf-8") if css_file else DEFAULT_CSS

    print("Converting markdown to HTML...")
    run_pandoc(markdown_file, html_file, document_title, toc, toc_depth)
    print(f"  HTML generated: {html_file}")

    rendered_diagrams = render_diagrams(diagrams or [], output_dir)
    html_content = html_file.read_text(encoding="utf-8")
    html_content = embed_diagrams(html_content, rendered_diagrams)
    html_content = normalize_task_lists(html_content)
    html_content = inject_styles(html_content, css)
    html_file.write_text(html_content, encoding="utf-8")
    print("  Styles injected.")

    print("Generating PDF with WeasyPrint...")
    HTML(str(html_file)).write_pdf(str(pdf_file))
    print(f"  PDF generated: {pdf_file}")

    if not keep_html:
        html_file.unlink(missing_ok=True)

    return pdf_file


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Convert a Markdown file to a styled PDF.")
    parser.add_argument("markdown_file", type=Path, help="Markdown file to convert")
    parser.add_argument("--output", "-o", type=Path, help="PDF output path")
    parser.add_argument("--title", help="Document title metadata")
    parser.add_argument("--css", type=Path, help="Custom CSS file")
    parser.add_argument("--keep-html", action="store_true", help="Keep generated intermediate HTML")
    parser.add_argument("--toc", action="store_true", help="Generate a table of contents")
    parser.add_argument("--toc-depth", type=int, default=2, help="Table of contents depth")
    parser.add_argument(
        "--diagram",
        action="append",
        default=[],
        type=parse_diagram_arg,
        help="Render and embed a Graphviz DOT file. Format: NAME=DOT_FILE",
    )
    return parser


def main() -> None:
    args = build_parser().parse_args()
    try:
        convert_markdown_to_pdf(
            args.markdown_file,
            args.output,
            title=args.title,
            css_file=args.css,
            keep_html=args.keep_html,
            toc=args.toc,
            toc_depth=args.toc_depth,
            diagrams=args.diagram,
        )
    except Exception as error:
        print(f"Error: {error}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
