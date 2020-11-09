import React, {useState,useEffect} from 'react'
import { useSelector } from 'react-redux'
import Article from '../components/Article'
import ArticleForm from '../components/ArticleForm'


function ArticleList (props,{ value }) {
    const [articleList,setArticleList] = useState([])
    const token = useSelector(token=>token.token)

   useEffect(()=>{
        fetch("http://localhost:8000/gallery/api/articles/", {
                method: 'GET',
                Authorization: `Token ${token}`
            })
            .then(response => response.json())
            .then(data => setArticleList(data))
            .catch(error => console.log(error))
    })

    return (
            <div>
                <h2> Articles</h2>
                {
                    token ?
                        <ArticleForm requestType="post" articleID={null} btnText="Create"/>
                    :
                        <h3> Login to create articles</h3>
                }
                <br/>
                <h1> Article List </h1>
                {
                     token ?
                          <Article data={articleList}/>
                     :
                         <h3> Login to see posts</h3>
                }




            </div>
    )
}

export default ArticleList