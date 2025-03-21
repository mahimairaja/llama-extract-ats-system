from dotenv import load_dotenv
from llama_cloud_services import LlamaExtract
from llama_cloud.core.api_error import ApiError
from schema import Resume
load_dotenv()


llama_extract = LlamaExtract()

try:
    existing_agent = llama_extract.get_agent(name="ats-resume-parser")
    if existing_agent:
        llama_extract.delete_agent(existing_agent.id)
except ApiError as e:
    if e.status_code == 404:
        pass
    else:
        raise


agent = llama_extract.create_agent(name="ats-resume-parser", data_schema=Resume)

agent.data_schema = Resume
resume = agent.extract("resume.pdf")

print(resume.data)
