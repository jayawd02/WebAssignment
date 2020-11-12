import {applyMiddleware, createStore,compose} from "redux"
import rootReducer from "./redux/rootReducer"
import thunk from "redux-thunk"

const composeEnhances = window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose

const store = createStore(rootReducer,composeEnhances(
    applyMiddleware(thunk)
))

export default store