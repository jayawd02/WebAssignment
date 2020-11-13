import * as actionTypes from './postActionTypes'

export const fetchPostsRequest = () => {
    return{
        type: actionTypes.FETCH_POSTS_REQUEST
    }
}

export const fetchPostsSuccess = posts=> {
    return {
        type: actionTypes.FETCH_POSTS_SUCCESS,
        payload: posts
    }
}

export const fetchPostsFailure = error => {
    return {
        type: actionTypes.FETCH_POSTS_FAILURE,
        payload: error
    }
}

export const fetchPosts = () => {
    const token =localStorage.getItem('token')
    return async (dispatch) => {
        dispatch(fetchPostsRequest())
        const result = await fetch("http://localhost:8000/gallery/api/posts/",{
                method: 'GET',
                Authorization: `Token ${token}`
            })
            .then(response => response.json())
            .then(data => {
                const posts = data
                dispatch(fetchPostsSuccess(posts))
            })
            .catch(error =>{
                const errorMsg=error.message
                dispatch(fetchPostsFailure(errorMsg))
            })
    }
}
