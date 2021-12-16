from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.rl_config import defaultPageSize
import logging

import config


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    filename='debug.log'
)
logger = logging.getLogger(__name__)

PAGE_WIDTH = defaultPageSize[0]
PAGE_HEIGHT = defaultPageSize[1]


def create_cert(name, contact_id, template_pdf=None):
    """
    Функция для добавления текста на PDF файл.

    Parameters:
    name (string): ФИО в дательном падеже
    contact_id (string): telegram_id
    template_pdf (string): название файла шаблона

    Returns:
    string or False: название выходного файла.
    """

    try:
        """
        1. Создаем canvas и рисуем наш текст
        """
        packet = io.BytesIO()
        can = canvas.Canvas(packet, pagesize=letter)
        pdfmetrics.registerFont(TTFont('DejaVuSerif', 'DejaVuSerif.ttf'))
        can.setFont("DejaVuSerif", 30)

        text = name
        text_width = pdfmetrics.stringWidth(text, "DejaVuSerif", 30)
        y = 310
        x = ((PAGE_WIDTH - text_width) / 2) + 120

        can.drawString(x, y, text)
        can.save()
        packet.seek(0)

        # получаем свою PDF с помощью canvas из Reportlab
        new_pdf = PdfFileReader(packet)

        # берем шаблон PDF
        if template_pdf is None:
            template_pdf = config.DEFAULT_TEMPLATE_PDF

        existing_pdf = PdfFileReader(open(config.ROOT_APP + '/templates/' + template_pdf, "rb"))

        """
        2. Создаем новый PDF-файл с помощью PyPDF2
        """
        output = PdfFileWriter()
        page = existing_pdf.getPage(0)  # страница шаблона
        page.mergePage(new_pdf.getPage(0))  # мержим с нашей страницей
        output.addPage(page)

        """
        3. Save and enjoy!
        """
        output_pdf = contact_id + '.pdf'
        outputStream = open(config.ROOT_APP + '/files/' + output_pdf, "wb")
        output.write(outputStream)
        outputStream.close()
        return output_pdf

    except Exception as e:
        logger.warning(e)

        return False


if __name__ == '__main__':
    create_cert("Иванову Петрову Сидоровичу")
