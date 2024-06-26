# Authentication

## Overview
  Login using phone number with OTP validation


## Installation

1. Clone the repository:
    ```sh
    git clone "Project URL"
    ```

2. Navigate to the project directory:
    ```sh
    cd auth
    ```

3. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

4. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the development server:
    ```sh
    python manage.py runserver
    ```

2. Access the application at `http://127.0.0.1:8000/`.

## API Endpoints

### Send OTP
- **URL**: `/api/send-otp/`
- **Method**: `POST`
- **Data Params**: `{"phone_number": "<phone_number>"}`
- **Output**: `{"message": "OTP sent successfully!","OTP": "<otp>"}`

### Verify OTP
- **URL**: `/api/verify-otp/`
- **Method**: `POST`
- **Data Params**: `{"phone_number": "<phone_number>", "otp_code": "<otp_code>"}`
- **Output**: `{"message": "Mobile number verified successfully !"}`

### Admin

Before invoking admin api you should create super user.

```sh
    python manage.py createsuperuser
```

- **URL**: `/api/admin/`
- **Method**: `GET`






