import uvicorn

if __name__ == "__main__":
    uvicorn.run("testapi:app", host='0.0.0.0', port=420, reload=True)