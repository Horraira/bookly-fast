from fastapi import FastAPI
from src.basics.routes import router as basics_router
from src.books.routes import book_router
from contextlib import asynccontextmanager
from src.db.main import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup actions can be added here
    print("Starting up...")
    await init_db()
    yield
    # Shutdown actions can be added here
    print("Shutting down...")


version = "v1"

app = FastAPI(
    title="Bookly API",
    description="An API to manage a collection of books.",
    version=version,
    lifespan=lifespan,
)

app.include_router(basics_router, prefix="", tags=["basics"])
app.include_router(book_router, prefix=f"/api/{version}/books", tags=["books"])
