import React, {Component} from 'react'
import {Card,Button} from 'antd'
import ArticleForm from "../components/ArticleForm"
import {connect} from 'react-redux'
import {fetchArticles} from "../redux"


class ArticleDetail extends Component{
  constructor(props) {
    super(props)
    this.state = {
      article: {}
    }

  }

  async componentDidMount() {
    const api_url = process.env.REACT_APP_API_URL
    const articleID = this.props.match.params.articleID
    const token = this.state.token

    const response =  await fetch(`${api_url}/gallery/api/articles/${articleID}`, {
                method: 'GET',
                Authorization: `Token ${token}`
            })
    const responseJson = await response.json()

   if (response.ok) {
      this.setState({
        article :responseJson
      })
    } else {
      this.setState({
        error: true,
      })
    }
  }

  componentWillUnmount (){
        console.log ("unmount")
    }

  handleDelete= (event) => {
        const articleID = this.props.match.params.articleID
        const token = this.state.token
        const api_url = process.env.REACT_APP_API_URL

        fetch(`${api_url}/gallery/api/articles/${articleID}`,{method:'DELETE', Authorization: `Token ${token}`})
        this.props.history.push('/')
        this.forceUpdate()
  }

  handleTokenNotNull =()=>{
      if (this.state.token !==null){
          return true
      }else{
          return false
      }
  }



  render(){
    return (
      <div>
        <h1> Article Detail </h1>
            <Card title={this.state.article.title}>

                <p>{this.state.article.content} </p>

                <div>
                    <form onSubmit={this.handleDelete}>
                        <Button htmlType="submit" type="danger">Delete</Button>
                    </form>
                </div>

            </Card>

                {
                    this.handleTokenNotNull() ?
                          <ArticleForm requestType="put" articleID={this.props.match.params.articleID} data={this.state.post} btnText="Update"/>
                    :
                        <h3> You are not authorized to edit this article </h3>
                }

      </div>
    )
  }
}

const mapStateToProps= state =>{
    return{
        token: state.auth.token
    }
}

const mapDispatchToProps = dispatch => {
    return {
        fetchArticles: ()=> dispatch(fetchArticles())
    }
}

export default connect(mapStateToProps,mapDispatchToProps)(ArticleDetail)