import React from 'react'

function Video({video}){

    return (
        <div>
            <h3>{video.title}</h3>
            <div>Description {video.description}</div>
            <div>Type: {video.type}</div>
            <div> <img src={video.thumbnail} /></div>
            <div> {video.link}</div>
        </div>)
}
export default Video