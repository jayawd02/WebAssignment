import React, {Component} from 'react'
import Video from '../components/Video'
import axios from 'axios'

import VideoForm from '../components/VideoForm'


class VideoList extends Component{
  constructor(props) {
    super(props)
    this.state = {
      videoList: []
    }
  }

  componentDidMount() {
    axios.get('http://localhost:8000/gallery/api/videos')
        .then (res => {
          this.setState({
            videoList :res.data
          })
          console.log(res.data)
        })
  }


  render(){
    return (
      <div>
        <h2>Create Video</h2>
        <br/>
        <VideoForm/>
        <h1> Post List </h1>
        <Video data={this.state.videoList}/>
      </div>
    )
  }
}
export default VideoList