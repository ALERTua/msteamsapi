## Contributing

#### Fork the `dev` branch of this repository

#### Install both Python 2 and Python 3
#### Set Up Development Environment

For now, Tox and package management is performed using Python 3(!) Poetry, as Python 2 Poetry is too old.

Create Python 2 virtual environment
- `python2 -m pip install virtualenv`
- `python2 -m virtualenv .venv2`

Create Python 3 virtual environment
- `python3 -m pip install virtualenv`
- `python3 -m virtualenv .venv`

Activate Python virtual environments
- Linux: `source .venv/bin/activate`
- Windows `.venv\Scripts\activate`

#### Make your modifications

#### Re-create Poetry Lock File, if you modified the requirements
- `poetry lock`

#### Perform Tests
- Copy `.env.example` to `.env`
- Modify `.env` with your test WebHook, a Teams User Email to mention, and their name.
- Run `poetry run tox`
- You should receive a card for each Python version

#### Install Pre-Commit Hook
- `pre-commit install`

#### Stage Your Changes
- `git add .`

#### Commit Your Changes
- `git commit -m "my changes"`
- The pre-commit hook will tell you if something's wrong

#### Push Your Changes To The Fork

#### Create A Pull Request

Too hard? Contact me via Discord `alertua`
