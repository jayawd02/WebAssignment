import * as actionTypes from './articleActionTypes'

const initialState ={
    articleLoading:false,
    articles:[],
    error:''
}

const articleReducer = (state=initialState, action) => {
    switch (action.type){
        case actionTypes.FETCH_ARTICLES_REQUEST:
            return {
                ...state,
                articleLoading: true
            }

        case actionTypes.FETCH_ARTICLES_SUCCESS:
            return {
                articleLoading: false,
                articles: action.payload,
                error:''
            }

        case actionTypes.FETCH_ARTICLES_FAILURE:
            return {
                articleLoading: false,
                articles: [],
                error:action.payload
            }
        default:
            return state
    }
}

export default articleReducer

