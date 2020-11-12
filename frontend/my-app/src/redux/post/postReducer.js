import * as actionTypes from './postActionTypes'

const initialState ={
    postLoading:false,
    posts:[],
    error:''
}

const postReducer = (state=initialState, action) => {
    switch (action.type){
        case actionTypes.FETCH_POSTS_REQUEST:
            return {
                ...state,
                postLoading: true
            }

        case actionTypes.FETCH_POSTS_SUCCESS:
            return {
                postLoading: false,
                posts: action.payload,
                error:''
            }

        case actionTypes.FETCH_POSTS_FAILURE:
            return {
                postLoading: false,
                posts: [],
                error:action.payload
            }
        default:
            return state
    }
}

export default postReducer

