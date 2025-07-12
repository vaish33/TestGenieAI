# 🧠 TestGenieAI – GenAI-Based Test Case Generator

TestGenieAI is a Generative AI-powered app built with **Streamlit** + **OpenAI API** to generate high-quality UI, API, functional, Data Quality test cases— instantly! 

### 🚀 Features
- Generate **positive & negative test cases**
- Supports UI, API, and functional testing , Data Quality
- Powered by **OpenAI GPT**
- Beautiful UI built with Streamlit
- One-click copy for test cases

### 🛠️ Tech Stack
- Python 🐍
- Streamlit 🌐
- OpenAI API 🤖
- dotenv (.env) for secret management

### 🔐 Setup Locally

```bash
# 1. Clone the repo
git clone https://github.com/vaish33/TestGenieAI.git
cd TestGenieAI

# 2. Create virtual env (optional but recommended)
python -m venv testgenie_env
source testgenie_env/bin/activate  # or .\testgenie_env\Scripts\activate on Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Add your OpenAI key to `.env`
OPENAI_API_KEY=your_key_here

# 5. Run the app
streamlit run app.py





