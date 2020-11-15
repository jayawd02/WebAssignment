import * as actionTypes from './articleActionTypes'

export const fetchArticlesRequest = () => {
    return{
        type: actionTypes.FETCH_ARTICLES_REQUEST
    }
}

export const fetchArticlesSuccess = articles=> {
    return {
        type: actionTypes.FETCH_ARTICLES_SUCCESS,
        payload: articles
    }
}

export const fetchArticlesFailure = error => {
    return {
        type: actionTypes.FETCH_ARTICLES_FAILURE,
        payload: error
    }
}

export const fetchArticles = () => {
    const token =localStorage.getItem('token')
    const api_url = process.env.REACT_APP_API_URL
    return async (dispatch) => {
        dispatch(fetchArticlesRequest())
        const result = await fetch(`${api_url}/gallery/api/articles/`,{
                method: 'GET',
                Authorization: `Token ${token}`
            })
            .then(response => response.json())
            .then(data => {
                const articles = data
                dispatch(fetchArticlesSuccess(articles))
            })
            .catch(error =>{
                const errorMsg=error.message
                dispatch(fetchArticlesFailure(errorMsg))
            })
    }
}
