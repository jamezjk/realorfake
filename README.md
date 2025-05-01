# realorfake
A real time fake news detector extension.


HOW TO USE THIS BACKEND:

1. Rename your downloaded Google Service Account JSON file to: service_account_key.json
2. Place it in this same folder.
3. Replace "your-gcp-project-id" in app.py with your actual GCP project ID.
4. Run this backend using:
   pip install -r requirements.txt
   python app.py
5. Send a POST request to http://localhost:5000/verify-news with a JSON body like:
   {
     "text": "Some news headline here"
   }
