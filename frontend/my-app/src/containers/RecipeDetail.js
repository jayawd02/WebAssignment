import React, {Component} from 'react'
import axios from 'axios'
import {Card,Button} from 'antd'
import RecipeForm from "../components/RecipeForm"

class RecipeDetail extends Component{
  constructor(props) {
    super(props)
    this.state = {
      recipe: {}
    }
  }

  componentDidMount() {
    const recipeID = this.props.match.params.recipeID
    const api_url = process.env.REACT_APP_API_URL

    axios.get(`${api_url}/gallery/api/recipes/${recipeID}`)
        .then (res => {
          this.setState({
            recipe :res.data
          })
            console.log(res.data)
        })
  }

  handleDelete= (event) => {
        const recipeID = this.props.match.params.recipeID
        const api_url = process.env.REACT_APP_API_URL

        axios.delete(`${api_url}/gallery/api/recipes/${recipeID}`)
        this.props.history.push('/')
        this.forceUpdate()
  }



  render(){
    return (
      <div>
        <h1> Recipe Detail </h1>
            <Card title={this.state.recipe.name}>
                <form onSubmit={this.handleDelete}>
                    <Button htmlType="submit" type="danger">Delete</Button>
                </form>
                <p>{this.state.recipe.description}
                Type: {this.state.recipe.type}
                Category: {this.state.recipe.category}
                Ingredients: {this.state.recipe.ingredients}
                Prep Time: {this.state.recipe.prep_time}
                </p>

                <img
                    width={272}
                    alt="post image"
                    src={this.state.recipe.recipe_image}
                  />
            </Card>

          <RecipeForm requestType="put" recipeID={this.props.match.params.recipeID} btnText="Update"/>
      </div>
    )
  }
}
export default RecipeDetail