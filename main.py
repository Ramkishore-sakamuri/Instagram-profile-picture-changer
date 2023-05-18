import requests
import time

# Get your Instagram username and password
username = "your_username"
password = "your_password"

# Create a function to change your profile picture
def change_profile_picture(image_url):
    # Make a request to the Instagram API to change your profile picture
    response = requests.post("https://api.instagram.com/v1/users/self/profile_picture",
                              data={"url": image_url},
                              auth=(username, password))

    # Check if the request was successful
    if response.status_code == 200:
        print("Profile picture changed successfully!")
    else:
        print("Error changing profile picture:", response.status_code)

# Create a list of image URLs
image_urls = [
    "https://blogger.googleusercontent.com/img/a/AVvXsEhI9szDaFBSqU72WWihPHq5X9S0Iz_FBySvh3UQkodknzDxwFogHect_3wLpSlU2XM0_0Li3CudMgz3e2eyknrJBbGKQjhYixV5De9opPtboQrpyMWcekZwLtZ8lGfMcioF8bwO6DMoFglXraNyCcLzPepWU6M43KCyMMLY40KcodrYvWPpV6n1rLhM=s500",
]

# Loop forever, changing your profile picture every time someone refreshes
while True:
    # Get a random image URL from the list
    image_url = image_urls[random.randint(0, len(image_urls) - 1)]

    # Change your profile picture
    change_profile_picture(image_url)

    # Wait for 5 seconds before changing your profile picture again
    time.sleep(5)
