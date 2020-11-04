import React from 'react'
import {Route} from 'react-router-dom'
import PostList from './containers/PostList'
import VideoList from "./containers/VideoList"
import RecipeList from "./containers/RecipeList"
import PostDetail from "./containers/PostDetail"
import CreatePost from "./components/CreatePost"

const BaseRouter = () => (
    <div>
        <Route exact path='/' component={PostList} />
        <Route exact path='/posts' component={PostList} />
        <Route exact path='/videos' component={VideoList} />
        <Route exact path='/recipes' component={RecipeList} />
        <Route exact path='/posts/:postID' component={PostDetail} />
        <Route exact path='/post/new' component={CreatePost} />

    </div>

)

export default BaseRouter