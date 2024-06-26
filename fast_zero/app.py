from fastapi import FastAPI

app = FastAPI()


@app.get('/confuso')
def read_root():
    return {'message': 'Olá mundo'}
