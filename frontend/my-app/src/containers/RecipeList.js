import React, {useEffect, useState} from 'react'
import { useSelector } from 'react-redux'
import Recipe from '../components/Recipe'
import RecipeForm from "../components/RecipeForm"



function RecipeList (){
    const [recipeList,setRecipeList] = useState([])
    //const token= localStorage.getItem('token')
    const token = useSelector(token=>token.token)

    useEffect(()=>{
            fetch("http://localhost:8000/gallery/api/recipes",{Authorization: token})
            .then(response => response.json())
            .then(data => setRecipeList(data))

    },[])

    return (
      <div>
        <h2>Create Recipe</h2>
        <br/>
        <RecipeForm requestType="post" recipeID={null} btnText="Create"/>
        <h1> Recipe List </h1>
        <Recipe data={recipeList}/>
      </div>
    )
}
export default RecipeList