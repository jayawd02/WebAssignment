import React, {useEffect, useState} from 'react'
import { useSelector,useDispatch } from 'react-redux'
import Video from '../components/Video'
import VideoForm from '../components/VideoForm'

function VideoList ({ value }){
    const [videoList,setVideoList] = useState([])
    //const token = localStorage.getItem('token')
    const token = useSelector(token=>token.token)
    const dispatch = useDispatch()


    useEffect(()=>{
            fetch("http://localhost:8000/gallery/api/videos",{Authorization: token})
            .then(response => response.json())
            .then(data => setVideoList(data))

    })

    return (
      <div>
          <div>
                      <span>{value}</span>
                      <button onClick={() => dispatch({ type: 'increment-counter' })}>
                        Increment counter
                      </button>
                    </div>
        <h2>Create Video</h2>
        <br/>
        <VideoForm requestType="post" videoID={null} btnText="Create"/>
        <h1> Video List </h1>
        <Video data={videoList}/>
      </div>
    )

}
export default VideoList