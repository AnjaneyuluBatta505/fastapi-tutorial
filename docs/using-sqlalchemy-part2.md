
1. Create new category [DONE]

    `POST /categories`

    payload:
    ```
    {
        "name": "string",
        "description": "string"
    }
    ```
    response status code: `201`

2. List all categories **[TODO]**

    `GET /categories`

    response status code: `200`
    expected response:

    ```
    [
        {
            "name": "string",
            "description": "string",
            "id": "int"
        }
    ]
    ```

3. Retrieve category by id **[TODO]**

    `GET /categories/<pk>`

    response status code: `200`

    expected response:
    
    ```
    {
        "name": "string",
        "description": "string",
        "id": "int"
    }
    ```

    constraints:

        - Return 404 response if not found

4. Update category by id **[TODO]**

    `PUT /categories/<pk>`

    updatable attributes/columns: `name`, `description`

    response status code: `200`

    expected response:
    
    ```
    {
        "name": "string",
        "description": "string",
        "id": "int"
    }
    ```

    constraints:

        - Do not update if category already exists
        - Return 404 response if not found

5. Delete category by id **[TODO]**

    `DELETE /categories/<pk>`

    response status code: `204`

    expected response: no body


## Example categories:

Appliances

    Shop Wide range of Appliances Online in India from Pepperfry such as Kitchen Appliances, Screens, Home Appliances at Best Price.

Apps & Games

    Top 50 games apps ranking in android Google Play Store in India by installs and usage data - See the Full list here.

Arts, Crafts, & Sewing

    Discover the best Arts, Crafts & Sewing in Best Sellers. Find the top 100 most popular items in Amazon Arts, Crafts & Sewing Best Sellers.
