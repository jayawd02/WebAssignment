import React, {Component} from 'react'
import Profile from "./Profile"

class ProfileDetail extends Component{
  constructor(props) {
    super(props)
    this.state = {
      profile: {}
    }
  }

  componentDidMount() {
      const { profile } = this.state.profile
      const cachedHits = sessionStorage.getItem(profile)
      const api_url = process.env.REACT_APP_API_URL

      if (cachedHits) {
        this.setState({ profile: JSON.parse(sessionStorage.getItem(profile)) })
      } else {
          const memberID = this.props.match.params.memberID
          fetch(`${api_url}/members/api/members/${memberID}`)
            .then(response => response.json())
            .then(result => this.onSetResult(result,"profile"))

      }
      this.forceUpdate()
  }

  onSetResult = (result, key) => {
    sessionStorage.setItem(key, JSON.stringify(result))
    this.setState({ profile: result })
  }



  render(){
    return (
      <div>
        <h1> Profile Detail </h1>
            <Profile data={this.state.profile}/>
      </div>
    )
  }
}
export default ProfileDetail