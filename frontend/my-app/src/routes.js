import React from 'react'
import {Route} from 'react-router-dom'
import PostList from './containers/PostList'
import VideoList from "./containers/VideoList"
import RecipeList from "./containers/RecipeList"
import PostDetail from "./containers/PostDetail"
import PostForm from "./components/PostForm"
import Login from './containers/Login'
import Signup from './containers/Signup'
import Home from './containers/Home'
import ProfileDetail from './containers/ProfileDetail'
import RecipeForm from './components/RecipeForm'
import RecipeDetail from './containers/RecipeDetail'
import VideoForm from './components/VideoForm'
import VideoDetail from './containers/VideoDetail'
import ArticleList from './containers/ArticleList'
import ArticleDetail from './containers/ArticleDetail'

const BaseRouter = () => (
    <div>
        <Route exact path='/' component={Home} />
        <Route exact path='/posts' component={PostList} />
        <Route exact path='/videos' component={VideoList} />
        <Route exact path='/recipes' component={RecipeList} />
        <Route exact path='/posts/:postID' component={PostDetail} />
        <Route exact path='/post/new' component={PostForm} />
        <Route exact path='/videos/:videoID' component={VideoDetail} />
        <Route exact path='/video/new' component={VideoForm} />
        <Route exact path='/recipes/:recipeID' component={RecipeDetail} />
        <Route exact path='/recipe/new' component={RecipeForm} />
        <Route exact path='/articles' component={ArticleList} />
        <Route exact path='/articles/:articleID' component={ArticleDetail} />
        <Route exact path='/login' component={Login} />
        <Route exact path='/signup' component={Signup} />
        <Route exact path='/profile/:memberID' component={ProfileDetail} />

    </div>

)

export default BaseRouter