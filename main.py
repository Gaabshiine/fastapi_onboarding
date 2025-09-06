from fastapi import FastAPI


app = FastAPI()

# Test
@app.get("/test")
def test():
    return {
        "message": "The API is working probably"
    }


# Create todo
@app.post("/")
def create_todo():
    return { "msg": "This is creating requests" }

# Read all todo list
@app.get("/")
def get_all_todos():
    return { "msg": "all requests" }

# Read specific todo by id 
@app.get("/{todo_id}")
def get_todo_by_id(todo_id: int):
    return { "msg": f"Getting specific request by id -> {todo_id}" }

# Update todo by id 
@app.put("/{todo_id}")
def update_todo_by_id(todo_id: int):
    return { "msg": f"Updating request by id -> {todo_id}" }

# Delete todo by id
@app.delete("/{todo_id}")
def delete_todo_by_id(todo_id: int):
    return { "msg": f"Deleting request by id -> {todo_id}" }