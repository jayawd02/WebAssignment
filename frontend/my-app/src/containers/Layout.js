import React from 'react'
import {Link} from "react-router-dom"
import { Layout, Menu, Breadcrumb } from 'antd';
import { UserOutlined, LaptopOutlined, NotificationOutlined } from '@ant-design/icons';

const { SubMenu } = Menu;
const { Header, Content, Sider } = Layout;

const CustomLayout = (props) =>{
    return (
    <Layout>
        <Header className="header">
          <div className="logo" />
          <Menu theme="dark" mode="horizontal" defaultSelectedKeys={['2']}>
            <Menu.Item key="1">Profile</Menu.Item>
            <Menu.Item key="2">Logout</Menu.Item>
          </Menu>
        </Header>
        <Layout>
          <Sider width={200} className="site-layout-background">
            <Menu
              mode="inline"
              defaultSelectedKeys={['1']}
              defaultOpenKeys={['sub1']}
              style={{ height: '100%', borderRight: 0 }}
            >
              <SubMenu key="sub1" icon={<UserOutlined />} title="My Plans">
                <Menu.Item key="1">Workout Plan</Menu.Item>
                <Menu.Item key="2">Meal Plan</Menu.Item>
              </SubMenu>
              <SubMenu key="sub2" icon={<LaptopOutlined />} title="Gallery">
                  <Menu.Item key="3"><Link to="/posts">All Posts</Link></Menu.Item>
                  <Menu.Item key="4"><Link to="/videos">All Videos</Link></Menu.Item>
                  <Menu.Item key="5"><Link to="/recipes">All Recipes</Link></Menu.Item>
              </SubMenu>
              <SubMenu key="sub3" icon={<NotificationOutlined />} title="Create New">
                  <Menu.Item key="6"><Link to="/post/new">Add New Post</Link></Menu.Item>
                <Menu.Item key="7">Add New Video</Menu.Item>
                <Menu.Item key="8">Add New Recipe</Menu.Item>
              </SubMenu>
            </Menu>
          </Sider>
          <Layout style={{ padding: '0 24px 24px' }}>
            <Breadcrumb style={{ margin: '16px 0' }}>
              <Breadcrumb.Item>Home</Breadcrumb.Item>
              <Breadcrumb.Item>List</Breadcrumb.Item>
              <Breadcrumb.Item>App</Breadcrumb.Item>
            </Breadcrumb>
            <Content
              className="site-layout-background"
              style={{
                padding: 24,
                margin: 0,
                minHeight: 280,
              }}
            >
                {props.children}
            </Content>
          </Layout>
        </Layout>
      </Layout>
    )
}
export default CustomLayout

