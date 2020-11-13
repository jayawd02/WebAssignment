## Architecture:
- When would you prefer to develop an Assignment 1 style web application (Server-side rendering, serving HTML)?
- When would you prefer an Assignment 2 one (REST API & Single Page Application)?

### Version Control:
### What is git and what is it used for?     
    It is a  version controling system and is used for tracking changes. You can use it to track changes to source code while developing software
### List 3 git commands you’ve learned in this course.
    
    git add <filename>  - to add files to the git repository. similar to staging
    
    git commit -m "Commit message"  - to commit files to the git repo
    
    git push origin <branch> - pushing changes to the git repo.
    
### What is GitHub and what is it used for?
    
    It provides hosting for software development and version control using Git.
    It is useful when several developers are working together they can coordinate their work and maintain the code in the same repository.
    
### What is Kanban and what is it used for?
    
    It is a workflow managament method and used as a tool for Agile software development. It has 3 basic principles : Visualizing the tasks and  workflow by using Kanban boards,  Limit the work in progress items, enhance the flow by pulling in work
    
### What is Markdown and what is it used for?
    
    It is a light weight markup language with plain-text-formatting syntax. Used to format files like Readme files. Markdown file has the extent ion or *.md or *. markdown.
    https://en.wikipedia.org/wiki/Markdown

## Platform vs Infrastructure:

### What are some of the pros and cons of using Platform-as-a-Service (PaaS) providers such as Heroku?
*Pros :*
    * Easy to deploy and configure
    * Can scale easily

*Cons :* 
    * Migrations to other platforms maynot be easy or stratight forward
    * Not all features are supported 
    * More costly


### What are some of the pros and cons of using Infrastructure-as-a-Service providers such as Amazon?
*Pros:*
    * cheaper compared to PaaS

*Cons:*
    * Complex to configure and need skills
    * difficult to migrate if proprietary database or cloud vendor specific technology is used

## Web Frameworks:

### What is Django? What are some of its useful features?
    It's a open source web application development framework based on Python. Since it has built in libraries, you can easliy and quickly set up a web application. It follows the model -template-view  architecture. It has admin panel , unit test framework, basic authentication libraries, ORM etc
    https://en.wikipedia.org/wiki/Django_(web_framework)

### What is a model?
    It is the object relational mapping to the database. It is the built-in feature that Django uses to create tables, their fields, and various constraints.

### What is a view?
This controls what is passed to the interface.It is a Python function or class that takes a web request and return a web response. Views are used to do things like fetch objects from the database, modify those objects if needed, render forms, return HTML, and much more

### Name two other popular non-Python web frameworks.
    Ruby on Rails
    React
    https://hotframeworks.com/

### What is WSGI? 
    WSGI (Web server gateway interface) is a  Python standard. It is a specification that describes how a web server communicates with web applications, and how web applications can be chained together to process one request. Provided a standard for synchronous Python apps

### What is ASGI?
    ASGI (Asynchronous Server Gateway Interface) is a successor to WSGI. It is intended to provide a standard interface between async-capable Python web servers, frameworks, and applications. It is backward compatible with WSGI.
    https://asgi.readthedocs.io/en/latest/

### What is celery and what are task queues used for?
    Celery is an open source asynchronous task queue or job queue based on distributed message passing.
    https://en.wikipedia.org/wiki/Celery_(software)

## Databases:

### What is PostgreSQL? 
    It is a open source advanced relational database management system
    https://en.wikipedia.org/wiki/PostgreSQL

### Using StackShare, list 3 well-known companies that use PostgreSQL.
    Uber 
    Netflix
    Instagram
    https://stackshare.io/postgresql#:~:text=PostgreSQL%20is%20an%20advanced%20object,category%20of%20a%20tech%20stack.

### List two other well-known databases.
    Oracle
    MySQL

### What are some of the pros and cons of using an Object Relational Mapper (ORM)?
*Pros*
    -No need to write SQL queries
    -We can easily switch from one database to another 
    -You can extend and inherent from models (OOP)
    -SQL injection is difficlut
*Cons*
    -Complex queries may cause performance issues if not written properly
    -Developers will tend to ignorace basic SQL skills which is useful
    
    https://centralblue.co.uk/blog/2019/01/the-pros-and-cons-of-object-relational-mapping-orm

### What is the purpose of database migrations?
    Migrations in django is the way the changes in models are propogated to the database.
    https://docs.djangoproject.com/en/3.1/topics/migrations/
    
    The genral database migration is changing from out platform to the other which is done t save cost, improve performance, for scalability etc.

### What is redis and what are two things it can be used for?
    It is a distributed in-memory key–value database.
    It can be used for caching and message brokering
    https://en.wikipedia.org/wiki/Redis

### Why do we use caches?
    Cache is a temporary storage area to store data so that data can be served faster in future requests.

## HTTP & REST:

- Which four HTTP methods does REST use for performing CRUD operations?
- What is Django REST Framework used for?
- What is serialization and why do we use it?
- Which type of object serialization notation is most commonly used on the web?
- What is Postman and what is it used for?
- What are websockets and what are they used for?

React:

- What is the virtual DOM?
- What is JSX?
- What are props used for?
- When and why would you use setState()?
- When would you use hooks?
- What is react-router used for?
- What is react-native used for?

Redux:

- What is redux used for?
- What are actions?
- What are reducers?
- What is the store?
- What is redux-thunk used for?

Javascript:

- What is NodeJS and how is it different from in-browser Javascript?
- What is npm and what is it used for?
- What is ES6? List the names of 3 features that ES6 provides.
- What is ReactJS and what is it used for?
- List two popular alternative Javascript libraries to ReactJS.
- What is the DOM? What is a virtual DOM?
- What is the difference between sessionStorage and localStorage?
- What is a library like Material-UI used for?

Docker:

- Why do we run apt-get update && apt-get install -y in one command when using

Docker?

- What are Docker containers and what are the pros and cons of using them?
- What is the difference between ADD and COPY with Docker?
- What is a .dockerignore file used for?
- What is Kubernetes and why didn’t we use it for this assignment?

Deployment:

- What is Amazon S3 used for?
- What is Amazon ECS?
- What is the difference between ECS Fargate and EC2?
- Name 3 other cloud providers.
- What is Sentry and what is it used for?
- What is Cloudflare and what is it used for?
- What is SendGrid and what is it used for?
- What is the difference between a DNS A record and a CNAME record?
