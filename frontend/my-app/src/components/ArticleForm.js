import React, {Component, useEffect, useState} from 'react'
import {Card} from 'antd'
import TextField from '@material-ui/core/TextField'
import Button from '@material-ui/core/Button'
import { useSelector} from "react-redux"



function ArticleForm (props) {

    const [title,setTitle]=useState('')
    const [content,setContent]=useState('')
    const token = useSelector(state=>state.auth.token)


    useEffect((event,field)=>{
        return
    },[])

    function handleTitleChange (event) {
        setTitle(event.target.value)

    }
    function handleContentChange (event) {
        setContent(event.target.value)

    }

    function handleSubmit (event,requestType,articleID)  {
        event.preventDefault()
        setTitle(event.target.elements.title.value)
        setContent(event.target.elements.content.value )
        //const token = localStorage.getItem("token")



        switch( requestType){
            case 'post':
                return fetch('http://127.0.0.1:8000/gallery/api/articles/', {
                    method: 'POST',
                    Authorization: `Token ${token}`,
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ title: title, content: content })
                })
                    .then(res => console.log(res))
                    .catch(error => console.log(error))


            case 'put':
                return fetch(`http://127.0.0.1:8000/gallery/api/articles/${articleID}/`,{
                    method: 'PUT',
                    Authorization: `Token ${token}`,
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({title: title, content: content})
                })
                    .then(res => console.log(res))
                    .catch(error => console.log(error))

        }

    }
        return(
            <div>
                <Card title="Article">

                    <form onSubmit={(event) =>handleSubmit(
                        event,
                        props.requestType,
                        props.articleID)}>

                        <div>
                            <TextField required id="standard-required" label="Article Title" defaultValue="Enter Title here" name="title" value={title} onChange={handleTitleChange} />

                        </div>

                        <div>
                            <TextField required id="standard-required" label="Content" defaultValue="Enter Content here" name="content" value={content} onChange={handleContentChange} />

                        </div>

                        <Button type="submit" variant="contained" color="primary"> {props.btnText} </Button>
                    </form>
                </Card>
            </div>
        )

}


export default ArticleForm
