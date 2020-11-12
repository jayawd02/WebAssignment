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
