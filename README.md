#  HNG 9 INTERNSHIP

# Backend Stage 1 Task

## Study Material

-   [learn http methods - w3schools](https://www.w3schools.com/tags/ref_httpmethods.asp)
-   [learn http request methods - FreeCodeCamp](https://www.freecodecamp.org/news/http-request-methods-explained/)

## Task Description

-   Setup a server (Host)
    
-   Create an **(GET)** api endoint that returns the following json response:
    
    { "**slackUsername**": String, "**backend**": Boolean, "**age**": Integer, "**bio**": String }
    
    -   SlackUsername should be a **string** datatype and your slack username
    -   Backend should be a **boolean** datatype
    -   Age should be an **integer** datatype
    -   Bio(description about yourself) should be a **string** datatype
-   Push to **GitHub**
    

**Sample Input:** does not apply ****None

**Sample Response Format** { "**slackUsername**": String, "**backend**": Boolean, "**age**": Integer, "**bio**": String }

## Production url:
https://hng9stage1-production-87ae.up.railway.app/

## Task 2 Requirements

**Backend Stage 2 Task****![:bulb:](https://a.slack-edge.com/production-standard-emoji-assets/14.0/google-medium/1f4a1.png)**  Study Material  
[REST API TUTORIAL](https://www.gravitee.io/blog/rest-api-tutorial)**![:bulb:](https://a.slack-edge.com/production-standard-emoji-assets/14.0/google-medium/1f4a1.png)**  Task Description  

-   Using the same server setup from stage one
-   Create an  **(POST)**  api endoint that takes the following sample json:
-   { “**operation_type**”: Enum <addition | subtraction | multiplication> , “**x**”: Integer, “**y**”: Integer }

-   Operation can either be addition, subtraction or mutiplication
-   **x**  can be a number and Integer datatype
-   **y**  can be a number and Integer datatype

-   Based on the operation sent, perform a simple arithmetic operation on  **x**  and  **y**
-   Return a response with the result of the operation and your slack username
-   { “**slackUsername**”: String, "**operation_type**" : Enum. value, “**result**”: Integer }
-   Push to GitHub

**Sample Input**  { “**operation_type**”: Enum <addition | subtraction | multiplication> , “**x**”: Integer, “**y**”: Integer }**Sample Response Format**  { “**slackUsername**”: String, “**result**”: Integer, “**operation_type**”: Enum.value }**

## Production Url:
https://hng9stage1-production-87ae.up.railway.app/stage2/