import React,{Component} from 'react'
import {Link, withRouter} from "react-router-dom"
import { Layout, Menu} from 'antd';
import { UserOutlined, LaptopOutlined, CameraOutlined,MessageOutlined  } from '@ant-design/icons';
import * as actions from '../redux/auth/authActions'
import { connect } from 'react-redux'

const { SubMenu } = Menu;
const { Header, Content, Sider } = Layout

class CustomLayout extends Component{
    render(){
       return (
          <Layout>
            <Header className="header">
              <div className="logo" />
              <Menu theme="dark" mode="horizontal" defaultSelectedKeys={['1']}>
                  <Menu.Item key="1"><Link to="/">Home</Link></Menu.Item>
                  {
                      this.props.isAuthenticated ?
                          <Menu.Item key="2"><Link to={`/profile/1`}>Profile</Link></Menu.Item>
                      :
                          <Menu.Item key="3"><Link to="/signup">Register</Link></Menu.Item>
                  }

                  {
                      this.props.isAuthenticated ?
                          <Menu.Item key="4" onClick={this.props.logout}>Logout</Menu.Item>
                      :
                          <Menu.Item key="5"><Link to="/login">Login</Link></Menu.Item>

                  }


              </Menu>
            </Header>
            <Layout>
              <Sider width={200} className="site-layout-background">
                <Menu mode="inline" defaultSelectedKeys={['1']} defaultOpenKeys={['sub1']} style={{ height: '100%', borderRight: 0 }}>
                  <SubMenu key="sub1" icon={<UserOutlined />} title="My Plans">
                    <Menu.Item key="6">Workout Plan</Menu.Item>
                    <Menu.Item key="7">Meal Plan</Menu.Item>
                  </SubMenu>
                  <Menu.Item key="8" icon={<MessageOutlined />}><Link to="/posts">Posts</Link></Menu.Item>
                  <Menu.Item key="9" icon={<CameraOutlined />}><Link to="/videos">Videos</Link></Menu.Item>
                  <Menu.Item key="10" icon={<LaptopOutlined />}><Link to="/recipes">Recipes</Link></Menu.Item>
                    <Menu.Item key="11" icon={<LaptopOutlined />}><Link to="/articles">Article</Link></Menu.Item>

                </Menu>
              </Sider>
              <Layout style={{ padding: '0 24px 24px' }}>

                <Content
                  className="site-layout-background"
                  style={{
                    padding: 24,
                    margin: 0,
                    minHeight: 280,
                  }}
                >
                    {this.props.children}
                </Content>
              </Layout>
            </Layout>
          </Layout>
       )
    }
}

const mapDispatchToProps = dispatch => {
    return {
        logout: () => dispatch(actions.logout())
    }
}
export default withRouter(connect(null, mapDispatchToProps)(CustomLayout))