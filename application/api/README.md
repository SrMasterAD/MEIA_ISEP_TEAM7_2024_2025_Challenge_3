## Setup

1. Clone the repository
2. Navigate to the folder ->> **/application/api** <<-- :
  - `cd MEIA_ISEP_TEAM7_2024_2025_Challenge_3/application/api`
3. Create and activate a virtual environment
4. The commands to do that:

```bash

python3 -m venv .venv
source .venv/bin/activate  # or .\.venv\Scripts\Activate.ps1 on Windows
pip3 install -r requirements.txt
```
5. Setup Postgres container with docker-compose:
    - It need docker-compose or Docker Desktop installed
```bash

docker-compose up -d

```

## Running the app
After active the .venv run the following command in the -->> **MEIA_ISEP_TEAM7_2024_2025_Challenge_3** <<-- folder e.g the root folder of challenge 3:
 - `cd MEIA_ISEP_TEAM7_2024_2025_Challenge_3`
``` bash

uvicorn application.api.main:app --reload

```

### Postman collection
File: postman_collection/deep_wheat_collection.postman_collection.json
Steps to Use
Open Postman

Click Import → Select the collection file

Use the Login request to authenticate

The login request automatically stores the JWT in {{token}}

Other requests use Bearer {{token}} for authentication