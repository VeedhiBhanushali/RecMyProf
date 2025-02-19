📌 Rec My Prof - Find Your Ideal Professor

🚀 Discover professors that match your learning style and academic goals at San José State University.

🌟 Features

🔹 Personalized Professor Recommendations - Discover professors based on learning preferences and workload.
🔹 AI-Powered Chatbot - Get instant professor insights, ratings, and course details using AI.
🔹 Advanced Filtering - Search by department, professor rating, difficulty, and student feedback.
🔹 Comprehensive Analytics - Visualize professor rating distributions, teaching styles, and department comparisons.
🔹 Interactive Visualizations - Dynamic data representation with Plotly for an intuitive dashboard.
🔹 User-Friendly Interface - A responsive UI with an intuitive design.

🖼️ Screenshots

🎯 Personalized Search for Professors
💬 AI Chatbot for Quick Queries
📊 Detailed Professor Insights
📈 Analytics & Data Visualization
🛠️ Tech Stack

Backend (API & Server)
FastAPI - A modern, high-performance Python framework for building APIs.
Flask - Used for handling specific routes and microservices.
SessionMiddleware - Manages user sessions within FastAPI.
Frontend (User Interface)
HTML/CSS - For structuring and styling the web pages.
JavaScript - Client-side interactivity and API requests.
Plotly - Interactive data visualization for analytics dashboards.
Material Icons - Used for a clean and professional UI.
Data Handling & Processing
Pandas - Data manipulation and analysis for professor data.
Jinja2 - Dynamic templating for HTML rendering.
Environment Management
dotenv - Loads environment variables securely from a .env file.
AI & External APIs
OpenAI API - AI-powered chatbot for professor insights.
Pinecone - Vector database service used for efficient data retrieval.
Data Visualization
Plotly - Creates interactive charts and graphs to display professor performance insights.
📦 Installation & Setup

1️⃣ Clone the Repository

git clone https://github.com/veedhibhanushali/rec-my-prof.git
cd rec-my-prof
2️⃣ Create a Virtual Environment

python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
3️⃣ Install Dependencies

pip install -r requirements.txt
npm install  # If frontend has additional dependencies
4️⃣ Set Up Environment Variables
Create a .env file in the root directory and configure:

OPENAI_API_KEY=your_openai_api_key
PINECONE_API_KEY=your_pinecone_api_key
DATABASE_URL=your_database_url
GITHUB_CLIENT_ID=your_github_client_id
GITHUB_CLIENT_SECRET=your_github_client_secret
5️⃣ Run the Backend (FastAPI & Flask)

uvicorn main:app --host 0.0.0.0 --port 8000 --reload
6️⃣ Run the Frontend

npm run dev  # or yarn dev
The app will be available at http://localhost:3000

📌 How It Works

Select Your Learning Preferences
Choose classroom experience, grading criteria, and workload.
Filter Professors
Adjust by department, rating, difficulty, and "Would Take Again" percentage.
Explore Professor Profiles
View ratings, teaching styles, workload, and real student reviews.
AI Chatbot Support
Get instant answers to professor-related questions.
Analytics & Insights
Interactive visual dashboards for rating distributions and departmental comparisons.
📊 Roadmap

🔹 Enhance AI Chatbot - Improve responses using fine-tuned OpenAI models.
🔹 Add Student Reviews - Allow students to submit and upvote reviews.
🔹 Compare Professors - Side-by-side comparison of two professors.
🔹 Course Difficulty Insights - Aggregate course difficulty ratings across multiple professors.

📢 Contributing

We welcome contributions! 🚀

Fork the repository
Create a feature branch
git checkout -b feature-new-enhancement
Commit your changes
git commit -m "Added new feature"
Push and create a pull request
git push origin feature-new-enhancement
📜 License

This project is licensed under the MIT License. See LICENSE for details.

✨ Contact

📩 Email: bhanushaliveedhi@gmail.com
🌐 GitHub: veedhibhanushali
🚀 Live Demo: Rec My Prof

# SJSU Professor Chatbot

A chatbot that provides information about SJSU professors, including:
- Contact information
- Office hours
- Ratings and reviews
- Course information
- Research interests

## Setup
1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Copy `.env.example` to `.env` and fill in your API keys
4. Run the server: `uvicorn main:app --reload`

## Environment Variables
Required environment variables:
- OPENAI_API_KEY
- PINECONE_API_KEY
- PINECONE_REGION

