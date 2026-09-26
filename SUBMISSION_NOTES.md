Todo List Application – Submission Notes

1. HTML Elements Identified from the Reference Image

I identified the main elements from the reference image as a header section, a profile area containing an icon and name, the "My Todo List" heading, and individual todo items. Each todo item contains a title, description, and visible completion status.

2. Frontend Challenges and Fixes

One challenge was creating the initial frontend structure before adding CSS. I first built the page using HTML only, then added CSS to improve the layout, spacing, typography, and visual difference between completed and incomplete tasks.

Another challenge was moving the todo data from the HTML into JavaScript. I solved this by creating a JavaScript array and using a loop to dynamically create and display each todo item.

3. Backend Challenges and Fixes

One challenge was setting up the FastAPI backend with SQLite and ensuring that the database was initialized correctly. I created functions for opening the SQLite connection and initializing the database table.

I also tested the "/todos" endpoint using the FastAPI documentation at "/docs" to confirm that the database returned the required todo information.

4. Data Flow

The todo data is stored in the SQLite database. FastAPI connects to the database and retrieves the records through the "/todos" endpoint. The JavaScript frontend sends a GET request to the FastAPI endpoint, receives the data as JSON, and displays the todos in the browser.

SQLite → FastAPI → JavaScript → Browser