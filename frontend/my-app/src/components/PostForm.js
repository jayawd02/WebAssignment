import React,{Component} from 'react'
import {Card} from 'antd'
import axios from 'axios'


class PostForm extends Component {
    constructor(props) {
        super(props)
            this.state={
                posted_by: '',
                content: '',
                image: ''
            }
    }

    handlePostedByChange = (event) => {
        this.setState({
            posted_by: event.target.value
        })
    }

    handleContentChange = (event) =>{
        this.setState({
            content: event.target.value
        })
    }

    handleImageChange = (event) => {
        this.setState({
            image: event.target.value
        })
    }

    handleSubmit = (event,requestType,postID) => {
        event.preventDefault()
        const posted_by= event.target.elements.posted_by.value
        const content= event.target.elements.content.value

        console.log(posted_by,content)

        switch( requestType){
            case 'post':
                return axios.post('http://127.0.0.1:8000/gallery/api/posts/',{
                    posted_by:posted_by,
                    content: content
                })
                    .then(res => console.log(res))
                    .catch(error => console.log(error))
            case 'put':
                return axios.put(`http://127.0.0.1:8000/gallery/api/posts/${postID}/`,{
                    posted_by:posted_by,
                    content: content
                })
                    .then(res => console.log(res))
                    .catch(error => console.log(error))
        }

    }

    render () {
        const {posted_by,content,image} = this.state
        return(
            <div>
                <Card title="Post">

                    <form onSubmit={(event) =>this.handleSubmit(
                        event,
                        this.props.requestType,
                        this.props.postID)}>
                        <div>
                            <label>Posted By </label>
                            <input
                                name="posted_by"
                                type='text'
                                value={posted_by}
                                onChange={this.handlePostedByChange}
                            />
                        </div>
                        <div>
                            <label>Content</label>
                            <textarea name="content" value={content} onChange={this.handleContentChange}></textarea>
                        </div>
                        <div>
                            <label>Image</label>
                            <input name="image" type='file' id='single' onChange={this.handleImageChange} />
                        </div>
                        <button type="submit">{this.props.btnText}</button>
                    </form>
                </Card>
            </div>
        )
    }
}

export default PostForm
