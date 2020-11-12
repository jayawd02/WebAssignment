import {combineReducers} from "redux"
import articleReducer from "./article/articleReducer"
import authReducer from "./auth/authReducer"
import postReducer from "./post/postReducer"
import counterReducer from "./counterReducer"

const rootReducer =combineReducers({
    auth: authReducer,
    article : articleReducer,
    post: postReducer,
    counter: counterReducer

})

export default rootReducer