# 🎓 Rec My Prof - SJSU Professor Finder

> An AI-powered chatbot to help SJSU students find the perfect professor match.

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🤖 AI Chatbot | Get instant insights about professors using natural language |
| 🔍 Smart Search | Find professors by name, course, or department |
| 📊 Detailed Ratings | View comprehensive professor ratings and reviews |
| 📝 Course Info | See which professors teach specific courses |
| 📱 Responsive UI | Works seamlessly on desktop and mobile |

## 📸 Screenshots

<details>
<summary>View Screenshots</summary>

### 1. Homepage with AI Chatbot
![Homepage](assets/ss1.png)

### 2. Professor Search Interface
![Search](assets/ss2.png)

### 3. Course Query Results
![Course Query](assets/ss3.png)

### 4. Detailed Professor Information
![Professor Details](assets/ss4.png)

### 5. Quick Tips & Suggestions
![Quick Tips](assets/ss5.png)

</details>

## 🛠️ Tech Stack

### Backend
- **FastAPI** - Modern Python web framework
- **OpenAI API** - Powers the AI chatbot
- **Pinecone** - Vector database for efficient queries
- **SessionMiddleware** - User session management

### Frontend
- **HTML/CSS/JavaScript** - Core web technologies
- **WebSocket** - Real-time chat functionality
- **Responsive Design** - Mobile-friendly interface

### Data & Analytics
- **Pandas** - Data processing
- **Plotly** - Interactive visualizations
- **Jinja2** - Template rendering

## 🚀 Quick Start

1. **Clone the Repository**
   ```bash
   git clone https://github.com/veedhibhanushali/rec-my-prof.git
   cd rec-my-prof
   ```

2. **Set Up Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate     # On Windows
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys
   ```

5. **Run the Application**
   ```bash
   uvicorn main:app --reload
   ```

## 🔑 Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `OPENAI_API_KEY` | OpenAI API key | Required |
| `PINECONE_API_KEY` | Pinecone API key | Required |
| `PINECONE_REGION` | Pinecone region | us-east-1 |
| `SECRET_KEY` | Session secret key | Required |

## 📝 License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

## 👥 Contact

- 📧 Email: bhanushaliveedhi@gmail.com
- 🌐 GitHub: [veedhibhanushali](https://github.com/veedhibhanushali)
- 🔗 Demo: [Live Demo](https://rec-my-prof.vercel.app)

---
<div align="center">
Made with ❤️ by Veedhi Bhanushali
</div>

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

