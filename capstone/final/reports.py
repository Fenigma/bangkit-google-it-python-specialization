#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

def generate_report(attachment, title, paragraph):
  report_builder = []
  styles = getSampleStyleSheet()
  report = SimpleDocTemplate(attachment)

  report_title = Paragraph(title, styles["h1"])
  empty_line = Spacer(1,1)

  report_builder.append(report_title)
  report_builder.append(empty_line)

  for c in paragraph:
    report_paragraph = Paragraph(c, styles["BodyText"])
    report_builder.append(report_paragraph)
    report_builder.append(empty_line)
  
  report.build(report_builder)