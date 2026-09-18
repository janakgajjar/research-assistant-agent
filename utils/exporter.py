"""
Report Export Utilities

Provides functions to export the final research
report into PDF, Markdown and TXT formats.
"""

from io import BytesIO

from reportlab.lib.pagesizes import A4
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_LEFT


def export_txt(report):
    """
    Convert report into plain text.
    """

    return str(report)


def export_markdown(report):
    """
    Convert report into Markdown format.
    """

    return str(report)


def export_pdf(report):
    """
    Convert report into PDF format.
    """

    buffer = BytesIO()

    document = SimpleDocTemplate(
        buffer,
        pagesize=A4,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40
    )

    styles = getSampleStyleSheet()

    title_style = styles["Title"]
    heading_style = styles["Heading2"]
    body_style = styles["BodyText"]

    story = []

    lines = str(report).split("\n")

    for line in lines:

        line = line.strip()

        if not line:
            story.append(Spacer(1, 8))
            continue

        if line.startswith("# "):

            text = line[2:].strip()

            story.append(
                Paragraph(
                    text,
                    title_style
                )
            )

        elif line.startswith("## "):

            text = line[3:].strip()

            story.append(
                Paragraph(
                    text,
                    heading_style
                )
            )

        elif line.startswith("- "):

            text = "• " + line[2:].strip()

            story.append(
                Paragraph(
                    text,
                    body_style
                )
            )

        else:

            story.append(
                Paragraph(
                    line,
                    body_style
                )
            )

        story.append(
            Spacer(1, 5)
        )

    document.build(story)

    buffer.seek(0)

    return buffer.getvalue()