from flask import Flask, render_template, request, redirect, url_for
import uuid

app = Flask(__name__)


# Store tasks in memory (list of dictionaries)
# Each task has an ID, description, and completed status
tasks = []


@app.route('/')
def index():
    """
    Display the main page with all tasks and counters
    """
    total_tasks = len(tasks)
    completed_tasks = sum(1 for t in tasks if t.get('completed'))
    return render_template('index.html', tasks=tasks, total_tasks=total_tasks, completed_tasks=completed_tasks)


@app.route('/add', methods=['POST'])
def add_task():
    """
    Add a new task to the list
    """
    task_description = request.form.get('task', '').strip()
    # Validate input
    if task_description:
        # Create new task with unique ID and completed status
        new_task = {
            'id': str(uuid.uuid4()),
            'description': task_description,
            'completed': False
        }
        tasks.append(new_task)
    return redirect(url_for('index'))


@app.route('/delete/<task_id>', methods=['POST'])
def delete_task(task_id):
    """
    Delete a task by its unique ID
    """
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    return redirect(url_for('index'))
@app.route('/toggle/<task_id>', methods=['POST'])
def toggle_task(task_id):
    """
    Toggle the completed status of a task
    """
    for task in tasks:
        if task['id'] == task_id:
            task['completed'] = not task.get('completed', False)
            break
    return redirect(url_for('index'))

@app.route('/clear', methods=['POST'])
def clear_all():
    """
    Clear all tasks
    """
    global tasks
    tasks = []
    
    return redirect(url_for('index'))

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
