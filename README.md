# Introduction 

# Getting Started
[ ] copy paste the .env.sample file to .env file and update the variables as per your project.
[ ] update the docker-compose.prod.yml for production release, add volumes of required.
[ ] run docker-compose.prod.yml using docker compose command or similar for checking project is ready for production.
[ ] while doing the development run the docker-compose,yml which runs postgres and rabitmq only.
[ ] if you want to add new entity, then create entity in app/entity folder and then import it in __init__.py, then run `alembic revision --autogenerate -m "Added account table"` for generating the create or update table script automatically.
[ ] check and verify auto generated tables scripts in migration folder. if required modify the generated script.
[ ] to generate the required tables run `alembic upgrade head` before starting the application in development.
[ ] you can use the vscode debugger for running the debugging the project while development.
[ ] add your background task to app/background tasks folder and import it in last line of the app/dramatiq file.
[ ] send that method just in example bg url from the routes
[ ] add any new route to routes folder and don't forget to import it in route entries section
