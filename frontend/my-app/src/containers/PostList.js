import React, {Component,useState,useEffect} from 'react'
import Post from '../components/Post'
import PostForm from '../components/PostForm'
import {connect} from 'react-redux'

class PostList extends Component {

    constructor(props) {
    super(props)
    this.state = {
      postList: []
    }
  }

  async componentWillReceiveProps(newPros) {
        if (newPros.token){
            const response = await fetch("http://localhost:8000/gallery/api/posts",{Authorization: newPros.token})
            const responseJson = await response.json()
            if (response.ok) {
              this.setState({
                postList :responseJson
              })
            } else {
              this.setState({
                error: true,
              })
                console.log(this.state.error)
            }

        }
        this.forceUpdate()
  }

    componentWillUnmount (){
        console.log ("unmount")
    }


    render()
    {
        return (
            <div>
                <h2> Create New Post</h2>
                {
                    this.props.token ?
                        <PostForm requestType="post" postID={null} btnText="Create"/>
                    :
                        <h3> Login to create posts</h3>
                }

                <br/>
                <h1> Post List </h1>


                {
                    this.props.token ?
                         <Post data={this.state.postList}/>
                    :
                         <h3> Login to see posts</h3>
                }
            </div>
        )
    }
}

const mapStateToProps= state =>{
    return{
        token: state.token
    }
}

export default connect(mapStateToProps)(PostList)