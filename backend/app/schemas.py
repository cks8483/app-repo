from typing import List
from pydantic import BaseModel, HttpUrl

class Skill(BaseModel):
    name: str
    proficiency: int  # 0 to 100 representing percentage

class Project(BaseModel):
    title: str
    description: str
    link: HttpUrl

class Profile(BaseModel):
    name: str
    bio: str
    skills: List[Skill]
    projects: List[Project]