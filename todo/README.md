# To-Do List App

A clean, professional, full-stack web application built with Flask that helps you manage your daily tasks efficiently. Add, view, and delete tasks with a beautiful, responsive interface.

## 📋 Overview

This To-Do List application provides a simple yet powerful way to organize your tasks. Built with Python Flask on the backend and modern HTML/CSS on the frontend, it offers a smooth user experience with instant updates.

## 🚀 Features

- ✅ **Add Tasks**: Quickly add new tasks with a single input field
- ✅ **View Tasks**: See all your tasks in a clean, numbered list
- ✅ **Delete Tasks**: Remove completed tasks with one click
- ✅ **Clear All**: Remove all tasks at once
- ✅ **Task Counter**: See how many tasks you have at a glance
- ✅ **Unique IDs**: Each task has a UUID for reliable deletion
- ✅ **Responsive Design**: Works perfectly on mobile, tablet, and desktop
- ✅ **Modern UI**: Beautiful gradient background with smooth animations
- ✅ **Empty State**: Friendly message when no tasks exist
- ✅ **Scrollable List**: Handle large task lists elegantly
- ✅ **ZAK Branding**: Logo in top-left corner

## 📁 Project Structure

```
todo_app/
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
cd todo_app
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

The app runs on `0.0.0.0:5000` by default, accessible at:
- Local: http://localhost:5000
- Network: http://YOUR_IP:5000

## 💻 Usage

### Adding a Task

1. Open http://localhost:5000 in your browser
2. Type your task in the input field (e.g., "Buy groceries")
3. Click the green "Add Task" button
4. Your task appears instantly in the list below

### Deleting a Task

1. Find the task you want to remove
2. Click the red "✕" button next to it
3. The task is immediately removed from the list

### Clearing All Tasks

1. Click the "Clear All" button at the top-right of the task list
2. Confirm the action
3. All tasks are removed at once

## 🎨 Design Features

### Visual Design
- **Purple Gradient Background**: Professional gradient from purple to violet
- **Card-based Layout**: Centered white card with shadow effects
- **ZAK Logo**: Branded logo in top-left corner
- **Responsive Grid**: Adapts to all screen sizes

### Interactive Elements
- **Green Add Button**: Color-coded for positive action
- **Red Delete Buttons**: Clear visual indicator for removal
- **Hover Effects**: Smooth transitions on all interactive elements
- **Numbered Tasks**: Each task displays its position in the list
- **Color-coded Borders**: Tasks have a purple left border accent

### Animations
- **Slide-in**: Card smoothly appears on page load
- **Fade-in**: New tasks fade into the list
- **Hover Transform**: Tasks and buttons respond to mouse hover
- **Smooth Transitions**: All state changes are animated

## 🔧 Technical Details

### Backend (Flask)
- **Routes**:
  - `GET /` - Display main page with all tasks
  - `POST /add` - Add a new task
  - `POST /delete/<task_id>` - Delete a specific task
  - `POST /clear` - Clear all tasks

- **Data Storage**: Tasks stored in-memory using Python list
- **Task Structure**: Each task is a dictionary with `id` and `description`
- **UUID**: Uses Python's `uuid` module for unique task IDs

### Frontend (HTML/Jinja2)
- **Template Engine**: Jinja2 for dynamic rendering
- **Forms**: POST forms for add, delete, and clear actions
- **Loops**: Jinja2 `for` loop to display all tasks
- **Conditionals**: Show/hide elements based on task count
- **Semantic HTML**: Proper HTML5 structure

### Styling (CSS)
- **Flexbox**: Modern layout system
- **Custom Scrollbar**: Styled scrollbar for task list
- **Media Queries**: Responsive breakpoints for mobile and tablet
- **CSS Variables**: (Can be added for easy theming)
- **Animations**: @keyframes for smooth effects

## 📱 Mobile Responsive

The application automatically adjusts for different screen sizes:

- **Smartphones (< 600px)**:
  - Stacked layout
  - Full-width buttons
  - Smaller logo and fonts
  - Touch-friendly button sizes

- **Tablets (600px - 900px)**:
  - Medium container width
  - Optimized spacing

- **Desktops (> 900px)**:
  - Maximum 600px container width
  - Side-by-side input and button
  - Larger fonts and spacing

## 🌐 Browser Compatibility

Tested and working on:
- Chrome/Edge (Chromium)
- Firefox
- Safari
- Opera
- Mobile browsers (iOS Safari, Chrome Mobile)

## 🐧 Linux Deployment

### Development Mode

```bash
python3 app.py
```

### Production Mode

For production deployment with better performance:

```bash
# Install gunicorn
pip3 install gunicorn

# Run with gunicorn (4 worker processes)
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

### Running as a Service

Create a systemd service file for automatic startup on Linux:

```bash
sudo nano /etc/systemd/system/todo-app.service
```

## 🔒 Data Persistence

**Note**: The current version stores tasks in memory, which means:
- ✅ Fast and simple
- ⚠️ Tasks are lost when the server restarts

### Optional Enhancements:

1. **File Storage**: Save tasks to a JSON or text file
2. **Database**: Use SQLite, PostgreSQL, or MongoDB
3. **Session Storage**: Store per-user tasks in Flask sessions

## 🛡️ Features & Validation

- ✅ Required field validation
- ✅ Empty string protection (strips whitespace)
- ✅ Unique UUID for each task
- ✅ Confirmation dialog for "Clear All"
- ✅ Graceful empty state handling

## 👨‍💻 Technology Stack

- **Backend**: Python 3 + Flask
- **Frontend**: HTML5 + CSS3 + Jinja2
- **Task IDs**: UUID (universally unique identifier)
- **Server**: Flask Development Server (debug mode)
- **Styling**: Custom CSS with Flexbox

## 📝 Example Workflow

```
1. User visits http://localhost:5000
2. Page displays "No tasks yet!" message
3. User types "Buy groceries" and clicks "Add Task"
4. Task #1 appears: "Buy groceries" with a delete button
5. User adds more tasks: "Call dentist", "Finish report"
6. Task list shows: 3 tasks numbered 1, 2, 3
7. User clicks delete on "Call dentist"
8. Task is removed, list updates to show 2 tasks
9. User clicks "Clear All"
10. Confirmation prompt appears
11. All tasks cleared, empty state returns
```

## 🎯 Future Enhancements

Potential features to add:
- [ ] Edit existing tasks
- [ ] Mark tasks as complete (with strikethrough)
- [ ] Task priorities (high, medium, low)
- [ ] Due dates and reminders
- [ ] Categories/tags for tasks
- [ ] Search and filter functionality
- [ ] User authentication
- [ ] Cloud synchronization
- [ ] Dark mode toggle

## 📧 Support

For issues or questions:
1. Ensure Flask is properly installed: `pip3 list | grep Flask`
2. Check that port 5000 is not in use: `lsof -i :5000`
3. Verify all files are in correct directories
4. Check Python version: `python3 --version`

## 📄 License

This project is open-source and available for educational and personal use.

## 🤝 Contributing

Feel free to fork, modify, and enhance this project!

---

**Made with ❤️ using Flask**

Stay organized and productive! ✅📝🚀
