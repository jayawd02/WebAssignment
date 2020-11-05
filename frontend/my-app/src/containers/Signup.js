import React, { useState } from 'react'
import {Form, Input, Button} from 'antd'
import {NavLink} from "react-router-dom"
import * as actions from "../store/actions/auth"
import { connect } from 'react-redux'


const formItemLayout = {labelCol: {xs: {span: 24,}, sm: {span: 8,},}, wrapperCol: {xs: {span: 24,}, sm: {span: 16,},},}
const tailFormItemLayout = {wrapperCol: {xs: {span: 24, offset: 0,}, sm: {span: 16, offset: 8,},},}

const Signup =(props)=>{
    const [form] = Form.useForm()
    const onFinish = (values) => {
        console.log('Received values of form: ', values)
        props.onAuth(values.username,values.email, values.password1,values.password2)
        props.history.push('/')
    }


        return (
            <Form {...formItemLayout} form={form} name="register" onFinish={onFinish} scrollToFirstError>
                <Form.Item label="Username" name="username" rules={[{ required: true, message: 'Please input your username!' }]}>
                    <Input />
                </Form.Item>

                <Form.Item name="email" label="E-mail" rules={[ {type: 'email', message: 'The input is not valid E-mail!',}, {required: true, message: 'Please input your E-mail!',},]}>
                    <Input />
                </Form.Item>

                <Form.Item name="password1" label="Password" rules={[{required: true, message: 'Please input your password!',},]} hasFeedback>
                    <Input.Password />
                </Form.Item>

                <Form.Item name="password2" label="Confirm Password" dependencies={['password']} hasFeedback rules={[{required: true, message: 'Please confirm your password!',}, ({ getFieldValue }) => ({validator(rule, value) {if (!value || getFieldValue('password1') === value) {return Promise.resolve();}return Promise.reject('The two passwords that you entered do not match!');},}),]}>
                    <Input.Password />
                </Form.Item>
                <Form.Item {...tailFormItemLayout}>
                    <Button type="primary" htmlType="submit"> Signup </Button>
                    Or
                    <NavLink style={{marginRight: '10px'}} to='/login/'>
                        Login
                    </NavLink>
                </Form.Item>
            </Form>
        )

}

const mapStateToProps = (state) => {
    return {
        loading: state.loading,
        error: state.error
    }
}

const mapDispatchToProps = dispatch => {
    return {
        onAuth: (username,email, password1, password2) => dispatch(actions.authSignup(username,email, password1, password2))
    }
}

export default connect(mapStateToProps, mapDispatchToProps)(Signup)