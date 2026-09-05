import os

# Specify the directory path
directory_path = '/WebDev'

contents = os.listdir(directory_path)

#printing contents
for item in contents:
    print(item)