# Promptulate running on Vercel

A minimal example on how to run Promptulate on Vercel using Flask.

## Installation

#### 1. Virtualenv
Create and activate `virtualenv`.

```bash
virtualenv MY_ENV
source MY_ENV/bin/activate
```

#### 2. Install requirements
```bash
pip install requirements.txt
```

#### 3. Start development server
```bash
vercel dev
```

#### 4. Example API route
```bash
GET http://localhost:3000
```

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`OPENAI_API_KEY`


## Further Reading

Learn more about how to use LangChain by visiting the offical documentation or repo:

- https://github.com/Undertone0809/promptulate

- https://undertone0809.github.io/promptulate/#/