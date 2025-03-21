from typing import List, Optional
from pydantic import BaseModel, Field

class Education(BaseModel):
    institution: str = Field(description="The institution of the candidate")
    degree: str = Field(description="The degree of the candidate")
    start_date: Optional[str] = Field(
        default=None, description="The start date of the candidate's education"
    )
    end_date: Optional[str] = Field(
        default=None, description="The end date of the candidate's education"
    )


class Experience(BaseModel):
    company: str = Field(description="The name of the company")
    title: str = Field(description="The title of the candidate")
    description: Optional[str] = Field(
        default=None, description="The description of the candidate's experience"
    )
    start_date: Optional[str] = Field(
        default=None, description="The start date of the candidate's experience"
    )
    end_date: Optional[str] = Field(
        default=None, description="The end date of the candidate's experience"
    )


class Resume(BaseModel):
    name: str = Field(description="The name of the candidate")
    email: str = Field(description="The email address of the candidate")
    links: List[str] = Field(
        description="The links to the candidate's social media profiles"
    )
    experience: List[Experience] = Field(description="The candidate's experience")
    education: List[Education] = Field(description="The candidate's education")