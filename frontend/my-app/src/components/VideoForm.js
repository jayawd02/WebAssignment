import React,{Component,  useState} from 'react'

import { Form, Input, Button} from 'antd'


class VideoForm extends Component {
    handleFormSubmit = (event)=> {
        event.preventDefault()

        const title= event.target.elements.title.value
        const type = event.target.elements.type.value
        const description = event.target.elements.description.value
        const thumbnail = event.target.elements.thumbnail.value
        const link = event.target.elements.link.value
        console.log("form submit clicked")
        console.log(title,type,description,link)
    }

    render (){
          return (
            <div>
              <Form onSubmitCapture={this.handleFormSubmit} layout="vertical">

                <Form.Item label="Title">
                  <input name="title" placeholder="Enter video title" />
                </Form.Item>
                <Form.Item label="Type">
                  <input name="type" placeholder="Enter type" />
                </Form.Item>
                <Form.Item label="Description">
                  <textarea name="description" placeholder="Enter description here" />
                </Form.Item>
                <Form.Item label="Image">
                  <Input type='file' id='single'  name="thumbnail" />
                </Form.Item>
                <Form.Item label="Link">
                  <input name="link" placeholder="Enter link to video here" />
                </Form.Item>
                <Form.Item >
                  <Button type="primary" htmlType="submit" >Submit</Button>
                </Form.Item>
              </Form>
            </div>
          )
    }

}

export default VideoForm
