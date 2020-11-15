import React, {Component} from 'react'
import axios from 'axios'
import {Card,Button} from 'antd'
import VideoForm from "../components/VideoForm"

class VideoDetail extends Component{
  constructor(props) {
    super(props)
    this.state = {
      video: {}
    }
  }

  componentDidMount() {
    const videoID = this.props.match.params.videoID
    const api_url = process.env.REACT_APP_API_URL

      axios.get(`${api_url}/gallery/api/videos/${videoID}`)
        .then (res => {
          this.setState({
            recipe :res.data
          })
            console.log(res.data)
        })
  }

  handleDelete= (event) => {
        const videoID = this.props.match.params.videoID
        const api_url = process.env.REACT_APP_API_URL

        axios.delete(`${api_url}/gallery/api/videos/${videoID}`)
        this.props.history.push('/')
        this.forceUpdate()
  }



  render(){
    return (
      <div>
        <h1> Video Detail </h1>
            <Card title={this.state.video.title}>
                <form onSubmit={this.handleDelete}>
                    <Button htmlType="submit" type="danger">Delete</Button>
                </form>
                <p>{this.state.video.description}
                Type: {this.state.video.type}

                </p>

                <a href={this.state.video.link}><img
                    width={272}
                    alt="post image"
                    src={this.state.video.thumbnail}
                  />
                </a>
            </Card>

          <VideoForm requestType="put" videoID={this.props.match.params.videoID} btnText="Update"/>
      </div>
    )
  }
}
export default VideoDetail