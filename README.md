# Sentiment Analysis Backend

This is the backend for the **Sentiment Analysis Tool**. It provides a REST API built with **FastAPI** to handle sentiment analysis requests for product reviews and social media posts. The backend is also responsible for storing and retrieving review data from a **PostgreSQL** database.

## 🚀 Features

- **Product Review Analysis**: Analyze product reviews from multiple sources.
- **Social Media Analysis**: Extract and analyze comments from social media posts (e.g., Twitter, Reddit).
- **Sentiment Analysis**: Uses a machine learning model to classify sentiments (positive/negative/neutral).
- **Database**: Store and retrieve analysis results and user data.

## 🛠️ Setup and Installation

### Prerequisites

- Python 3.x
- PostgreSQL database

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/sna-back.git
cd sna-back
```
### 2. Create a Virtual Environment
```bash
python -m venv venv

#To Activate the environment in Windows: venv\Scripts\activate
#To Activate in Mac/Linus: source venv/bin/activate
```
### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
### 4. Set Up Database
Ensure your PostgreSQL database is running. Update the .env file with your database credentials:
```bash
DATABASE_URL=postgresql://username:password@localhost/dbname
```
### 5. Run the FastAPI Server
```bash
uvicorn app.main:app --reload
```
