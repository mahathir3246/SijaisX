# SijaisX


To activate .venv in Linux terminal(make sure you are in the root folder or wherever the venv is)

    - source .venv/bin/activate

To create a database(if not already created(it should be already there) and make sure you are in the root folder to run this command)

    - python3 -m backend.src.database_create

To create test data(if not existing alreadymake sure you are in the root folder to run this command)

    - python3 -m backend.src.test_data

To activate the backend server

    - python3 -m backend.src.api_calls

To activate the frontend server

    - pnpm install(to install all the libraries and dependencies)
    - pnpm dev