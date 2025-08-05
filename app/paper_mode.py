from types import Optional
from markdown_it import MarkdownIt
from weasyprint import HTML, CSS
from .base import *
import os, re

#write documents, can insert images at specific rates (optional, search images and insert them automatically)
#can do good pdf's overall (anti ai detection ?)
#use gemini 2.5 pro for text gen

def paper_input():
    #can prompt
    #can insert files one by one ?
    #can insert images (files)
    print("Welcome on the Paper Mode. This mode's purpose is to generate documents for you, from A to Z. Expected output: PDF.")

    print("What would you like to build?")
    input1 = input("Ask anything: ")

    print("If you have any document for context to add, add them in paper_input/ (instructions or more details, resources... etc)")
    input("Press enter when done or to skip this step.") #retype this sentence its rly unclear

    print("Would you like to enable the anti-AI plagiarism mode?")
    input3 = input("Input ('y' or 'n'): ") #retype this so it looks better, add colors soon too on all the cli
    
    return input1, input3

def add_paper_documents(): #return false if none, return true and add to existing context if good
    #will do later, gather all documents available in paper_input
    folder = os.path("paper_input/")
    for document in folder:
        pass

    """
    #put all this in base.py, add_documents function that takes as an input the folder to read in and add in prompt? much easier
    gemini_file = genai.upload_file(
            path=temp_file_path,
            display_name=original_filename,
            mime_type=mime_type
        )

        # Polling logic
        timeout_seconds = 300
        start_time = time.time()
        while gemini_file.state.name == 'PROCESSING':
            if time.time() - start_time > timeout_seconds:
                raise Exception(f"Timeout waiting for Gemini file {original_filename} to become active.")
            time.sleep(5)
            gemini_file = genai.get_file(name=gemini_file.name)
            print(f"Polling Gemini file '{gemini_file.display_name}', state: {gemini_file.state.name}")

        if gemini_file.state.name == 'FAILED':
            raise Exception(f"Gemini file processing FAILED for {original_filename}.")
        
        gemini_file_cache[cache_key] = gemini_file
        print(f"File {original_filename} is ACTIVE on Gemini.")
        return gemini_file
    """


def strip_gemini_output(content: str):
    pattern = r"```\s*(\w*)?\s*\n?(.*?)```"
    condition = re.search(pattern, content, re.DOTALL)

    if condition:
        output = condition.group(2).strip()
    else:
        output = content.strip()
    
    return output


def gemini_context(input1: str):
    add_paper_documents()
    prompt(f"Here are the user details: {input1}, just respond with 'OK' and remember this for the next instruction.")
    #need to remove ``` from gemini's output btw
    html = strip_gemini_output(prompt(html_prompt()))
    css = strip_gemini_output(prompt(css_prompt()))
    generate_pdf_from_markdown(html, css)


#configure, ask input, if documents add in gemeini context documents, then add user input,
#then ask ai to generate html, then css (with all context) then download output in paper_ouput/ and open it automatically
#ask if user likes result, if not then it adds into chat new details from the user
def html_prompt():
    output = "You need to generate the markdown content for a pdf document that will render automatically through a python script. It will be transformed into HTML then we will add CSS then output a .pdf file. Please do not output any superfleous information and only output the markdown content for now, the objective is to automatically parse your output and generate qualitative documents. All the context is given, documents sent... etc. Good luck."
    return output

def css_prompt():
    output = "Now you need to generate the CSS, make this look like a latex professional document, be original and respect what the user is asking, guess the type of document formatting. It has to look good. No superfleous informations again, only the important stuff."
    return output


def generate_pdf_from_markdown(markdown_text: str, css: str, output_path: str):
    md = MarkdownIt()
    html_content = md.render(markdown_text)
    stylesheet = CSS(css)
    HTML(string=html_content).write_pdf(output_path, stylesheets=[stylesheet])


def undetect_text(text: str) -> str:
    pass