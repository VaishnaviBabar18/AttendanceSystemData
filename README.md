# 🎓 Face Recognition Attendance System
A real-time, AI-powered attendance system using face recognition with a Streamlit dashboard.

## Project Structure

This project includes three main components:
1. **`add_faces.py`**  
   → Captures and stores face data using OpenCV for training the model.
2. **`test.py`**  
   → Recognizes faces in real-time using KNN and marks attendance in a CSV file.  
   → Features voice feedback using `pywin32`.
3. **`app.py`**  
   → Streamlit app to display the latest attendance records dynamically.  
   → Includes a FizzBuzz counter with autorefresh functionality.

## Features
- Real-time face detection using OpenCV
- KNN classifier for face recognition
- Voice feedback for attendance confirmation
- CSV-based attendance logging with timestamp
- Interactive Streamlit dashboard for live attendance monitoring
- Auto-refresh with FizzBuzz counter for demo/test purposes
  
## Tech Stack
- Python
- OpenCV
- scikit-learn (KNN)
- Streamlit
- pywin32 (for voice feedback on Windows)
- Pandas, NumPy

## How to Run
### 1. Install Dependencies
pip install -r requirements.txt

**###2.To Run App.py use the command**
-  streamlit run app.py
  ###3 To run Add_faces.py use the command**
- Python add_faces.py
**###4. To run test,py use the command**
- python test.py
  

