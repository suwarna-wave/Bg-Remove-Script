

# 🖼️ Background Removal Script

Welcome to **Background Removal Script**, your ultimate solution for removing image backgrounds effortlessly! This repository contains a Python script that uses `rembg` and `PIL` to seamlessly remove backgrounds from images. Perfect for developers, designers, and enthusiasts looking to automate image editing!

![Background Removal](https://img.shields.io/badge/Background-Removal-brightgreen) ![Python](https://img.shields.io/badge/Python-3.9-blue) ![Open Source](https://img.shields.io/badge/Open-Source-orange)

## 🎯 Features

- **Fast & Efficient**: Powered by `rembg` for speedy processing.
- **High Quality**: Retains image clarity and detail after background removal.
- **Easy to Use**: Plug and play with minimal configuration required.
- **Customizable**: Modify the script to suit your specific needs.
  
## 🚀 Getting Started

### Prerequisites

Ensure you have the following installed:

- **Python 3.x**
- **PIL** (Python Imaging Library)
- **rembg**

To install the required libraries, use:

```bash
pip install pillow rembg
```

### 💻 Usage

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/suwarna-wave/Bg-Remove-Script.git
   ```
2. **Navigate to the directory:**
   ```bash
   cd Bg-Remove-Script
   ```
3. **Run the Script:**
   ```bash
   python bg_remove_script.py
   ```

### 📁 File Structure

```
Bg-Remove-Script/
├── bg_remove_script.py    # The main script for background removal
├── sample_images/         # Folder to store sample images
└── README.md              # This file
```

###  How It Works

- **Input Image**: Provide the path to the image you want to edit.
- **Background Removal**: The script uses the `rembg` library to identify and remove the background from the image.
- **Output Image**: The processed image is saved to the specified path with the background removed.

### Example:

```python
from rembg import remove
from PIL import Image

# Paths to the image files
input_path = "path/to/your/image.png"
output_path = "path/to/save/edited_image.png"

# Call the function
remove_background(input_path, output_path)
```

## 🌟 Why Choose This Script?

- **Lightning Fast** : Process images in seconds.
- **Simple & Intuitive** : Easy to modify and integrate into your projects.
- **Open Source** : Free to use and contribute!

## 💬 Feedback & Contributions

Contributions, issues, and feature requests are welcome! Feel free to check the social media handle for open issues and contribute.

## 🔥 Like This Project?

Give this repo a ⭐ if you find it useful! Follow me for more amazing projects.

---

📧 **Contact**: For any questions or support, feel free to reach out through my social media handles

Happy coding! ✨
