import React from 'react'
import {Route} from 'react-router-dom'
import PostList from './containers/PostList'
import VideoList from "./containers/VideoList"
import RecipeList from "./containers/RecipeList"
import PostDetail from "./containers/PostDetail"
import PostForm from "./components/PostForm"
import Login from './containers/Login'
import Signup from './containers/Signup'

const BaseRouter = () => (
    <div>
        <Route exact path='/' component={PostList} />
        <Route exact path='/posts' component={PostList} />
        <Route exact path='/videos' component={VideoList} />
        <Route exact path='/recipes' component={RecipeList} />
        <Route exact path='/posts/:postID' component={PostDetail} />
        <Route exact path='/post/new' component={PostForm} />
        <Route exact path='/login' component={Login} />
        <Route exact path='/signup' component={Signup} />

    </div>

)

export default BaseRouter