import React from 'react'

function Post({post}){

    return (
        <div>
            <h3>Posted By: {post.posted_by}</h3>
            <div> {post.content}</div>
            <div> <img src={post.image} /></div>
        </div>)
}
export default Post