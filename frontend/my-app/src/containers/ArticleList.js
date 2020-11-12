import React, {useState,useEffect} from 'react'
import { useSelector, useDispatch } from 'react-redux'
import Article from '../components/Article'
import ArticleForm from '../components/ArticleForm'
import {fetchArticles} from "../redux"
import Loading from "../components/Loading";

function  ArticleList (props) {
    //const [articleList,setArticleList] = useState([])
    const token = useSelector(state=>state.auth.token)
    const dispatch =useDispatch()
    let articleData =useSelector(state=>state.article)

   useEffect(()=>{
       dispatch(fetchArticles())

       /*const fetchData = async () => {
            const result = await fetch("http://localhost:8000/gallery/api/articles/", {
                method: 'GET',
                Authorization: `Token ${token}`
            })
                .then(response => response.json())
                .then(data => setArticleList(data))
                .catch(error => console.log(error))
        }
       fetchData()*/

   }, [])

    return (
            <div>
                {
                    token ? (
                        articleData.loading?
                                <Loading/>
                        : articleData.error ? (
                              <p> {articleData.error}</p>
                        ): (
                            <div>
                                <h2> Articles</h2>
                                <ArticleForm requestType="post" articleID={null} btnText="Create"/>
                                <br/>

                                <h1> Article List </h1>
                                <Article data={articleData.articles}/>
                                {console.log("articleData",articleData)}
                            </div>
                            )
                    ):
                        <h3> Login to see articles</h3>
                }
            </div>
    )
}

export default ArticleList