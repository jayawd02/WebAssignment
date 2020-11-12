import React, {Component} from 'react'
import {Card,Button} from 'antd'
import PostForm from "../components/PostForm"
import {connect} from 'react-redux'
import Post from "../components/Post";

class PostDetail extends Component{
  constructor(props) {
    super(props)
    this.state = {
      post: {}
    }
  }

  async componentDidMount() {
    const postID = this.props.match.params.postID
    const token=this.state.token
    //const token = localStorage.getItem("token")

    const response = await fetch(`http://localhost:8000/gallery/api/posts/${postID}`,{Authorization: {token}})
    const responseJson = await response.json()

    if (response.ok) {
      this.setState({
        post :responseJson
      })
    } else {
      this.setState({
        error: true,
      })
    }
  }

  componentWillUnmount (){
        console.log ("unmount")
    }

  handleDelete= (event) => {
        const postID = this.props.match.params.postID
        const token = localStorage.getItem("token")

        fetch(`http://localhost:8000/gallery/api/posts/${postID}`,{method:'DELETE',Authorization: {token}})
        this.props.history.push('/')
        this.forceUpdate()
  }

  handleTokenNotNull =()=>{
      if (this.state.token !==null){
          return true
      }else{
          return false
      }
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

                {
                    this.handleTokenNotNull() ?
                          <PostForm requestType="put" postID={this.props.match.params.postID} data={this.state.post} btnText="Update"/>
                    :
                        <h3> You are not authorized to edit this post </h3>
                }
          {console.log (this.handleTokenNotNull())}

      </div>
    )
  }
}

const mapStateToProps= state =>{
    return{
        token: state.auth.token
    }
}
export default connect(mapStateToProps)(PostDetail)