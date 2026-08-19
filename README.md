# 🧙‍♂️ Blue Invisibility Cloak

### by CyberVishuCodex (Vishal Narkhede)

A fun computer vision project built with **Python** and **OpenCV** that recreates the classic "Harry Potter invisibility cloak" effect using color detection and background substitution — all in real time from your webcam.

![Python](https://img.shields.io/badge/Python-3.7%2B-blue?logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green?logo=opencv&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-Array%20Ops-orange?logo=numpy&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

## 📸 Demo

> Add a screenshot or GIF of the effect in action here once you record one.
> Example placeholder (replace with your own `assets/demo.gif` or `assets/screenshot.png`):



---

## ✨ Features

- 🎥 Real-time webcam-based invisibility effect
- 🔵 Detects **blue-colored** cloth/object using HSV color space
- 🪄 Seamlessly replaces the detected color with a pre-captured background
- 🪞 Mirror-flipped output for a natural, webcam-like view
- 🧹 Noise reduction using morphological operations (Open + Dilate)
- ⚡ Lightweight — no deep learning models required

---

## 🛠️ How It Works

1. **Capture Background** – For the first 3 seconds, the camera captures the empty background (make sure you're out of frame).
2. **Convert to HSV** – Each live frame is converted from BGR to HSV color space, which makes color detection more reliable.
3. **Color Masking** – A blue-colored mask is created using defined HSV ranges.
4. **Mask Cleanup** – Morphological operations remove noise and smooth the mask edges.
5. **Background Substitution** – Pixels matching the blue mask are replaced with the corresponding background pixels; everything else keeps the live frame.
6. **Display Output** – The final composited frame is shown in real time until `q` is pressed.

```
Webcam Frame → HSV Conversion → Blue Mask → Clean Mask
      → Combine (Background + Live Frame) → Invisibility Output
```

---

## 📋 Requirements

- Python 3.7+
- A working webcam
- Good, even lighting (avoid shadows/glare for best detection)
- A **plain blue cloth/object** to use as the "cloak"

### Python Dependencies

| Package | Purpose |
|---|---|
| `opencv-python` | Video capture, image processing, display |
| `numpy` | Array operations & frame manipulation |

---

## ⚙️ Setup & Installation

**1. Clone or download the project**
```bash
git clone https://github.com/your-username/invisibility-cloak.git
cd invisibility-cloak
```

**2. (Optional but recommended) Create a virtual environment**
```bash
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # macOS/Linux
```

**3. Install dependencies**
```bash
pip install opencv-python numpy
```

**4. Run the script**
```bash
python invisibale.py
```

---

## ▶️ Usage

1. Run the script and **step out of the camera frame** for the first 3 seconds — this lets it capture a clean background.
2. Step back in with a **plain blue cloth/object**.
3. Watch the blue-colored areas turn "invisible," revealing the background behind you.
4. Press **`q`** at any time to quit the application.

> 💡 Tip: A solid, matte blue fabric (avoid glossy/shiny material) with no other blue objects in the frame gives the cleanest results.

---

## 🚀 Advantages

- **Beginner-friendly** – A great hands-on project to learn OpenCV fundamentals: color spaces, masking, and bitwise operations.
- **No ML/AI models needed** – Works purely on classical computer vision, so it's lightweight and runs on almost any machine.
- **Real-time performance** – Processes frames live without noticeable lag on standard hardware.
- **Highly customizable** – Easily change `lower_blue`/`upper_blue` values to detect any other color (red, green, etc.).
- **Educational value** – Demonstrates practical use of HSV color space, image masking, and morphological transformations.
- **Fun & shareable** – Great for demos, portfolios, and social media content.

---

## 🔧 Customization Ideas

- Change cloak color by adjusting the HSV range (e.g., for red or green cloth).
- Add a color picker/trackbar UI to fine-tune HSV values live.
- Save the output as a video file using `cv2.VideoWriter`.
- Add multiple background snapshots and let the user switch between them.

---

## ⚠️ Troubleshooting

| Issue | Possible Fix |
|---|---|
| Camera not opening | Check camera index in `cv2.VideoCapture(0)`; try `1` or `2` |
| Cloak not detected properly | Improve lighting, use a more solid/matte blue cloth |
| Flickering mask edges | Increase kernel size or add `cv2.GaussianBlur` before masking |
| Background looks off | Make sure no one is in frame during the first 3 seconds |

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 🙌 Acknowledgements

Inspired by the classic "Harry Potter Invisibility Cloak" OpenCV tutorials used widely for learning computer vision basics.

---

## 👤 Author

**Vishal Narkhede** — *CyberVishuCodex*

[![GitHub](https://img.shields.io/badge/GitHub-vishalnarkhede463--debug-181717?logo=github&logoColor=white)](https://github.com/vishalnarkhede463-debug)
[![Instagram](https://img.shields.io/badge/Instagram-jerry__boy__658-E4405F?logo=instagram&logoColor=white)](https://instagram.com/jerry_boy_658)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Vishal%20Narkhede-0A66C2?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/vishalnarkhede463)



⭐ If you like this project, don't forget to star the repo on GitHub!
