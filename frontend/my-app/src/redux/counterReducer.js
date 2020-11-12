const COUNTER_INCREMENT='COUNTER INCREMENT'
const COUNTER_DECREMENT='COUNTER DECREMENT'

export const increase =()=>{
    return {
        type: COUNTER_INCREMENT
    }
}

export const decrease =()=>{
    return {
        type: COUNTER_DECREMENT
    }
}

const initialState ={
    counter:0
}

const counterIncrement=(state,action)=>{
    return {
        ...state,
        counter:state.counter+1
    }

}

const counterDecrement=(state,action)=>{
    return {
        ...state,
        counter:state.counter-1
    }

}

const counterReducer = (state=initialState, action) => {
    switch(action.type){
        case COUNTER_INCREMENT: return counterIncrement(state,action)
        case COUNTER_DECREMENT: return counterDecrement(state,action)
        default:
            return state
    }

}

export default counterReducer