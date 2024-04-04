# Feature Toggle API

The Feature Toggle API is a Django project designed to provide a standardized interface for managing feature toggles within a software system.

## Requirements

- Python 3.x

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/feature-toggle-api.git

2. Navigate to the project directory:
    ```bash
   cd feature-toggle-api
   
3. Create a virtual environment (optional but recommended):
    ```bash
   python3 -m venv venv
4. Activate the virtual environment:

    For Windows:
    ```bash
    venv\Scripts\activate
    
   
    For Linux:
    
    source venv/bin/activate

5. Install dependencies using pip:
    ```bash
   pip install -r requirements.txt
6. Apply database migrations:
   ```bash
   python manage.py migrate
7. Run the development server:
   ```bash
   python manage.py runserver
8. Access the API at http://127.0.0.1:8000/.

## API Endpoints

- **GET /feature-toggles/**: Retrieve a list of all feature toggles.
- **POST /feature-toggles/**: Create a new feature toggle.
- **GET /feature-toggles/<toggle_id>/**: Retrieve details of a specific feature toggle.
- **PUT /feature-toggles/<toggle_id>/**: Update an existing feature toggle.
- **DELETE /feature-toggles/<toggle_id>/**: Delete a feature toggle.
