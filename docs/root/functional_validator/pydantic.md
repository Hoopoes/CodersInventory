### Overriding Pydantic Schema Constructor for Post-Validation

The following code demonstrates how to override the Pydantic schema constructor to add a post-validation step. The goal is to automatically replace empty string fields with `"N/A"` when creating an object:

```python linenums="1"
from typing import Optional
from pydantic import BaseModel

class IDCard(BaseModel):
    identity_number: Optional[str] = None
    name: Optional[str] = None
    father_name: Optional[str] = None
    date_of_birth: Optional[str] = None
    date_of_issuance: Optional[str] = None
    date_of_expiry: Optional[str] = None

    def __init__(self, **kwargs):
        # Call the BaseModel constructor
        super().__init__(**kwargs)
        # Replace empty strings with "N/A"
        self._replace_empty_strings()

    def _replace_empty_strings(self):
        for field_name, value in self.dict().items():
            if value == "":
                setattr(self, field_name, "N/A")


# Example usage
id_card = IDCard(
    identity_number="123456789",
    name="",  # Empty field
    father_name="John Doe",
    date_of_birth="1990-01-01",
    date_of_issuance="",  # Empty field
    date_of_expiry="2030-01-01"
)

print(id_card.model_dump())
```

### Output
```python
{
    'identity_number': '123456789',
    'name': 'N/A',
    'father_name': 'John Doe',
    'date_of_birth': '1990-01-01',
    'date_of_issuance': 'N/A',
    'date_of_expiry': '2030-01-01'
}
```

### Key Points:
1. **Constructor Override (`__init__`)**:
   - The `__init__` method is overridden to insert custom logic after the object initialization.
   - The `super().__init__(**kwargs)` ensures the base Pydantic model is initialized properly.
   
2. **Post-Validation Logic**:
   - A helper method `_replace_empty_strings` iterates through the fields of the object.
   - Empty strings (`""`) are replaced with `"N/A"` using `setattr`.

3. **Simple and Reusable**:
   - This approach ensures the object is automatically validated and modified at creation time, without needing additional manual steps.










class ChartsRequest(BaseModel):
    title: str = "Generated Chart"
    transparent: bool = False
    x_axis: str = "X-axis"
    y_axis: str = "Y-axis"
    x_values: list[int | float]
    y_values: Optional[list[int | float]] = None
    graph_type: Optional[Literal['HIST', 'LINE', 'SCATTER', 'BAR', 'BOX']] = None  # Required when both x and y values are provided otherwise onlyy histogram is generated (frequency distribution)

    @model_validator(mode="after")
    def post_validation(self):
        if not self.graph_type == "HIST":
            if self.y_values is not None and len(self.x_values) != len(self.y_values):
                raise ValueError('x_values and y_values must be of equal length')
        return self
    
    class Config:
        json_schema_extra = {
            "example": {
                "title": "Pollution Level",
                "x_axis": "Years",
                "y_axis": "Level of CO2",
                "transparent": False,
                "x_values": [2009, 2010, 2011, 2012, 2013],
                "y_values": [5, 4, 3, 2, 1],
                "graph_type": "LINE"
            }
        }


class OutlineReq(LanguageInput):
    pages: int = Field(..., le=Constant.MAX_PAGE, description="Number of slides/pages")
    general: Optional[str] = Field(None, description="General Prompt")
    specific: Optional[SpecificOutlineReq] = Field(
        None, description="Specific Prompt with drop down values"
    )

    @model_validator(mode="after")
    def post_validation(self):
        if (self.general is None and self.specific is None) or (
            self.general is not None and self.specific is not None
        ):
            raise ValueError(
                "Either `general` or `specific` must be provided, but not both."
            )
        return self


class GitIssueReq(BaseModel):
    text: Optional[str] = Field(None, description="The text content to create issue.")
    url: Optional[str] = Field(None, description="The URL of the slide to be regenerated.")
    milestone: Optional[int] = Field(1, description="The milestone number to associate this issue with.")

    @computed_field
    @property
    def document_id(self) -> str:
        return get_google_docs_id(self.url)
    
    @model_validator(mode="after")
    def post_validation(self):
        if bool(self.url) == bool(self.text):
            raise ValueError("Either `text` or `url` must be provided, but not both.")
        return self



OutlineList = Annotated[
    list[str], Field(..., max_length=Constant.MAX_PAGE, description="Outline list")
]

Templates = Literal["gamma_template", "beacon_house_template", "beacon_house_template_2_urdu"]

class Outline(LanguageInput):
    template: Templates = "beacon_house_template"
    title: str = Field(..., description="Title name")
    outline: OutlineList


    general: Optional[str] = Field(None, description="General Prompt")
    specific: Optional[SpecificOutlineReq] = Field(
        None, description="Specific Prompt with drop down values"
    )

    @model_validator(mode="after")
    def post_validation(self):
        if (self.general is None and self.specific is None) or (
            self.general is not None and self.specific is not None
        ):
            raise ValueError(
                "Either `general` or `specific` must be provided, but not both."
            )
        return self


decimalPlace = Annotated[float, AfterValidator(lambda x: round(x, 5))]
class WhisperUsage(ServiceUsage):
    service_type: ServiceType = ServiceType.WHISPER
    usage_minutes: decimalPlace = 0


class RoleMessage(BaseModel):
    role: Role = Role.user
    content: Annotated[str, StringConstraints(strip_whitespace=True, min_length=1)] = 'START'
    phase: int = 0
    action: BotAction = BotAction.PURSUE




##############################################################################
from typing import Literal, Optional, Union, Annotated
from pydantic import BaseModel, Field, field_validator, BeforeValidator

enumKeys = ["employmentType", "noticePeriod", "jobSeniority"]

def sanitize_string(value: str) -> Optional[str]:
    if value == "null" or value == "":
        return None
    elif value in {"string", "str", "boolean", "bool", "integer", "int", "float", "number", "object", "array"}:
        raise ValueError(f"Invalid input value: '{value}' found")
    return value

def sanitize_string_list(value: list[str]) -> list[str]:
    value = [item for item in value if sanitize_string(item)]
    return value

ValidatedString = Annotated[str, BeforeValidator(sanitize_string)]
ValidatedStringList = Annotated[list[str], BeforeValidator(sanitize_string_list)]

class JobDescription(BaseModel):
    # Job title of the position
    jobTitle: ValidatedString
    
    # Company offering the job
    company: ValidatedString
    
    # Overview of the job role
    roleOverview: ValidatedString
    
    # Indicates if the job is remote
    isRemote: Optional[bool] = None
    
    # Years of experience required; should be a positive float
    experienceRequired: Optional[float] = Field(None, ge=0)  # Positive float for years of experience
    
    # Employment type, restricted to specific values
    employmentType: Optional[Literal['full-time', 'part-time', 'contract', 'internship', 'freelance', 'volunteer', 'unknown']] = None

    # Notice period options, should be one of the predefined strings
    noticePeriod: Optional[Union[Literal['immediate', '1 month', '2 months', '3 months', '4 weeks', '6 days'], str]] = None

    # `jobSeniority` can be a list of predefined values or free-text string
    # Using Literal to restrict specific values helps clarify valid roles for the field.
    jobSeniority: Optional[list[Literal['entry-level', 'mid-level', 'senior-level', 'lead', 'director', 'executive', 'manager']]] = None

    # Key responsibilities in bullet points, list of strings
    responsibilitiesBullets: Optional[ValidatedStringList] = None
    
    # Required qualifications (degrees, certifications, etc.), list of strings
    qualificationsBullets: Optional[ValidatedStringList] = None
    
    # Additional job requirements (skills, experience, etc.), list of strings
    requirementBullets: Optional[ValidatedStringList] = None
    
    # Multiple possible job locations
    locations: Optional[ValidatedStringList] = None  
    
    # Industry-specific experience required (e.g., 'Tech', 'Finance', etc.)
    industryExperience: Optional[ValidatedStringList] = None 
    
    # Hard skills required (e.g., 'Python', 'Data Analysis', etc.)
    hardSkills: Optional[ValidatedStringList] = None
    
    # Soft skills required (e.g., 'Communication', 'Leadership', etc.)
    softSkills: Optional[ValidatedStringList] = None

    @field_validator(*enumKeys, mode='before')
    @classmethod
    def to_lower_case_strings(cls, value: str | list[str]) -> str | list[str]:
        if isinstance(value, list):
            value = sanitize_string_list([itm.lower() for itm in value])
        else:
            value = sanitize_string(value.lower())
        return value

##########################################

class Links(BaseModel):
    platform: str
    url: str
    
class ProfessionalExperience(BaseModel):
    job_title: Optional[str] = None
    company_name: Optional[str] = None
    date: Optional[str] = None
    work_done: Optional[str] = None

class Education(BaseModel): 
    degree_type: Optional[str] = Field(None, description="The degree type (e.g., matric, intermediate, associate, bachelor's, master's, and doctoral)")
    major: Optional[str] = Field(None, description="The major or field of study (e.g., Computer Science, Statistics, zoology)")
    institute_name: Optional[str] = Field(None, description="The name of the educational institution (e.g., \"University of Karachi\")")
    graduation_date: Optional[str] = Field(None, description="The graduation date in the format \"YYYY-MM-DD\" or \"YYYY-MM-DD - YYYY-MM-DD\" or \"YYYY-MM-DD - Present\" (if available)") 

class Certification(BaseModel):
    name: Optional[str] = None
    issuing_organization: Optional[str] = None
    date_issued: Optional[str] = Field(None, description="format \"YYYY-MM-DD\"")

class Achievement(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    date: Optional[str] = Field(None, description="format \"YYYY-MM-DD\"")

class Project(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    url: Optional[str] = None

class ResumeObject(BaseModel):
    name: Optional[str] = "John Doe"
    title: Optional[str] = "Senior Software Engineer"
    email: Optional[list[str]] = ["john.doe@example.com"]
    number: Optional[list[str]] = ["123-456-7890"]
    address: Optional[str] = "123 Main St, Anytown, USA"
    professional_summary: Optional[str] = "Experienced software engineer with a strong background in developing scalable web applications."
    soft_skills: Optional[list[str]] = ["Dummy Skill-1", "Dummy Skill-2"]
    technical_skills: Optional[list[str]] = ["Dummy Skill-1", "Dummy Skill-2"]
    social_links: Optional[list[Links]] = [{"platform": "LinkedIn", "url": "https://www.linkedin.com/in/johndoe"}]
    achievements: Optional[list[Achievement]] = None
    certifications: Optional[list[Certification]] = None
    education: Optional[list[Education]] = None
    projects: Optional[list[Project]] = None
    professional_experience: Optional[list[ProfessionalExperience]] = None


    @field_validator('name', 'title', 'email', 'number', 
                     'address', 'soft_skills', 'professional_summary', 
                     'education', 'technical_skills', 'achievements',
                     'certifications', 'professional_experience')
    @classmethod
    def set_null_to_default(cls, v: str, info: ValidationInfo) -> str:
        if v is None:
            return cls.model_fields[info.field_name].default
        return v