import './App.css'
import VideoList from './components/VideoList'
import {
BrowserRouter as Router,
Switch,
Route,
Link,
} from 'react-router-dom'
import ButtonAppBar from "./components/Appbar"
import React from "react"
import PostList from "./components/PostList"
import RecipeList from "./components/RecipeList"

const routes ={
  'recipe': '/recipes',
  'video':'/videos',
  'post': '/posts'
}

function App() {
  return (

      <Router>
        <ButtonAppBar />
          <div className="App">
            <header className="App-header">
              <h1> Links </h1>
              <ul>
                <li> <Link to={routes.recipe}>Recipes </Link> </li>
                <li> <Link to={routes.video}> Videos </Link> </li>
                <li> <Link to={routes.post}> Posts </Link> </li>

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
              </Switch>

            </header>
          </div>
      </Router>
  )
}

export default App
