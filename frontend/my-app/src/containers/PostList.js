import React, {Component} from 'react'
import Post from '../components/Post'
import axios from 'axios'

class PostList extends Component{
  constructor(props) {
    super(props)
    this.state = {
      postList: []
    }

  }

  componentDidMount() {
    axios.get('http://localhost:8000/gallery/api/posts')
        .then (res => {
          this.setState({
            postList :res.data
          })
          console.log(res.data)
        })
  }



  render(){
    return (
      <div>
        <h1> Post List </h1>
        <Post data={this.state.postList}/>
      </div>
    )
  }
}
export default PostList