import React,{Component} from 'react'
import {Card} from 'antd'
import TextField from '@material-ui/core/TextField'
import Button from '@material-ui/core/Button'



class PostForm extends Component {
    constructor(props) {
        super(props)
            this.state={

                content: '',
                image: ''
            }
    }

    handleChange = (event,field) => {

        this.setState({
          [field]: event.target.value,
        })
    }

    handleSubmit = (event,requestType,postID) => {
        event.preventDefault()

        const content= event.target.elements.content.value
        const token = localStorage.getItem("token")


        switch( requestType){
            case 'post':
                return fetch('http://127.0.0.1:8000/gallery/api/posts', {
                    method: 'POST',
                    Authorization: `${token}`,
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ content: content })
                })
                    .then(res => console.log(res))
                    .catch(error => console.log(error))


            case 'put':
                return fetch(`http://127.0.0.1:8000/gallery/api/posts/${postID}/`,{
                    method: 'PUT',
                    Authorization: `${token}`,
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({content: content})
                })
                    .then(res => console.log(res))
                    .catch(error => console.log(error))
        }

    }

    render () {
        const {content,image} = this.state
        return(
            <div>
                <Card title="Post">

                    <form onSubmit={(event) =>this.handleSubmit(
                        event,
                        this.props.requestType,
                        this.props.postID)}>

                        <div>
                            <TextField required id="standard-required" label="Content" defaultValue="Enter Content here" name="content" value={content} onChange={(event)=>this.handleChange(event,'content')} />

                        </div>
                        <div>
                            <label>Image</label>

                            <input name="image" type='file' id='single' onChange={(event)=>this.handleChange(event,'image')} />
                        </div>

                        <Button type="submit" variant="contained" color="primary"> {this.props.btnText} </Button>
                    </form>
                </Card>
            </div>
        )
    }
}


export default PostForm
