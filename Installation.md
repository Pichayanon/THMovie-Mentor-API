## Instructions for how to install and configure application

> Note : If you run the code below and find ***python : command not found***, change **python** to **python3**.

1. Clone repository from GitHub to your computer.
    ```
    git clone https://github.com/Pichayanon/THMovie-Mentor-API.git
    ```

2. Create virtual environment.
    ```
   python -m venv venv
   ```
3. Start the virtual environment.
   * macOS / Linux
     ```
     . venv/bin/activate 
     ```
   * Windows
     ```
     venv\Scripts\activate
     ```
4. Install dependencies.
   ```
   pip install -r requirements.txt
   ```
   > Note : If you can't use **pip**, change it to **pip3**.
5. Set values for externalized variables.
   * macOS / Linux
     ```
     cp sample.env .env 
     ```
   * Windows
     ```
     copy sample.env .env
     ```
6. Change directory to api.
    ```
    cd  api
    ```
7. Run migrations.
   ``` 
   python manage.py migrate
   ```
8. Run test.
   ``` 
    python manage.py test THMovie 
   ```

   
