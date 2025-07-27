<img width="2154" height="607" alt="image" src="https://github.com/user-attachments/assets/5040ceab-8f5e-4f26-9def-56f9415a023d" />

<h1> Google Agentic AI Day Hackathon</h1>

<h5> AI-Powered Financial Advisor Chatbot </h5>
This repository contains the source code for an advanced Financial Advisor chatbot built using Google's Agent Development Kit (ADK) and deployed on Google Cloud Run. The application leverages Google's Generative AI models through Vertex AI to provide intelligent financial advice, answer user queries, and perform related tasks.

<h2> **Steps to use working AI-Powered Financial Advisor Chatbot Prototype (MVP)** </h2>

Please follow the below steps:

1. Access url: https://finadvisorai-chat.web.app/
2.  Start with Hi/Hello. and ask any finacial query like get my credit score , get my networ, get my epf details, get mutual funds etc.

<img width="2500" height="1454" alt="image" src="https://github.com/user-attachments/assets/cb01379f-5099-4f6e-9841-0a8a5a5067ce" />

3. It will ask you for the sign into this url : https://fi-mcp-prod-server-93313385804.us-central1.run.app/mockWebPage?sessionId=mcp-session-594e48ea-fea1-40ef-8c52-7552dd9272af.
4. Please enter dymmy mobile number and dummy OTP as Login : 2222222222
                                                       OTP : 12345
<img width="2390" height="1461" alt="image" src="https://github.com/user-attachments/assets/d76cf4b8-0486-49f9-a725-1f48a2fbe4d8" />

5. Continue with Chatbot and ask queries about your personal financial data.

As Chatbot is using financial data from Fi Money MCP Server. This login is required.

Note: Some dummpy data is mocked in Fi Money MCP dev Server.

**Recorded Demo :** https://drive.google.com/drive/folders/1PC9yjoU4Ol6ETBJItrHDeLLC_7bIWHnT?usp=sharing

The frontend is a simple, clean web interface built with React and hosted on Firebase Hosting, providing a seamless user experience.
D✨ **Features**

Conversational AI: Utilizes Google's powerful language models (e.g., Gemini) for natural and intelligent conversations.

Tool Integration: The agent can use custom tools to fetch real-time financial data, perform calculations, or connect to other services.

Scalable Backend: Built with FastAPI and deployed as a serverless container on Google Cloud Run, ensuring it can handle a high volume of requests efficiently.

Web-Based UI: A clean, responsive user interface built with React and hosted on Firebase, allowing users to interact with the agent easily.

Secure and Managed: Leverages Google Cloud's robust infrastructure for security, logging, and monitoring.

🛠️ **Tech Stack**
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

🚀 **Getting Started**
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
git clone https://github.com/naidu9678/google_agentic_ai_day
cd google_agentic_ai_day
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

You have now successfully deployed the AI-powered financial advisor

can you give one signle copy and paste format. I still need more professional way.
can you give one signle copy and paste format. I still need more professional way.
Of course. Here is a professional, comprehensive, and well-structured README.md file that you can copy and paste directly into your GitHub repository. It includes placeholders for you to fill in specific details.

AI-Powered Financial Advisor
[
[
[
[

An intelligent, conversational financial advisor powered by Google's Agent Development Kit (ADK) and Gemini models. This application provides a seamless, serverless architecture using Google Cloud Run for the backend and a responsive React frontend hosted on Firebase.

🏛️ **Architecture**

This project is built on a modern, serverless architecture designed for scalability, security, and low maintenance.

Frontend: A React-based single-page application (SPA) hosted on Firebase Hosting. It communicates with the backend via HTTP requests.

Backend: A Python FastAPI application running in a container on Google Cloud Run. This service exposes the agent's conversational interface.

Agent Core: The agent logic is built using the Google Agent Development Kit (ADK), which orchestrates calls to Google's Gemini large language models via the Vertex AI API.

Build & Deployment: Source code is automatically built into a container image by Google Cloud Build and deployed to Cloud Run.

<p align="center"><img width="2373" height="1321" alt="image" src="https://github.com/user-attachments/assets/746b2747-b4ec-4955-86c2-d6c42da54d68" />
</p>

✨ **Key Features**
Natural Language Interaction: Ask complex financial questions in plain English.

Extensible Tool Use: The agent is built to use custom tools (e.g., for real-time stock data, calculations, or accessing financial APIs).

Scalable & Cost-Effective: Serverless architecture on Cloud Run scales to zero, so you only pay for what you use.

Secure: Leverages Google Cloud's Identity and Access Management (IAM) for secure service-to-service communication.

Centralized Logging: Integrated with Google Cloud's operations suite (formerly Stackdriver) for robust monitoring and debugging.

🛠️ Tech Stack
Category	Technology / Service
Backend	
AI / LLM	![Vertex AI](https://img.shields.io/badge/Vertex_AI-4285F4?style=for-the-badge&logo=google-cloud&logoColor=white
Frontend	
Infrastructure	![Google Cloud](https://img.shields.io/badge/Google_Cloud-4285F4?style=for-the-badge&logo= ![Docker](https://img.shields.Prerequisites
Google Cloud Project: Create or select a GCP project.

Enable APIs: In your GCP project, enable the following APIs:

Cloud Run API

Cloud Build API

Vertex AI API

Artifact Registry API

Install SDKs:

Google Cloud SDK (gcloud CLI)

Node.js and npm

Python 3.10+

Authenticate:

bash
gcloud auth login
gcloud auth application-default login
gcloud config set project YOUR_PROJECT_ID
💻 Local Development
1. Clone the Repository
bash
git clone https://github.com/naidu9678/google_agentic_ai_day.git
cd your-repo-name
2. Configure Environment
Create a .env file inside the backend/ directory with your project details:

File: backend/.env

text
GOOGLE_CLOUD_PROJECT="your-gcp-project-id"
GOOGLE_CLOUD_LOCATION="us-central1"
# Add any other required environment variables, like API keys for tools.
3. Run the Backend
The backend is a FastAPI application that can be run locally using the ADK's development server.

bash
# Navigate to the backend directory
cd backend

# Create and activate a Python virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the local development server
adk web
Your agent's API is now running, typically at http://127.0.0.1:8000.

4. Run the Frontend
The frontend is a React application that provides the chat interface.

bash
# Open a new terminal and navigate to the frontend directory
cd frontend

# Install dependencies
npm install

# Start the React development server
npm start
Your web app should now be accessible at http://localhost:3000 and will be configured to communicate with your local backend.

☁️ Cloud Deployment
Step 1: Deploy the Backend to Cloud Run
The gcloud run deploy command uses Google's built-in Buildpacks to containerize and deploy the application from your source code.

Navigate to the backend directory.

Run the deployment command:

bash
gcloud run deploy financial-advisor-ai-backend \
  --source . \
  --region "us-central1" \
  --memory "2Gi" \
  --timeout "600s" \
  --allow-unauthenticated
--memory "2Gi": Allocates 2 GiB of memory. AI/ML libraries can be memory-intensive.

--timeout "600s": Sets a 10-minute timeout for requests, useful for long-running agent tasks.

--allow-unauthenticated: Makes the endpoint public. For production, you should implement IAM-based authentication.

After the deployment succeeds, copy the Service URL provided in the output. It will look like: https://financial-advisor-ai-backend-xxxxxxxxxx-uc.a.run.app

Step 2: Configure and Deploy the Frontend to Firebase
Update the API Endpoint:

In the frontend source code, find the configuration file where the backend URL is set (e.g., src/config.js or directly in a component).

Replace the local URL (http://localhost:8000) with the Cloud Run Service URL you copied in the previous step.

Initialize Firebase (if you haven't already):

bash
# Run from the /frontend directory
firebase init hosting
Select Use an existing project and choose your GCP project.

What do you want to use as your public directory? build

Configure as a single-page app (rewrite all urls to /index.html)? Yes

Set up automatic builds and deploys with GitHub? No

Build and Deploy the Frontend:

bash
# Run from the /frontend directory
npm run build
firebase deploy --only hosting
Once complete, Firebase will provide the Hosting URL. This is the public link to your production-ready chatbot!


