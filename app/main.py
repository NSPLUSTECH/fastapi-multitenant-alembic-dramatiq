from app.dramatiq import set_host
set_host()
from fastapi import FastAPI
from app.routes import setup_routes
from app.utils.life_cycle_handler import lifespan
from app.utils.middlewares import setup_middlewares
app = FastAPI(lifespan=lifespan)
setup_routes(app)
setup_middlewares(app)
