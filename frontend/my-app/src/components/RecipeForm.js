import React,{Component} from 'react'
import axios from 'axios'
import TextField from '@material-ui/core/TextField'
import Button from '@material-ui/core/Button'
import Select from '@material-ui/core/Select'
import InputLabel from '@material-ui/core/InputLabel'
import Card from '@material-ui/core/Card'
import CardActions from '@material-ui/core/CardActions'
import CardContent from '@material-ui/core/CardContent'



class RecipeForm extends Component {
    constructor(props) {
        super(props)
            this.state={
                name: '',
                type: '',
                category: '',
                description:'',
                recipe_image:'',
                ingredients:'',
                prep_time:''
            }
    }

    handleChange = (event) => {
        const type= event.target.elements.type.value
        this.setState({
          ...this.state,
          [type]: event.target.value,
        })
    }



    handleSubmit = (event,requestType,recipeID) => {
        event.preventDefault()
        const name= event.target.elements.name.value
        const type= event.target.elements.type.value

        console.log(name,type)


    }

    render () {
        const {name,type,category,description,recipe_image,ingredients,prep_time} = this.state
        return(
            <div>
                <Card title="Post">
                    <form onSubmit={(event) =>this.handleSubmit(
                            event,
                            this.props.requestType,
                            this.props.recipeID)}>
                        <CardContent>
                            <div>

                                <TextField required id="standard-required" label="Name" defaultValue="Enter Recipe Name here" name="name" value={name}  />

                            </div>
                            <div>
                                <InputLabel htmlFor="age-native-simple">Type</InputLabel>
                                <Select
                                  native
                                  value={type}
                                  onChange={this.handleChange}
                                  inputProps={{
                                    name: 'type',
                                    id: 'type-native-simple',
                                  }}
                                >
                                  <option aria-label="None" value="" />
                                  <option value={'Vegan'}>Vegan</option>
                                  <option value={'Vegetarian'}>Vegetarian</option>
                                  <option value={'Seafood'}>Seafood</option>
                                  <option value={'Meat'}>Meat</option>
                                  <option value={'Other'}>Other</option>
                                </Select>
                            </div>
                            <div>
                                <InputLabel htmlFor="age-native-simple">Category</InputLabel>
                                <Select
                                  native
                                  value={category}
                                  onChange={this.handleChange}
                                  inputProps={{
                                    name: 'category',
                                    id: 'category-native-simple',
                                  }}
                                >
                                  <option aria-label="None" value="" />
                                  <option value={'Main'}>Main</option>
                                  <option value={'Snack'}>Snack</option>
                                  <option value={'Side'}>Side</option>
                                  <option value={'Soup'}>Soup</option>
                                  <option value={'Salad'}>Salad</option>
                                  <option value={'Dessert'}>Dessert</option>
                                  <option value={'Drink'}>Drink</option>
                                  <option value={'Other'}>Other</option>
                                </Select>
                            </div>
                            <div>
                                <TextField required id="standard-required" label="Description" defaultValue="Enter Description here" name="description" value={description}  />

                            </div>
                            <div>
                                <label>Recipe Image </label>

                                <input name="recipe_image" type='file' id='single'  />
                            </div>
                            <div>
                                <TextField required id="standard-required" label="Ingredients" defaultValue="Enter Ingredients here" name="ingredients" value={ingredients}  />

                            </div>

                            <div>
                                <TextField required id="standard-required" label="Prep Time" defaultValue="Enter prep time here" name="prep_time" value={prep_time}  />

                            </div>
                        </CardContent>
                        <CardActions>
                                <Button type="submit" variant="contained" color="primary"> {this.props.btnText} </Button>
                        </CardActions>
                    </form>
                </Card>
            </div>
        )
    }
}

export default RecipeForm
