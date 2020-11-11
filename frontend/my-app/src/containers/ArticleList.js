import React, {useState,useEffect} from 'react'
import { useSelector } from 'react-redux'
import Article from '../components/Article'
import ArticleForm from '../components/ArticleForm'

function  ArticleList (props) {

    const [articleList,setArticleList] = useState([])
    const token = useSelector(token=>token.token)

   useEffect(()=>{
        const fetchData = async () => {
            const result = await fetch("http://localhost:8000/gallery/api/articles/", {
                method: 'GET',
                Authorization: `Token ${token}`
            })
                .then(response => response.json())
                .then(data => setArticleList(data))
                .catch(error => console.log(error))
        }
    fetchData()
  }, [])

    return (
            <div>
                {
                    token ?
                        (
                            <div>
                                <h2> Articles</h2>
                                <ArticleForm requestType="post" articleID={null} btnText="Create"/>
                                <br/>
                                <h1> Article List </h1>
                                <Article data={articleList}/>
                            </div>
                        )
                    :
                        <h3> Login to see articles</h3>
                }
            </div>
    )
}

export default ArticleList