# Promptulate running on Vercel

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2FUndertone0809%2Fvercel-promptulate-flask&env=OPENAI_API_KEY&envDescription=API%20Key%20for%20OpenAI&project-name=promptulate-flask&repository-name=vercel-promptulate-flask)

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
GET http://localhost:3000/api/hello
```

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`OPENAI_API_KEY`

## One-Click Deploy

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2FUndertone0809%2Fvercel-promptulate-flask&env=OPENAI_API_KEY&envDescription=API%20Key%20for%20OpenAI&project-name=promptulate-flask&repository-name=vercel-promptulate-flask)

## Further Reading

Learn more about how to use LangChain by visiting the official documentation or repo:

- https://github.com/Undertone0809/promptulate

- https://undertone0809.github.io/promptulate/#/