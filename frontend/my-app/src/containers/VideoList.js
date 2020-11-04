import React, {Component} from 'react'
import Video from '../components/Video'

class VideoList extends Component{
  constructor(props) {
    super(props)
    this.state = {
      videoList: []
    }
    this.fetchVideos=this.fetchVideos.bind(this)
  }

  componentWillMount() {
    this.fetchVideos()
  }

  fetchVideos(){
    console.log('fetching..')

    fetch("http://localhost:8000/gallery/api/videos")
        .then(response => response.json())
        .then (data =>
        this.setState({
          videoList: data
        })
        )

  }

  render(){
    var videos= this.state.videoList
    const videoList =videos.map(video=> <Video key={video.id} video={video}/>)
    return (
      <div>
        <h1> Video List </h1>
          <div>{videoList}</div>


      </div>
    )
  }
}
export default VideoList