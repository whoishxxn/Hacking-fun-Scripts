import os

# Create a file called "evil.txt" and write "I am In" to it
with open("evil.txt", "w") as file:
    file.write("We are Watching You.You Have been Hacked bruh!")

# Open the file using the default text editor
os.system("start evil.txt")