import VideoList from './containers/VideoList'
import {BrowserRouter as Router,Switch,Route,Link,} from 'react-router-dom'
import BaseRouter from "./routes"
import ButtonAppBar from "./components/Appbar"
import React from "react"
import PostList from "./containers/PostList"
import RecipeList from "./containers/RecipeList"
import CreatePost from "./components/CreatePost"
import 'antd/dist/antd.css'
import CustomLayout from "./containers/Layout"

/*const routes ={
  'recipe': '/recipes',
  'video':'/videos',
  'post': '/posts',
  'createpost':'/createpost'
}*/

function App() {
  return (

      <div className="App">
        <Router>
          <CustomLayout>
            <BaseRouter />
          </CustomLayout>
        </Router>
      </div>
  )
}

export default App


/*
<ButtonAppBar />
            <header className="App-header">
              <h1> Links </h1>
              <ul>
                <li> <Link to={routes.recipe}>Recipes </Link> </li>
                <li> <Link to={routes.video}> Videos </Link> </li>
                <li> <Link to={routes.post}> Posts </Link> </li>
                <li> <Link to={routes.createpost}> Create Post </Link> </li>

              </ul>
              <Switch>
                <Route path ="/recipes">
                    <RecipeList>Recipe</RecipeList>
                </Route>
                <Route path ="/videos">
                  <VideoList >Video</VideoList>
                </Route>
                <Route path="/posts">
                  <PostList> Post</PostList>
                </Route>
                <Route path="/createpost">
                  <CreatePost> Post Create</CreatePost>
                </Route>
              </Switch>

            </header>*/
