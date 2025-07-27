AI-Powered Financial Advisor Chatbot
This repository contains the source code for an advanced Financial Advisor chatbot built using Google's Agent Development Kit (ADK) and deployed on Google Cloud Run. The application leverages Google's Generative AI models through Vertex AI to provide intelligent financial advice, answer user queries, and perform related tasks.

The frontend is a simple, clean web interface built with React and hosted on Firebase Hosting, providing a seamless user experience.

![Project Architecture](https://storage.googleapis.com/gweb-cloudblog-publish/images/AD✨ Features

Conversational AI: Utilizes Google's powerful language models (e.g., Gemini) for natural and intelligent conversations.

Tool Integration: The agent can use custom tools to fetch real-time financial data, perform calculations, or connect to other services.

Scalable Backend: Built with FastAPI and deployed as a serverless container on Google Cloud Run, ensuring it can handle a high volume of requests efficiently.

Web-Based UI: A clean, responsive user interface built with React and hosted on Firebase, allowing users to interact with the agent easily.

Secure and Managed: Leverages Google Cloud's robust infrastructure for security, logging, and monitoring.

🛠️ Tech Stack
Backend:

Framework: FastAPI

Agent Logic: Google Agent Development Kit (ADK)

Language: Python

Server: Gunicorn with Uvicorn workers

AI & Machine Learning:

Models: Google Gemini (via Vertex AI)

Platform: Google Vertex AI

Frontend:

Library: React.js

Hosting: Firebase Hosting

Deployment & Infrastructure:

Containerization: Docker (via Google Cloud Buildpacks)

Hosting: Google Cloud Run

CI/CD: Google Cloud Build

🚀 Getting Started
Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

Prerequisites
Python 3.10+

Node.js and npm (for the React frontend)

Google Cloud SDK (gcloud CLI) installed and authenticated.

A Google Cloud Project with the following APIs enabled:

Cloud Run API

Cloud Build API

Vertex AI API

Artifact Registry API

Firebase CLI installed and authenticated.

Local Development Setup
1. Clone the Repository
bash
git clone https://github.com/your-username/financial-advisor-ai.git
cd financial-advisor-ai
2. Set Up the Backend
The backend is a FastAPI application that serves the agent.

bash
# Navigate to the backend directory
cd backend

# Create and activate a Python virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

# Install required Python packages
pip install -r requirements.txt

# Set up your environment variables
# Create a .env file in the `backend` directory and add your Google Cloud Project ID
echo "GOOGLE_CLOUD_PROJECT=your-gcp-project-id" > .env

# Authenticate for local development
gcloud auth application-default login
3. Run the Backend Locally
Use the ADK's built-in web server for local testing. This provides a simple UI to interact directly with your agent.

bash
adk web
This will start a server, typically on http://localhost:8000. Open this URL in your browser to test the agent.

4. Set Up and Run the Frontend
The frontend is a React application located in the frontend directory.

bash
# Navigate to the frontend directory from the root
cd ../frontend

# Install dependencies
npm install

# Start the React development server
npm start
This will launch the chatbot interface, which will be connected to your local backend.

☁️ Deployment to Google Cloud
This project is designed to be deployed with a serverless architecture using Google Cloud Run for the backend and Firebase Hosting for the frontend.

1. Backend Deployment to Cloud Run
The backend is deployed as a containerized service using Cloud Buildpacks, which automatically detect the Python environment and dependencies.

Important: Before deploying, make sure your Procfile in the backend directory is correctly configured:

text
web: gunicorn -w 4 -k uvicorn.workers.UvicornWorker -b 0.0.0.0:$PORT main:app
Navigate to the backend directory and run the following command:

bash
gcloud run deploy financial-advisor-ai-backend \
  --source . \
  --region "us-central1" \
  --memory "2Gi" \
  --allow-unauthenticated \
  --project "your-gcp-project-id"
--source .: Deploys the code from the current directory.

--region: Specify your preferred Google Cloud region.

--memory "2Gi": Allocates 2 GiB of memory. This is often necessary for AI/ML libraries.

--allow-unauthenticated: Makes the service publicly accessible. Remove this flag for private services.

Once deployed, gcloud will provide you with a Service URL. You will need this for the frontend configuration.

2. Frontend Deployment to Firebase
The React app needs to know the URL of your deployed Cloud Run backend.

a. Configure the Backend URL:

In your frontend/src directory, locate the file where the API endpoint is defined (e.g., api.js or App.js) and update it with your Cloud Run Service URL.

b. Build the React App:

bash
# In the /frontend directory
npm run build
This creates an optimized, static build of your application in the build directory.

c. Deploy to Firebase Hosting:

If you haven't already, initialize Firebase in your project:

bash
# Run this from the /frontend directory
firebase init hosting
Follow the prompts:

Select your Firebase project.

Set your public directory to build.

Configure as a single-page app (SPA): Yes.

Set up automatic builds and deploys with GitHub: No (for now).

Now, deploy the application:

bash
firebase deploy --only hosting
Firebase will provide you with a Hosting URL. This is the public URL for your chatbot.
