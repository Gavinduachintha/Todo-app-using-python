# 📝 Supabase ToDo CLI App

A simple and secure command-line ToDo application built with **Python** and **Supabase**. Manage your tasks with ease from the terminal, and log in securely using Supabase's authentication.

## 🚀 Features

- 🔐 User sign-up and sign-in
- ➕ Add new tasks
- ✅ Mark tasks as completed
- 📝 Update task description or status
- 🗑️ Delete tasks by ID
- 👀 View all tasks for the authenticated user

## 📦 Technologies Used

- 🐍 Python
- 🧱 Supabase (PostgreSQL + Auth)
- 🔐 `python-dotenv`

## 📁 Project Structure
- ├── main.py # Main CLI task manager
- ├── auth.py # User authentication (sign up / sign in)
- ├── .env # Environment variables
- ├── requirements.txt
- └── README.md


## 🔑 Supabase Authentication
Users must **sign up or sign in** before managing their tasks. The `auth.py` script handles:
- Email-based sign-up
- Email/password sign-in
- Session-based authorization

### ✨ Auth Flow
1. On app start, users run `auth.py` to sign up or sign in.
2. On successful login, a **session access token** is retrieved.
3. This token is used to **filter tasks per user** (e.g., using `user_id` in the `Todo` table).

---

## 🛠️ Setup Instructions
1. **Clone the repository**
   ```bash
   git clone https://github.com/Gavinduachintha/Todo-app-using-python.git
   Todo-app-using-python
   
2. **Install dependencies**
pip install supabase

3. **Create a .env file**
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_anon_or_service_role_key

4. **Run the Main App**
python main.py

🗃️ Supabase Table Schema
- Todo Table
- Column	Type	Description
- id	Integer	Primary key (auto-increment)
- to_do	Text	Task description
- completed	Boolean	Task status (True/False)
- user_id	UUID	Linked to auth.users.id (foreign)

❤️ Acknowledgements
- Supabase
- Python Dotenv
