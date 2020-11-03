import React, {Component} from 'react'
import Recipe from './Recipe'

class RecipeList extends Component{
  constructor(props) {
    super(props)
    this.state = {
      recipeList: []
    }
    this.fetchrecipes=this.fetchRecipes.bind(this)
  }

  componentWillMount() {
    this.fetchRecipes()
  }

  fetchRecipes(){
    console.log('fetching..')

    fetch("http://localhost:8000/gallery/recipes")
        .then(response => response.json())
        .then (data =>
        this.setState({
          recipeList: data
        })
        )

  }

  render(){
    var recipes= this.state.recipeList
    const recipeList =recipes.map(recipe=> <Recipe key={recipe.id} recipe={recipe}/>)
    return (
      <div>
        <h1> Recipe List </h1>
          <div>{recipeList}</div>
      </div>
    )
  }
}
export default RecipeList