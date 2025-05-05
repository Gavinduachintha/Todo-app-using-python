from supabase import create_client, client
from dotenv import load_dotenv
import os

load_dotenv()
url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)

current_user = None

def sign_in():
    global current_user
    # try:
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    response = supabase.auth.sign_in_with_password(
    {
        "email": email, 
        "password": password,
    }
)
    # except AuthApiError as e:
    #     print("Authentication error", e.message)
    # if response.user:
    #     current_user = {"id":response.user.id,"email":response.user.email}
    #     print(f"Signed in as: {current_user}")
    # else:
    #     print(f"Signed in failed: {response.error.meassage}")
    # if "user" in response:
    #     global current_user
    #     current_user = response["user"]
    #     print(f"Sign in successfull. User ID: {current_user}")
    # else:
    #     print(f"Sign in failed: {response.get('error','Unknown error')}")
        return current_user
    else:
        return None

def sign_up():
    global current_user
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    response = supabase.auth.sign_up(
    {
        "email": email, 
        "password": password,
    }
)
    if response.user:
        print(f"Sign up successfull. User ID: {response.user.id}")
        return current_user
    else:
        print(f"Sign up failed: {response.error.message if response.error else 'unkown error'}")
        return None
    
