    except Exception as e:
        error_message = str(e)
        if "Invalid login credentials" in error_message:
            print("Wrong email or password.")
        else:
            print("Something went wrong:", error_message)