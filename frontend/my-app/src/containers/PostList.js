import React, {useState,useEffect} from 'react'
import { useSelector,useDispatch } from 'react-redux'
import Post from '../components/Post'
import PostForm from '../components/PostForm'
import {fetchPosts} from "../redux"
import Loading from "../components/Loading"


function PostList (props,{ value }) {
    //const [postList,setPostList] = useState([])
    //const token = localStorage.getItem('token')
    const token = useSelector(state=>state.auth.token)
    const dispatch = useDispatch()
    let postData= useSelector(state=> state.post)



    useEffect(()=>{
        dispatch(fetchPosts())
            /*fetch("http://localhost:8000/gallery/api/posts",{Authorization: `Token ${token}`})
            .then(response => response.json())
            .then(data => setPostList(data))
*/
    },[])

    return (
            <div>
                {
                    token ? (
                        postData.loading?
                                <Loading/>
                        : postData.error ? (
                              <p> {postData.error}</p>
                        ): (
                            <div>
                                <h2> Create New Post</h2>
                                <PostForm requestType="post" postID={null} btnText="Create"/>
                                <h1> Post List </h1>
                                <Post data={postData.posts}/>
                            </div>
                        )
                    ):
                        <h3> Login to see posts</h3>
                }
            </div>
    )
}

export default PostList