from mega import Mega

# Initialize the Mega instance
mega = Mega()

# Login using your MEGA account
email = ""  # Replace with your email
password = ""           # Replace with your password
m = mega.login(email, password)

# Upload the file
file_path = ''  # Path to video
file = m.upload(file_path)

# Get and print the upload link
file_link = m.get_upload_link(file)
print(f'File uploaded successfully! You can access it at: {file_link}')
