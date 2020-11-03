import React, {Component} from 'react'
import Post from './Post'

class PostList extends Component{
  constructor(props) {
    super(props)
    this.state = {
      postList: []
    }
    this.fetchPosts=this.fetchPosts.bind(this)
  }

  componentWillMount() {
    this.fetchPosts()
  }

  fetchPosts(){
    console.log('fetching..')

    fetch("http://localhost:8000/gallery/posts")
        .then(response => response.json())
        .then (data =>
        this.setState({
          postList: data
        })
        )
  }

  render(){
    var posts= this.state.postList
    const postList =posts.map(post=> <Post key={post.id} post={post}/>)
    return (
      <div>
        <h1> Post List </h1>
          <div>{postList}</div>
      </div>
    )
  }
}
export default PostList