from pathlib import Path
import nltk
import torch
import contextlib

from pdf2text import *


def convert_pdf(pdf_obj, language:str='en'):
    rm_local_text_files()
    global ocr_model

    if isinstance(pdf_obj, list):
        pdf_obj = pdf_obj[0]

    file_path = Path(pdf_obj.name)

    conversion_stats = convert_PDF_to_Text(
            file_path, 
            ocr_model = ocr_model, 
            max_pages = 150,
            )
    coverted_text = conversion_stats['converted_text']
    num_pages = conversion_stats['num_pages']
    was_truncated = conversion_stats['truncated']

    temp_var = {"Text":converted_text, "No. of pages": num_pages, "Truncated ?": was_truncated}

    return temp_var

if __name__ == "__main__":

    with contextlib.redirect_stdout(None):

        ocr_model = ocr_predictor(
            "db_resnet50",
            "crnn_mobilenet_v3_large",
            pretrained=True,
            assume_straight_pages = True,
        )
   
    path = Path(__file__).parent
    pdf_obj = path / "keysight_U2722A.pdf"
    convert_pdf(pdf_obj)
