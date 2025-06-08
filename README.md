# 📟 TI-89 Inspired Graphing Calculator (Web App)

This is a fully functional, Flask-powered graphing calculator inspired by the TI-89. It supports trigonometric functions, graphing, and scientific operations with a colorful, intuitive interface.

---

## 🔗 Live Demo

**[Try it here on Render](https://basic-graphing-calculator.onrender.com)**

---

## ✨ Features

* ✅ Scientific operations: `sin`, `cos`, `tan`, `asin`, `acos`, `atan`
* ✅ Constants like `π`, factorial `!`, square root `√`, and exponentiation
* ✅ Expression parsing with parentheses
* ✅ Basic graphing (e.g., `sin(x)`, `x**2`, `ln(x)`) using `Matplotlib`
* ✅ Degree/Radian toggle
* ✅ Keyboard-style layout modeled after TI-89
* ✅ Responsive UI with colorful button schemes

---

## 🛠 Technologies Used

* Python 3
* Flask
* HTML5 / CSS3 / JavaScript
* Matplotlib (for graphing)
* Hosted via Render

---

## 🧪 How It Works

* Frontend sends expressions to the backend via a form
* Flask safely evaluates input using restricted namespaces (no arbitrary code execution)
* Graphing uses NumPy arrays over a defined `x` range and renders plots with Matplotlib
* Templating via Jinja2 inside the `/templates` folder

---

## 🚀 Setup Instructions (Local)

```bash
# Clone the repo
$ git clone https://github.com/mmontalvo9/Calculator.git
$ cd Calculator

# Create virtual environment (optional)
$ python -m venv venv
$ source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
$ pip install -r requirements.txt

# Run it
$ python main.py

# Visit
Go to http://127.0.0.1:5000 in your browser
```

---

## 📁 Folder Structure

```
Calculator/
├── static/              # CSS and images
├── templates/           # index.html, graph.html
├── main.py              # Flask app backend
├── requirements.txt     # Python dependencies
```

---

## 🤝 Contributing

Pull requests are welcome! Feel free to fork the project and suggest improvements.

---

## 📜 License

MIT License

---

## 📬 Contact

Created by **Marc Sebastian Montalvo** — feel free to reach out on GitHub or LinkedIn.

---

> "Looks like a TI-89. Runs like Python. Feels like yours."
