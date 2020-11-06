import React, {Component} from 'react'
import Recipe from '../components/Recipe'
import axios from 'axios'
import RecipeForm from "../components/RecipeForm"



class RecipeList extends Component{
  constructor(props) {
    super(props)
    this.state = {
      recipeList: []
    }

  }

  componentDidMount() {
    axios.get('http://localhost:8000/gallery/api/recipes')
        .then (res => {
          this.setState({
            recipeList :res.data
          })
          console.log(res.data)
        })
  }

  render(){
    return (
      <div>
        <h2>Create Recipe</h2>
        <br/>
        <RecipeForm requestType="post" postID={null} btnText="Create"/>
        <h1> Recipe List </h1>
        <Recipe data={this.state.recipeList}/>
      </div>
    )
  }
}
export default RecipeList