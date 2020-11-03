import React,{Component} from 'react'
import Loading from './Loading'
import {Link} from "react-router-dom"


export default class Video extends Component {
  constructor(props) {
    super(props)
    // this.state = {
    //   id: 'No ID',
    //   title: 'No Video Name Yet',
    //   description: '',
    //   type: '',
    //   thumbnail: null,
    //   link:''
    // }
  }

  /*async componentDidMount() {
    const response = await fetch("http://localhost:8000/gallery/videos/16/")
    const responseJson = await response.json()
    if (response.ok) {
      this.setState({
        id: responseJson['id'],
        title: responseJson.title,
        hasLoaded: true,
        thumbnail: responseJson.thumbnail,
      })
    } else {
      this.setState({
        error: true,
      })
    }
    console.log(response)
    console.log(responseJson)
  }
*/

  render() {
    //const { children } = this.props
    const {
      id,
      title,
      description,
      type,
      thumbnail,
      link
    } = this.state

    return (
      <p>
        Video: ID = {id} ---
        Title = {title} ---
        description = {description} ---
        type = {type} ---
        <img src={thumbnail} /> ---
        link = {link}
        <hr />
      </p>

        //{/*{videos.map(function(video,index){
        //  return(
          //    <div key={index}>
            //    <span>{video.title}
              //  {video.description} - {video.type}
                //<img src={video.thumbnail} /></span>

              //</div>
          //)
        //})}*/}
    )
  }
}






