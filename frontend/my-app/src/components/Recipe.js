import React from 'react'

function Recipe({recipe}){

    return (
        <div>
            <h3> {recipe.name}</h3>
            <div> Posted By: {recipe.posted_by}</div>
            <div> Description: {recipe.description}</div>
            <div> Type: {recipe.type}</div>
            <div> Category: {recipe.category}</div>
            <div> Ingredients: {recipe.ingredients}</div>
            <div> Prep time:{recipe.prep_time}</div>
            <div> <img src={recipe.recipe_image} /></div>

        </div>)
}
export default Recipe