# Image Transformation Tool

Welcome to the **Image Transformation Tool**, a simple yet powerful Python script to manipulate and transform images using the Pillow (PIL) library. Whether you want to resize, rotate, or convert an image to grayscale, this tool has got you covered.

---

## 🌟 Features

- **Resize Images**: Adjust the dimensions of your image effortlessly.
- **Rotate Images**: Rotate your image by any degree (e.g., 90°, 180°, etc.).
- **Grayscale Conversion**: Transform your image into a sleek grayscale version.
- **User-Friendly Input**: Interactive prompts for easy usage.
- **Error Handling**: Handles file-related and unexpected errors gracefully.

---

## 📋 Prerequisites

Before running the script, ensure you have the following installed:

1. **Python 3.7 or later**
2. **Pillow library** (for image processing)

Install Pillow using pip:
```bash
pip install Pillow
```

---

## 🚀 How to Use

1. Clone this repository or download the script:
   ```bash
  
   cd image-transformation-tool
   ```

2. Run the script:
   ```bash
   python transform_image.py
   ```

3. Follow the prompts:
   - Enter the **path** to your input image.
   - Specify the **new dimensions** (width and height) for resizing.
   - Provide a **rotation angle** in degrees (e.g., 90 for a 90° rotation).
   - Specify the **path** to save your transformed image.

4. Voilà! Your transformed image is ready. 🎉

---

## 🛠 Error Handling

- **FileNotFoundError**: Ensures the input file exists at the specified path.
- **UnidentifiedImageError**: Checks if the input file is a valid image.
- **Other Errors**: Any unexpected errors are caught and displayed for debugging.

---

## 📂 Example Workflow

1. Input Path: `images/sample.jpg`
2. New Size: `800 x 600`
3. Rotation Angle: `90`
4. Output Path: `images/output.jpg`

The tool will:
- Load `sample.jpg`.
- Resize it to `800 x 600`.
- Rotate it by 90°.
- Convert it to grayscale.
- Save it as `output.jpg`.



## 🤝 Contributing

We welcome contributions! Feel free to:
- Report issues.
- Suggest new features.
- Submit pull requests.


