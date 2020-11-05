import React, {Component} from 'react'
import axios from 'axios'
import {Card,Button} from 'antd'
import PostForm from "../components/PostForm"

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

  handleDelete= (event) => {
        const postID = this.props.match.params.postID
        axios.delete(`http://localhost:8000/gallery/api/posts/${postID}`)
        this.props.history.push('/')
        this.forceUpdate()
  }



  render(){
    return (
      <div>
        <h1> Post Detail </h1>
            <Card title={this.state.post.posted_by}>
                <form onSubmit={this.handleDelete}>
                    <Button htmlType="submit" type="danger">Delete</Button>
                </form>
                <p>{this.state.post.content} </p>
                <img
                    width={272}
                    alt="post image"
                    src={this.state.post.image}
                  />
            </Card>

          <PostForm requestType="put" postID={this.props.match.params.postID} btnText="Update"/>
      </div>
    )
  }
}
export default PostDetail