import React from 'react'
import { Form, Input, Button } from 'antd'
import { connect } from 'react-redux'
import { NavLink } from 'react-router-dom'
import * as actions from '../redux/auth/authActions'
import Loading from "../components/Loading"



const Login =(props) => {
    let errorMessage = null

    const onFinish = values => {
        console.log('Success:')
        props.onAuth(values.username, values.password)
        props.history.push('/')
    }

    const onFinishFailed = errorInfo => {
        console.log('Failed:', errorInfo)
        errorMessage = (
            <p>{props.error.message}</p>
        )
      }

      return (
        <div>
            {errorMessage}
            {
                props.loading ?

                <Loading/>

                :

                <Form onFinish={onFinish} onFinishFailed={onFinishFailed} className="login-form">

                    <Form.Item label="Username" name="username" rules={[{ required: true, message: 'Please input your username!' }]}>
                        <Input />
                    </Form.Item>

                    <Form.Item label="Password" name="password" rules={[{ required: true, message: 'Please input your password!' }]}>
                        <Input.Password />
                    </Form.Item>

                    <Form.Item>
                    <Button type="primary" htmlType="submit" style={{marginRight: '10px'}}>
                        Login
                    </Button>
                    Or
                    <NavLink
                        style={{marginRight: '10px'}}
                        to='/signup/'> signup
                    </NavLink>
                    </Form.Item>
                </Form>
            }
      </div>
    )

}

const mapStateToProps = (state) => {
    return {
        loading: state.auth.loading,
        error: state.auth.error
    }
}

const mapDispatchToProps = dispatch => {
    return {
        onAuth: (username, password) => dispatch(actions.authLogin(username, password))
    }
}

export default connect(mapStateToProps, mapDispatchToProps)(Login)