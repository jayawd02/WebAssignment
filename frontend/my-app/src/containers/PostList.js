import React, {useState,useEffect} from 'react'
import { useSelector,useDispatch } from 'react-redux'
import Post from '../components/Post'
import PostForm from '../components/PostForm'


function PostList (props,{ value }) {
    const [postList,setPostList] = useState([])
    //const token = localStorage.getItem('token')
    const token = useSelector(token=>token.token)
    const dispatch = useDispatch()


    useEffect(()=>{
            fetch("http://localhost:8000/gallery/api/posts",{Authorization: token})
            .then(response => response.json())
            .then(data => setPostList(data))

    })

    return (
            <div>
                <div>
                      <span>{value}</span>
                      <button onClick={() => dispatch({ type: 'increment-counter' })}>
                        Increment counter
                      </button>
                    </div>
                <h2> Create New Post</h2>

                {
                    token ?
                        <PostForm requestType="post" postID={null} btnText="Create"/>
                    :
                        <h3> Login to create posts</h3>
                }
                <br/>
                <h1> Post List </h1>
                {
                    token ?
                         <Post data={postList}/>
                    :
                         <h3> Login to see posts</h3>
                }
            </div>
    )
}

export default PostList