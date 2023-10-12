import cv2
import numpy as np
from keras.models import load_model
from keras.preprocessing import image
from PIL import Image
import csv

# Load the trained model
model = load_model("cnn_ep5.h5")

# Replace with your model's input dimensions
image_width = 128
image_height = 128

class_names = ['21BCS064', '21bcs019', '21bcs020', '21bcs028', '21bcs032', '21bcs035', '21bcs041', '21bcs057', '21bcs058', '21bcs061', '21bcs063']  # Replace with your actual class names

# Initialize the webcam
cap = cv2.VideoCapture(0)

# Load the existing classes from the CSV file into a set
existing_classes = set()
with open('attendance.csv', mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        if len(row) > 1:  # Skip empty rows
            existing_classes.add(row[1])  # Assuming the class name is in the second column

# Capture live frames
while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Preprocess the frame
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame_pil = Image.fromarray(frame)
    frame_pil = frame_pil.resize((image_width, image_height))
    frame_array = np.array(frame_pil)
    frame_array = np.expand_dims(frame_array, axis=0)

    # Perform prediction
    prediction = model.predict(frame_array)
    predicted_class_index = np.argmax(prediction)
    predicted_class_name = class_names[predicted_class_index]

    # Display the frame with predicted class
    cv2.putText(frame, predicted_class_name, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow('Live Attendance', frame)

    # Write data to CSV if the student is not already in the existing_classes set
    if predicted_class_name not in existing_classes:
        with open('attendance.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([predicted_class_name])
        existing_classes.add(predicted_class_name)

    # Exit when 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all windows
cap.release()
cv2.destroyAllWindows()
