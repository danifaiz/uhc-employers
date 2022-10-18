# Flask API to Fetch UHC Employers

API structured to fetch and search employers by Name & EIN.

## Dependencies

- [flask](https://palletsprojects.com/p/flask/): Python server of choise
- [requests]

## Set Up

1. Check out the code
2. Install requirements
    ```
    pip install requests
    pip install python-dotenv
    ```
3. Activate the virtual env:
    ```
   . venv/bin/activate
    ```
4. Run the server locally
    ```
   flask run
    ```

5. Visit http://127.0.0.1:5000/ for the welcome screen
   
## APIs

1. http://127.0.0.1:5000/api/v1/employer/sync ( First fetch and saves data from UHC Transparency Site )
2. http://127.0.0.1:5000/api/v1/employer?search=united&type=name ( Ability to Search by Type: ein or name )
