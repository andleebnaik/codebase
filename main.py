from parse_file import parser
from sumarize_doc import summarize_doc
from dotenv import load_dotenv
import os
# Load environment variables
load_dotenv()
# Set OpenAI API key
openai_api_key = os.getenv('openai_api_key')

file_name = r"d:\OFFICE\DI\The_Project\Sample Proposals\Uniform Format\1\Copy of Attachment J.3 - QASP COR Support.pdf"
#parser(file_name)

response,tokens_used = summarize_doc(openai_api_key,file_name)