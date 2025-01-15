// Task Management App

// Task Class
class Task {
    constructor(title, description, dueDate) {
        this.id = Date.now(); // Unique ID based on timestamp
        this.title = title;
        this.description = description;
        this.dueDate = dueDate;
        this.isCompleted = false;
    }

    toggleComplete() {
        this.isCompleted = !this.isCompleted;
    }
}

// Task Manager Class
class TaskManager {
    constructor() {
        this.tasks = [];
    }

    addTask(task) {
        this.tasks.push(task);
    }

    deleteTask(id) {
        this.tasks = this.tasks.filter(task => task.id !== id);
    }

    getTasks() {
        return this.tasks;
    }
}

// DOM Elements
const taskForm = document.querySelector('#taskForm');
const taskList = document.querySelector('#taskList');

// Task Manager Instance
const taskManager = new TaskManager();

// Helper Functions
const createTaskHTML = (task) => `
    <div class="task ${task.isCompleted ? 'completed' : ''}" data-id="${task.id}">
        <h3>${task.title}</h3>
        <p>${task.description}</p>
        <p><strong>Due:</strong> ${task.dueDate}</p>
        <button class="toggle-btn">${task.isCompleted ? 'Mark Incomplete' : 'Mark Complete'}</button>
        <button class="delete-btn">Delete</button>
    </div>
`;

const renderTasks = () => {
    taskList.innerHTML = '';
    taskManager.getTasks().forEach(task => {
        taskList.innerHTML += createTaskHTML(task);
    });
};

// Event Listeners
taskForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const title = document.querySelector('#taskTitle').value;
    const description = document.querySelector('#taskDescription').value;
    const dueDate = document.querySelector('#taskDueDate').value;

    if (title && dueDate) {
        const newTask = new Task(title, description, dueDate);
        taskManager.addTask(newTask);
        renderTasks();
        taskForm.reset();
    } else {
        alert('Title and Due Date are required!');
    }
});

taskList.addEventListener('click', (e) => {
    const parentTask = e.target.closest('.task');
    if (!parentTask) return;

    const taskId = parseInt(parentTask.dataset.id);

    if (e.target.classList.contains('toggle-btn')) {
        const task = taskManager.getTasks().find(t => t.id === taskId);
        if (task) task.toggleComplete();
        renderTasks();
    }

    if (e.target.classList.contains('delete-btn')) {
        taskManager.deleteTask(taskId);
        renderTasks();
    }
});

// Initial Render
renderTasks();
