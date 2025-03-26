# **PPE Detection Using YOLO & Webcam 🎥🔍**  

This project uses **YOLO (You Only Look Once)** to detect Personal Protective Equipment (**PPE**) in real time using a webcam. It is implemented in Python with **OpenCV** and **Ultralytics YOLO**.  

---

## **📁 Project Structure**  

```
PPE_Detection/
│── models/                  # Directory for storing the trained model
│   ├── best.pt              # Trained YOLO model
│── src/                     # Source code directory
│   ├── detect_ppe.py        # Main script to detect PPE using webcam
│   ├── utils.py             # Helper functions
│── colab_Notebook/          # Training notebook from Google Colab
│── requirements.txt         # Dependencies
│── README.md                # Project documentation
│── .gitignore               # Ignore unnecessary files
│── LICENSE                  # License file
```

---

## **🚀 Setup & Installation**  

### **1️⃣ Create a Virtual Environment (Recommended)**  
```bash
python -m venv vEnv
source vEnv/bin/activate    # On macOS/Linux
vEnv\Scripts\activate       # On Windows
```

### **2️⃣ Install Dependencies**  
```bash
pip install -r requirements.txt
```

### **3️⃣ Download & Place the Model**  
Ensure the trained **YOLO model (`best.pt`)** is inside the `models/` directory.

---

## **🎯 Running the PPE Detection Script**  
Run the script to detect PPE using your system’s webcam:  
```bash
python src/detect_ppe.py
```

- **Press 'Q'** to exit the webcam feed.

---

## **🛠 Troubleshooting**  

### **1. Model Not Found Error**  
```
FileNotFoundError: [Errno 2] No such file or directory: 'models/best.pt'
```
✅ **Fix:** Ensure `best.pt` exists in `models/` and use the absolute path in `detect_ppe.py` if needed.

### **2. Webcam Not Opening**  
```
cv2.error: (-215:Assertion failed) in function 'cv::VideoCapture'
```
✅ **Fix:** Try changing the webcam index in `cv2.VideoCapture(0) → cv2.VideoCapture(1)`

### **3. CUDA Not Available**  
```
CUDA not available, running on CPU.
```
✅ **Fix:** If running on CPU, ignore this message. If you have a GPU, install CUDA-enabled PyTorch:
```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

---

## **📜 License**  
This project is open-source and licensed under the **MIT License**.
