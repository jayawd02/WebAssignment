## Architecture:
### When would you prefer to develop an Assignment 1 style web application (Server-side rendering, serving HTML)?
    For a simple and small application or a website with lot of static contents.

### When would you prefer an Assignment 2 one (REST API & Single Page Application)?
    When you want to serve multiple types of clients like a mobile and web clients, havign REST API based backend is beenefitial.
    The interactin between server and client is low as only the payload needs to be sent to the client.
    Some functionality can still work off line for eample a counter or a simple game

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
    Pros :
    - Easy to deploy and configure
    - Can scale easily

    Cons : 
    - Migrations to other platforms maynot be easy or stratight forward
    - Not all features are supported 
    - More costly

### What are some of the pros and cons of using Infrastructure-as-a-Service providers such as Amazon?
    Pros:
    - cheaper compared to PaaS

    Cons:
    - Complex to configure and need skills
    - difficult to migrate if proprietary database or cloud vendor specific technology is used

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

### Which four HTTP methods does REST use for performing CRUD operations?
    GET - for Read
    POST - to post/create
    PUT - to update
    DELETE - to delete

### What is Django REST Framework used for?
    It is used to build WEB APIs. It's a framework and a powerful tool kit with libraries to simplify developing. 
    https://www.django-rest-framework.org/

### What is serialization and why do we use it?
    It is the process of translating a data structure or object state into a format that can be stored or transmitted and reconstructed later.
    https://en.wikipedia.org/wiki/Serialization
    
### Which type of object serialization notation is most commonly used on the web?
    JSON – JavaScript Object Notation

### What is Postman and what is it used for?
    Postman is a popular API client that makes it easy for developers to create, share, test and document APIs.
    https://www.postman.com/

### What are websockets and what are they used for?
     It is a computer communications protocol, providing full-duplex communication channels over a single TCP connection. In WebSocket connection, the connection remains open and the data can be sent to the client even if the client has not asked for it. This saves a lot of requests because the client does not have to ask explicitly each time. WebSocket’s are faster and requires lower bandwidth. 
     https://en.wikipedia.org/wiki/WebSocket

## React:

### What is the virtual DOM?
    It is a programming concept where a “virtual”, representation of a UI is kept in memory and synced with the “real” DOM by a library such as ReactDOM. This process is called reconciliation. In React, changes are first made in Virtual DOM and then they are synced with the actual DOM

### What is JSX?
    JSX stands for JavaScript XML. JSX allows us to write HTML in React. 
    https://www.w3schools.com/react/react_jsx.asp#:~:text=JSX%20stands%20for%20JavaScript%20XML,and%20add%20HTML%20in%20React.

### What are props used for?
    Props stands for properties and is being used for passing data from one component to another.
    https://itnext.io/what-is-props-and-how-to-use-it-in-react-da307f500da0

### When and why would you use setState()?
    Setstate enqueues changes to the component state and tells React that this component and its children need to be re-rendered with the updated state
    https://reactjs.org/docs/react-component.html#setstate

### When would you use hooks?
    Hooks let you split one component into smaller functions based on what pieces are related, rather than forcing a split based on lifecycle methods.Hooks let you always use functions instead of having to constantly switch between functions, classes, higher-order components, and render props.
### What is react-router used for?
    It allows us to build a single-page web application with navigation without the page refreshing as the user navigates. React Router uses component structure to call components, which display the appropriate information.

### What is react-native used for?
    It is an open-source mobile application framework and used to develop applications for Android, Android TV, iOS, macOS, tvOS, Web, Windows and UWP by enabling developers to use React's framework along with native platform capabilities

## Redux:


### What is redux used for?
    Redux can be used as a data store for any UI layer.It is used mostly for application state management. Redux maintains the state of an entire application in a single immutable state tree (object), which can't be changed directly. 

### What are actions?
    Actions are a plain JavaScript object that contains information. Actions are the only source of information for the store. Actions have a type field that tells what kind of action to perform and all other fields contain information or data.
    https://redux.js.org/tutorials/fundamentals/part-3-state-actions-reducers
    https://www.geeksforgeeks.org/introduction-to-redux-action-reducers-and-store/

### What are reducers?
    Reducers are the pure functions that take the current state and action and return the new state and tell the store how to do

### What is the store?
    The store is the object which holds the state of the application

### What is redux-thunk used for?
    It is a middleware that lets you call action creators that return a function instead of an action object. That function receives the store's dispatch method, which is then used to dispatch regular synchronous actions inside the function's body once the asynchronous operations have been completed.
    https://www.digitalocean.com/community/tutorials/redux-redux-thunk#:~:text=Redux%20Thunk%20is%20a%20middleware,asynchronous%20operations%20have%20been%20completed.

## Javascript:

### What is NodeJS and how is it different from in-browser Javascript?
    Javascript is a popular programming language and it runs in any web browser with a good web browser. On the other hand, Node. js is an interpreter and environment for the JavaScript with some specific useful libraries which JS programming can be used separately.
    https://hackernoon.com/nodejs-vs-javascript-differences-and-similarities-6w1ws22pc#:~:text=Javascript%20is%20a%20popular%20programming,with%20a%20good%20web%20browser.&text=On%20the%20other%20hand%2C%20Node,programming%20can%20be%20used%20separately.

### What is npm and what is it used for?
    It is the package manager for the Node JavaScript platform. It puts modules in place so that node can find them, and manages dependency conflicts intelligently. It is used to publish, discover, install, and develop node programs.
    https://docs.npmjs.com/cli/v6/commands/npm

### What is ES6? 
    ECMAScript 6, also known as ES6 is a general-purpose programming language, standardized by Ecma International according to the document ECMA-262. It is a JavaScript standard meant to ensure the interoperability of Web pages across different Web browsers.
    https://en.wikipedia.org/wiki/ECMAScript
    List the names of 3 features that ES6 provides
    1.	Arrow functions
    2.	Promises
    3.	Destructuring 

### What is ReactJS and what is it used for?
     It is an open-source, front end, JavaScript library for building user interfaces or UI components.

### List two popular alternative Javascript libraries to ReactJS.
    1.	Angular 
    2.	Vuejs

### What is the DOM? What is a virtual DOM?
    The Document Object Model is a cross-platform and language-independent interface that treats an XML or HTML document as a tree structure wherein each node is an object representing a part of the document. It represents the web application that is loaded in the browser. It is a combination of static (HTML) as well as the dynamic (ES) part.
    Virtual DOM is conceptual representation of the real DOM. The UI (which is the DOM) is kept in sync with the virtual DOM with the help of ReactDOM library.
    https://en.wikipedia.org/wiki/Document_Object_Model

### What is the difference between sessionStorage and localStorage?
    Data in localStorage doesn't expire, data in sessionStorage is cleared when the page session ends. A page session lasts as long as the browser is open, and survives over page reloads and restores.
    https://developer.mozilla.org/en-US/docs/Web/API/Window/sessionStorage#:~:text=sessionStorage%20is%20similar%20to%20localStorage,over%20page%20reloads%20and%20restores.

### What is a library like Material-UI used for?
    It provides an optional CssBaseline component. It fixes some inconsistencies across browsers and devices while providing slightly more opinionated resets to common HTML elements. Using this library the application can look professional without the knowledge of designing concepts. There are large number of UI elements available out of the box which can save a lot of time and still present a unified design experience for the end user.
    

## Docker:

### Why do we run apt-get update && apt-get install -y in one command when using Docker?
    Once starting the container, we cannot work interactively with the shell we need to run it in the same line with -y switch

### What are Docker containers and what are the pros and cons of using them?
    Docker is a set of platform as a service products that use OS-level virtualization to deliver software in packages called containers. Containers are isolated from one another and bundle their own software, libraries and configuration files.
    https://en.wikipedia.org/wiki/Docker_(software)
    Pros
    - Provides consistency across a team
    - Eases the pain of debugging environments.
    Cons
    - Persistent data storage is complicated    
    
    https://affinitybridge.com/blog/pros-and-cons-docker
    https://www.channelfutures.com/open-source/docker-downsides-container-cons-to-consider-before-adopting-docker

### What is the difference between ADD and COPY with Docker?
    Both serve similar purposes. They let you copy files from a specific location into a Docker image. COPY takes in a src and destination. When you want to extract a local tar file into a specific directory in your Docker image ADD can be used.

### What is a .dockerignore file used for?
    Allows you to mention a list of files and/or directories which you might want to ignore while building the image similar to the .gitignore file

### What is Kubernetes and why didn’t we use it for this assignment?
    It is an open-source container-orchestration system for automating computer application deployment, scaling, and management. 
    We didn;t use it as our application is small and didn't include several containers or processes


## Deployment:

### What is Amazon S3 used for?
    It is storage for the Internet. It is designed to make web-scale computing easier for developers. Amazon S3 has a simple web services interface that you can use to store and retrieve any amount of data, at any time, from anywhere on the web.

### What is Amazon ECS?
    Elastic Container Service allows to run and manage, docker containers via tasks. These containers run in a defined cluster, and can be scaled up and down, they are actually EC2 instances. ECS does not runs the container, it only provides the control plane to manage tasks. ECS is basically EC2+ container agent.

### What is the difference between ECS Fargate and EC2?
    ECS has two launch types that can define how the compute resources will be managed. The traditional EC2 launch type detailed in the overview above utilizes your own EC2 instances. Fargate removes the responsibility of provisioning, configuring and managing the EC2 instances by allowing AWS to manage the EC2 instances.

### Name 3 other cloud providers.
    Google Cloud
    Microsoft Azzure
    IBM Cloud

### What is Sentry and what is it used for?
    It is a application monitoring and error tracking software. It provides alerts , logs .

### What is Cloudflare and what is it used for?
    Cloudflare is a free CDN type product that protects against threats such as SQL injection and identity theft. Cloudflare also improves site performance and speeds up loading times by using their multiple data centers that are located around the world. The Cloudflare network acts like a giant VPN

### What is SendGrid and what is it used for?
    SendGrid is a cloud-based SMTP provider that allows you to send email without having to maintain email servers. 

### What is the difference between a DNS A record and a CNAME record?
    A record’ maps a name to specific IP addresses, whereas ‘CNAME record’ points a name to another name instead of to an IP
