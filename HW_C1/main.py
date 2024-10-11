from fastapi import FastAPI, HTTPException, Depends
from typing import List
from pydantic import BaseModel
from passlib.context import CryptContext
import jwt

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
fake_db = {"users": {}}

app = FastAPI()


class Payload(BaseModel):
    numbers: List[int]


class BinarySearchPayload(BaseModel):
    numbers: List[int]
    target: int


class User(BaseModel):
    username: str
    password: str


def verify_token(token: str = Depends()):
    try:
        payload = jwt.decode(token, "secret_key", algorithms=["HS256"])
        username = payload.get("username")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        return username
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Invalid token")


@app.post("/bubble-sort")
def bubble_sort(payload: Payload, token: str):
    verify_token(token)
    numbers = payload.numbers
    n = len(numbers)
    for i in range(n):
        for j in range(0, n - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return {"numbers": numbers}

           
@app.post("/filter-even")
def filter_even(payload: Payload, token: str):
    verify_token(token)
    numbers = payload.numbers
    even_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
    return {"even_numbers": even_numbers}


@app.post("/sum-elements")
def sum_elements(payload: Payload, token: str):
    verify_token(token)
    numbers = payload.numbers
    sum = 0
    for number in numbers:
        sum += number
    return {"sum": sum}


@app.post("/max-value")
def max_value(payload: Payload, token: str):
    verify_token(token)
    numbers = payload.numbers
    max = numbers[0]
    for number in numbers:
        if number > max:
            max = number
    return {"max": max}


@app.post("/binary-search")
def binary_search(payload: BinarySearchPayload, token: str):
    verify_token(token)
    numbers = payload.numbers
    target = payload.target
    low = 0
    high = len(numbers) - 1
    while low <= high:
        mid = (low + high) // 2
        if numbers[mid] == target:
            return {"found": True, "index": mid}
        elif numbers[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return {"found": False, "index": -1}

@app.post("/register")
def register(user: User):
    if user.username in fake_db["users"]:
        raise HTTPException(status_code=400, detail="User already exists")
    hashed_password = pwd_context.hash(user.password)
    fake_db["users"][user.username] = hashed_password
    return {"message": "User registered successfully"}

@app.post("/login")
def login(user: User):
    if user.username not in fake_db["users"]:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    if not pwd_context.verify(user.password, fake_db["users"][user.username]):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    access_token = jwt.encode({"username": user.username}, "secret_key", algorithm="HS256")
    return {"access_token": access_token}
