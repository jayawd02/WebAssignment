import React,{Component} from 'react'
import {Card} from 'antd'

class CreatePost extends Component {
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

    handleSubmit = (event) => {
        alert ( `${this.state.posted_by} ${this.state.content} `)
        event.preventDefault()
    }

    render () {
        const {posted_by,content,image} = this.state
        return(
            <div>
                <Card title="New Post">

                    <form onSubmit={this.handleSubmit}>
                        <div>
                            <label>Posted By </label>
                            <input
                                type='text'
                                value={posted_by}
                                onChange={this.handlePostedByChange}
                            />
                        </div>
                        <div>
                            <label>Content</label>
                            <textarea value={content} onChange={this.handleContentChange}></textarea>
                        </div>
                        <div>
                            <label>Image</label>
                            <input type='file' id='single' onChange={this.handleImageChange} />
                        </div>
                        <button type="submit">Submit</button>
                    </form>
                </Card>
            </div>
        )

    }
}
export default CreatePost
