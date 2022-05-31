## simple create [i.e POST] api endpoint

```
POST /api/users

{
    "first_name": "anji",
    "last_name": "b",
    "email": "anji@localhost.com",
    "date_of_birth": "invalid"
}

If valid data then
    create an entry into the database & return the success response
    response: 201

If invalid then
    return error response with validation errors
    response: 422

```

## getting started with pydantic

- What is pydantic?
  - data validation
  - convert data to json/dict
- Field Types
  - default python types
    - int, str, Enum, etc.
  - pydantic constrained types
    - constr, confloat, etc
- Custom validators
  - root_validator
  - validator
- Pydantic Recursive Models [i.e nested data]
  - product and category data
