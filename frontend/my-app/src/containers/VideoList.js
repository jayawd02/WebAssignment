import React, {useEffect, useState} from 'react'
import { useSelector,useDispatch } from 'react-redux'
import Video from '../components/Video'
import VideoForm from '../components/VideoForm'
import {decrease, increase} from "../redux";

function VideoList ({ value }){
    const [videoList,setVideoList] = useState([])
    //const token = localStorage.getItem('token')
    const token = useSelector(state=>state.auth.token)
    const counter =useSelector(state=>state.counter.counter)
    const dispatch = useDispatch()
    const api_url = process.env.REACT_APP_API_URL


    useEffect(()=>{
            fetch(`${api_url}/gallery/api/videos`,{Authorization: token})
            .then(response => response.json())
            .then(data => setVideoList(data))

    },[])

    return (
      <div>
          <div>
                    <h2> Counter : {counter}</h2>
                    <button onClick={()=>dispatch(increase())}> INCREMENT</button>
                    <button onClick={()=>dispatch(decrease())}> DECREMENT</button>
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