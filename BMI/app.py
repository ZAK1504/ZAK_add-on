from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    bmi = None
    category = None
    error = None
    height_input = ''
    weight_input = ''
    
    if request.method == 'POST':
        try:
            # Get form data
            height_input = request.form.get('height', '')
            weight_input = request.form.get('weight', '')
            
            # Convert to float
            height = float(height_input)
            weight = float(weight_input)
            
            # Validate input
            if height <= 0 or weight <= 0:
                error = "Height and weight must be positive numbers."
            elif height > 300 or weight > 500:
                error = "Please enter realistic values."
            else:
                # Calculate BMI
                height_in_meters = height / 100
                bmi = weight / (height_in_meters ** 2)
                bmi = round(bmi, 2)
                
                # Determine category
                if bmi < 18.5:
                    category = "Underweight"
                elif 18.5 <= bmi < 25:
                    category = "Normal"
                elif 25 <= bmi < 30:
                    category = "Overweight"
                else:
                    category = "Obese"
                    
        except ValueError:
            error = "Please enter valid numbers for height and weight."
        except Exception as e:
            error = f"An error occurred: {str(e)}"
    
    return render_template('index.html', 
                         bmi=bmi, 
                         category=category, 
                         error=error,
                         height_input=height_input,
                         weight_input=weight_input)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

# ============================================
# HOW TO RUN ON LINUX:
# ============================================
# Method 1 (Using Flask CLI):
#   export FLASK_APP=app.py
#   flask run
#
# Method 2 (Direct execution):
#   python3 app.py
#
# Then open your browser and go to:
#   http://localhost:5000
# ============================================
