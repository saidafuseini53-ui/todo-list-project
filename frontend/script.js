const todoListElement = document.getElementById("todo-list");

fetch("http://127.0.0.1:8000/todos")
    .then((response) => response.json())
    .then((todos) => {
        todos.forEach((todo) => {
            const todoElement = document.createElement("div");
            todoElement.className = "todo-item";

            if (todo.completed) {
                todoElement.classList.add("completed");
            }

            const titleElement = document.createElement("h2");
            titleElement.textContent = todo.title;

            const descriptionElement = document.createElement("p");
            descriptionElement.textContent = todo.description;

            const statusElement = document.createElement("p");
            statusElement.textContent = todo.completed
                ? "Status: Completed"
                : "Status: Incomplete";

            todoElement.appendChild(titleElement);
            todoElement.appendChild(descriptionElement);
            todoElement.appendChild(statusElement);

            todoListElement.appendChild(todoElement);
        });
    });