# Pydantic Validators

## 🧮 Computed Fields

Computed fields derive values dynamically at runtime using `@computed_field`. These fields **aren’t provided as input** but are **calculated from existing fields**. 

### Usecase 1: Extracting a Username from an Email

```python linenums="1" hl_lines="9-12"
from pydantic import BaseModel, Field, computed_field

def extract_username(email: str) -> str:
    return email.split("@")[0]

class User(BaseModel):
    email: str = Field(..., description="User's email address.")

    @computed_field
    @property
    def username(self) -> str:
        return extract_username(self.email)

# Example usage
user = User(email="foobar@example.com")
print(user.username)  # foobar
print(user.model_dump())  
"""
{
  'email': 'foobar@example.com',
  'username': 'foobar'
}
"""
```

???+ note  
    Computed fields are **evaluated every time** they are accessed. This means that calling `user.username`, printing it, or dumping the model (`model_dump()`) will **recompute** the value dynamically. 


## ✅ Field Validators

Field validators **modify, validate, or transform** individual fields before assignment. They can run **before or after** field processing (`mode="before"` or `"after"`). 

### Usecase 1: Replace `None` with Defaults  
Pydantic keeps `None` if explicitly provided, even if a default exists. A **field validator** ensures `None` is replaced with the field’s default.  

???+ tip  
    Useful for handling AI or API data where `None` should be replaced with defaults for consistency.

```python linenums="1" hl_lines="9-14"
from typing import Optional
from pydantic import BaseModel, field_validator

class User(BaseModel):
    username: Optional[str] = "foo_user"
    age: Optional[int] = 25
    email: Optional[str] = "foo@example.com"

    @field_validator("username", "age", mode="before")
    @classmethod
    def replace_null_with_default(cls, value, info):
        if value is None:
            return cls.model_fields[info.field_name].default
        return value

# Example usage
llm_response = {"username": "bar_user",  "age": None,  "email": None}
user = User.model_validate(llm_response)
print(user.model_dump_json(indent=2))
"""
{
  "username": "bar_user",
  "age": 25,
  "email": null
}
"""
```

### Usecase 2: Replace Empty Strings with `"N/A"`

By default, Pydantic does not modify empty strings. If you want to replace all empty string values with `"N/A"`, you can use a **field validator** to process them automatically.

???+ tip  
    This is useful for ensuring that empty input fields from forms, APIs, or databases do not remain blank but are replaced with a meaningful default value.

```python linenums="1" hl_lines="7-10"
from pydantic import BaseModel, field_validator

class User(BaseModel):
    name: str
    email: str

    @field_validator("*", mode="before")
    @classmethod
    def replace_empty(cls, value):
        return "N/A" if value == "" else value

# Example usage
user = User(name="", email="foo@bar.com")
print(user.model_dump())
"""
{
  'name': 'N/A',
  'email': 'foo@bar.com'
}
"""
```


## 🧩 Model Validators

Model validators enforce rules that involve **multiple fields**. They run **after all fields are validated**, ensuring cross-field constraints and dependencies are met.

### Usecase 1: Enforce Exactly One Optional Field

Sometimes, a model has two optional fields, but **at least one must be provided** while preventing both from being set simultaneously.  

???+ tip
    This is useful for ensuring users provide **either one type of input or another** but not both.

```python linenums="1" hl_lines="8-12"
from typing import Optional
from pydantic import BaseModel, model_validator

class FooBarModel(BaseModel):
    foo: Optional[str] = None
    bar: Optional[str] = None

    @model_validator(mode="after")
    def validate_exclusive_fields(self):
        if (self.foo is None) == (self.bar is None):
            raise ValueError("Either `foo` or `bar` must be provided, but not both.")
        return self

# Example usage
FooBarModel(foo="abc")  # ✅ Valid
FooBarModel(bar="xyz")  # ✅ Valid
FooBarModel()  # ❌ Raises error
FooBarModel(foo="abc", bar="xyz")  # ❌ Raises error
```


<!-- 



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



 -->
