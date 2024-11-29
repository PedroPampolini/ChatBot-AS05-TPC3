from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline, Pipeline
from typing import *
import torch
from PyPDF2 import PdfReader
import os
import re
import warnings

class ModelName:
  roberta = "deepset/roberta-base-squad2"
  roberta2 = "deepset/roberta-base-squad2-distilled"
  distilbert = "distilbert/distilbert-base-uncased"

class Bot:
  def __init__(self, modelName):
    self.modelName = modelName
    self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
    self.model = AutoModelForQuestionAnswering.from_pretrained(self.modelName).to(self.device)
    self.tokenizer = AutoTokenizer.from_pretrained(self.modelName)
    self.nlp = pipeline('question-answering', model=self.model, tokenizer=self.tokenizer, device=self.device)
    self.context = self.buildContext('uploadedPdf')
    print(f"Bot initialized with model: {self.modelName} running on {self.device}")
  
  async def Greetings(self):
    return f"Hello! Send me a PDF file and I will answer your questions."
  
  def getPdftext(self, pdfPath:str) -> str:
    with open(pdfPath, 'rb') as f:
      pdf = PdfReader(f)
      title = pdf.metadata.title
      text = ''
      for page in pdf.pages:
        text += page.extract_text()

    return title, text
  
  def processText(self,text:str) -> str:
    text = text.replace('\n', ' ')
    regex = r"[^A-Za-z %$#!@,.:]"
    resultado = re.sub(regex, "", text)
    return resultado

  def buildContext(self,documentsPath:str) -> str:
    documentsText:List = []
    # get pdfs list from a path
    pdfs:List[str] = os.listdir(documentsPath)
    # filter by pdf
    pdfs = [pdf for pdf in pdfs if pdf.endswith('.pdf')]
    print(f"found: {pdfs}")
    # for each pdf, extract its text
    for document in pdfs:
      document = os.path.join(documentsPath, document)
      print(f"getting info from {document}")
      title, text = self.getPdftext(document)
      text = self.processText(text)
      documentsText.append(f"{title}\n{text}")
    context = '\n'.join(documentsText)
    return context

  def answer_question(self, question, context):
    QA_input = {
      'question': question,
      'context': context
    }
    res = self.nlp(QA_input)
    return res['answer']
  
  async def GetAnwser(self, question:str, documentsPath:str) -> str:
    if not self.context:
      self.context = self.buildContext(documentsPath)
    answer = self.answer_question(question, self.context)
    return answer

  def ClearContext(self):
    self.context = ''