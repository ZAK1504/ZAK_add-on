# BMI Calculator

A professional, full-stack web application built with Flask that calculates Body Mass Index (BMI) and categorizes health status based on user input.

## 📋 Overview

This BMI Calculator accepts height (in cm) and weight (in kg) from users and calculates their Body Mass Index using the standard formula. The application provides instant feedback with color-coded categories to help users understand their health status.

### BMI Formula

```
BMI = weight (kg) / (height (m))²
```

### BMI Categories

- **Underweight**: BMI < 18.5 (Light Blue)
- **Normal**: BMI 18.5 - 24.9 (Green)
- **Overweight**: BMI 25 - 29.9 (Orange)
- **Obese**: BMI ≥ 30 (Red)

## 🚀 Features

- ✅ Clean, modern, and responsive user interface
- ✅ Real-time BMI calculation
- ✅ Color-coded health categories
- ✅ Input validation and error handling
- ✅ Mobile-friendly design
- ✅ Professional gradient styling with animations
- ✅ Clear visual feedback for all BMI ranges

## 📁 Project Structure

```
bmi_calculator/
├── app.py                  # Flask backend application
├── templates/
│   └── index.html         # Frontend HTML template
├── static/
│   └── style.css          # CSS styling
└── README.md              # This file
```

## 🛠️ Installation & Setup

### Prerequisites

- Python 3.6 or higher
- pip (Python package manager)

### Step 1: Install Flask

```bash
pip install flask
```

Or if using pip3:

```bash
pip3 install flask
```

### Step 2: Navigate to Project Directory

```bash
cd bmi_calculator
```

## ▶️ Running the Application

### Method 1: Using Flask CLI

```bash
export FLASK_APP=app.py
flask run
```

### Method 2: Direct Python Execution (Recommended)

```bash
python3 app.py
```

Or simply:

```bash
python app.py
```

### Method 3: Custom Host/Port

```bash
python3 app.py
```

The app runs on `0.0.0.0:5000` by default, accessible at:
- Local: http://localhost:5000
- Network: http://YOUR_IP:5000

## 💻 Usage

1. Open your web browser and navigate to `http://localhost:5000`
2. Enter your height in centimeters (e.g., 170)
3. Enter your weight in kilograms (e.g., 65)
4. Click the "Calculate BMI" button
5. View your BMI value and category with color-coded results

### Example

**Input:**
- Height: 170 cm
- Weight: 65 kg

**Output:**
- Your BMI is: **22.49**
- Category: **Normal** (Green)

## 🎨 Design Features

- **Gradient Background**: Purple gradient for modern aesthetics
- **Card-based Layout**: Centered card with shadow effects
- **Responsive Design**: Works perfectly on mobile, tablet, and desktop
- **Smooth Animations**: Slide-in and fade effects
- **Interactive Elements**: Hover effects on buttons and inputs
- **Color-coded Results**: Visual feedback based on BMI category

## 🔒 Input Validation

The application includes comprehensive error handling:

- ✅ Validates numeric input
- ✅ Ensures positive values
- ✅ Checks for realistic ranges (height < 300cm, weight < 500kg)
- ✅ Provides clear error messages
- ✅ Graceful exception handling

## 🌐 Browser Compatibility

Works on all modern browsers:
- Chrome
- Firefox
- Safari
- Edge
- Opera

## 📱 Mobile Responsive

The application automatically adjusts for:
- Smartphones (< 600px)
- Tablets (600px - 900px)
- Desktops (> 900px)

## 🐧 Linux Deployment

### Development Mode

```bash
python3 app.py
```

### Production Mode

For production deployment, consider using:

```bash
# Install gunicorn
pip3 install gunicorn

# Run with gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

## 🛡️ Error Handling

The application handles various error scenarios:

- Invalid input (non-numeric values)
- Negative or zero values
- Unrealistic measurements
- Form submission errors
- Server-side exceptions

## 👨‍💻 Technical Stack

- **Backend**: Python 3 + Flask
- **Frontend**: HTML5 + CSS3 + Jinja2 Templates
- **Styling**: Custom CSS with Flexbox and Grid
- **Server**: Flask Development Server (Debug mode)

## 📝 License

This project is open-source and available for educational purposes.

## 🤝 Contributing

Feel free to fork, modify, and use this project for learning or personal use.

## 📧 Support

For issues or questions, please check:
1. All files are in the correct directory structure
2. Flask is properly installed
3. Port 5000 is not in use by another application

---

**Made with ❤️ using Flask**

Enjoy calculating your BMI! 🏃‍♂️💪
