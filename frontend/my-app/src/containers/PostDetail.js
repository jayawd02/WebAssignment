import React, {Component} from 'react'
import axios from 'axios'
import {Card} from 'antd'

class PostDetail extends Component{
  constructor(props) {
    super(props)
    this.state = {
      post: {}
    }
  }

  componentDidMount() {
    const postID = this.props.match.params.postID
    axios.get(`http://localhost:8000/gallery/api/posts/${postID}`)
        .then (res => {
          this.setState({
            post :res.data
          })
            console.log(res.data)
        })
  }



  render(){
    return (
      <div>
        <h1> Post Detail </h1>
            <Card title={this.state.post.posted_by}>
                <p>{this.state.post.content} </p>
                <img
                    width={272}
                    alt="post image"
                    src={this.state.post.image}
                  />
            </Card>
      </div>
    )
  }
}
export default PostDetail