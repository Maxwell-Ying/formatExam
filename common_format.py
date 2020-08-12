from docx import Document
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT, WD_LINE_SPACING
from docx.opc.oxml import qn
from docx.shared import Pt
from docx.text.paragraph import Paragraph
from docx.text.run import Run

over_all_font = u"宋体"

title_const = [
    "none",
    "一、给下列词语注音并抄写\n",
    "二、生字组词\n",
    "三、形近字辨析\n",
    "四、多音字辨析\n"
]


def format_normal(document: Document):
    document.styles['Normal'].font.name = over_all_font
    document.styles['Normal'].font.size = Pt(15)
    document.styles['Normal']._element.rPr.rFonts.set(qn('w:eastAsia'), u'宋体')


def format_heading(heading: Paragraph):
    heading_format = heading.paragraph_format
    heading_format.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER


def format_heading_run(heading_run: Run):
    heading_run.font.name = over_all_font
    heading_run.font.size = Pt(17)
    heading_run._element.rPr.rFonts.set(qn('w:eastAsia'), over_all_font)
    heading_run.bold = True


def format_paragraph_title(paragraph: Paragraph, title_index):
    title = paragraph.add_run(title_const[title_index])
    title.bold = True


def format_paragraph(paragraph: Paragraph):
    paragraph.line_spacing_rule = WD_LINE_SPACING.ONE_POINT_FIVE
