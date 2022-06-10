from pydantic import BaseModel, ValidationError, constr, validator, root_validator


class UserModel(BaseModel):
    email: str
    password: str
    confirm_password: str
    amount: int

    @validator('email')
    def validate_google_email(cls, value):
        print("value", value)
        if(not value.endswith("google.com")):
            raise ValueError("only accepts google.com domain emails")
        return value
    
    @root_validator(pre=False)
    def validate_passwords(cls, values):
        amount = values.get("amount")
        print(type(amount))
        if(values.get("password") != values.get("confirm_password")):
            raise ValueError("Passowrds did not match")
        return values

data = {
    "email": "anji@localhost.com",
    "password": "secret",
    "confirm_password": "secret1",
}


try:
    obj = UserModel(**data)
    print(obj.json())
except ValidationError as e:
    print(e.json())
