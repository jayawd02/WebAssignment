import axios from 'axios'
import * as actionTypes from './actionTypes'

export const authStart = () => {
  return {
    type :actionTypes.AUTH_START
  }
}

export const authSucess= token => {
  return {
    type: actionTypes.AUTH_SUCCESS,
    token: token
  }
}

export const authFail = error => {
  return {
    type: actionTypes.AUTH_FAIL,
    error : error
  }
}

export const logout =() => {
  localStorage.removeItem('user')
  localStorage.removeItem('token')
  localStorage.removeItem('expirationDate')
  return{
    type: actionTypes.AUTH_LOGOUT
  }
}

export const checkAuthTimeout = expirationTime =>{
  return dispatch => {
    setTimeout(()=>{
        dispatch(logout())
    },expirationTime * 1000)
  }
}


export const authLogin = (username,password) => {
  return dispatch => {
    dispatch(authStart())
    axios.post('http://localhost:8000/rest-auth/login/',{
      username: username,
      password: password
    })
        .then(res => {
          const token = res.data.key
          const expirationDate = new Date(new Date().getTime()+ 3600*1000)
          localStorage.setItem('token',token)
          localStorage.setItem('expirationDate',expirationDate)
          dispatch(authSucess(token))
          dispatch(checkAuthTimeout(3600))

        })
        .catch(err => {
          dispatch(authFail(err))
        })
  }
}

export const authSignup = (username, email, password1, password2) => {
  return dispatch => {
    dispatch(authStart())
    axios.post('http://127.0.0.1:8000/users/api/register',{
      username: username,
      email: email,
      password1: password1,
      password2: password2

    })
        .then(res => {
          const token = res.data.key
          const expirationDate = new Date(new Date().getTime()+ 3600*1000)
          localStorage.setItem('token',token)
          localStorage.setItem('expirationDate',expirationDate)
          dispatch(authSucess(token))
          dispatch(checkAuthTimeout(3600))

        })
        .catch(err => {
          dispatch(authFail(err))
        })
  }
}

export const   authCheckState = () => {
    return dispatch => {
        const token = localStorage.getItem('token')
        if (token === undefined){
            dispatch(logout())
        }else{
            const expirationDate = new Date(localStorage.getItem('expirationDate'))
            if (expirationDate <= new Date()){
                dispatch(logout())
            }else{
                dispatch(authSucess(token))
                dispatch(checkAuthTimeout((expirationDate.getTime()-new Date().getTime())/1000))
            }
        }
    }
}

export const loadMember = (memberID) => async (dispatch, getState) => {
  dispatch({ type: actionTypes.MEMBER_LOADING });

  try {
    const res = await axios.get(`http://127.0.0.1:8000/members/api/members/$memberID` )
    dispatch({
      type: actionTypes.MEMBER_LOADED,
      payload: res.data
    })
  } catch (err) {
    dispatch({
      type: actionTypes.AUTH_FAIL
    })
  }
}


/*
// LOAD USER
export const loadUser = () => async (dispatch, getState) => {
  dispatch({ type: USER_LOADING });

  try {
    const res = await axios.get('/users/users', tokenConfig(getState));
    dispatch({
      type: USER_LOADED,
      payload: res.data
    });
  } catch (err) {
    dispatch({
      type: AUTH_ERROR
    });
  }
};

// LOGIN USER
export const login = ({ username, password }) => async dispatch => {
  // Headers
  const config = {
    headers: {
      'Content-Type': 'application/json'
    }
  };

  // Request Body
  const body = JSON.stringify({ username, password });

  try {
    const res = await axios.post('/users/login', body, config);
    dispatch({
      type: LOGIN_SUCCESS,
      payload: res.data
    });
  } catch (err) {
    dispatch({
      type: LOGIN_FAIL
    });
    dispatch(stopSubmit('loginForm', err.response.data));
  }
};

// helper function
export const tokenConfig = getState => {
  // Get token
  const token = getState().auth.token;

  // Headers
  const config = {
    headers: {
      'Content-Type': 'application/json'
    }
  };

  if (token) {
    config.headers['Authorization'] = `Token ${token}`;
  }

  return config;
};*/
