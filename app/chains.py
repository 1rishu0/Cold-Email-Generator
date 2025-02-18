import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain.schema import OutputParserException
from dotenv import load_dotenv

load_dotenv()

class Chain:
    def __init__(self):
        self.llm = ChatGroq(temperature=0, groq_api_key=os.getenv("GROQ_API_KEY"), model="llama-3.3-70b-versatile")

    def extract_jobs(self, cleaned_text):
        prompt_template = PromptTemplate.from_template(
            """
            ### SCRAPED TEXT FROM WEBSITE:
            {page_data}
            ### INSTRUCTION:
            The scraped text is from the carrer's page of a website.
            You job is to extract the job postings and return them in JSON format containing the 
            following keys: 'role','experience','skills' and 'description'.
            Only return the valid JSON , not write preamble on the top with commenting and skills sections should be in list.
            ### VALID JSON WITH NO PREAMBLE :
            """
        )

        chain_extract = prompt_template | self.llm
        res = chain_extract.invoke({"page_data":cleaned_text})

        try:
            json_parser = JsonOutputParser()
            res = json_parser.parse(res.content)
        except OutputParserException :
            raise OutputParserException("Context too big. Unable to parse jobs.")
        
        return res if isinstance(res,list) else [res]
    
    def write_mail(self, job, links):
        prompt_email = PromptTemplate.from_template(
            """ 
            ### JOB DESCRIPTION:
            {job_description}
            ### INSTRUCTION:
            You are Rishabh, who are interest in joining the company with the skills of AI and Data Science as a Basic. 
            Over My experience, I have been a AI Trainee at IBM for 2 months which give me relevant skills . 
            Your job is to write a cold email to the client regarding the job mentioned above describing the capability of AtliQ 
            in fulfilling their needs.
            Also add the most relevant ones from the following links to showcase Rishabh's portfolio: {link_list}
            Remember you are Rishabh Sharma. 
            Do not provide a preamble.
            ### VALID JSON WITH NOT PREAMBLE:"""
        )

        chain_email = prompt_email | self.llm
        res = chain_email.invoke({"job_description":str(job),"link_list":links})
        return res.content

if __name__=="__main__":
    print(os.getenv("GROQ_API_KEY"))