import React from 'react'
import { useSelector } from 'react-redux'
import { List, Avatar, Space } from 'antd'
import { MessageOutlined, LikeOutlined, StarOutlined } from '@ant-design/icons'
import Loading from "./Loading"



const IconText = ({ icon, text }) => (
  <Space>
    {React.createElement(icon)}
    {text}
  </Space>
)

const Post = (props)=> {
    return (
        <div>
        {
            useSelector(state =>state.post.postLoading) ?
                <Loading/>
            :

                <List
                    itemLayout="vertical"
                    size="large"
                    pagination={{
                        onChange: page => {
                            console.log(page);
                        },
                        pageSize: 3,
                    }}
                    dataSource={props.data}
                    renderItem={item => (
                        <List.Item
                            key={item.id}
                            actions={[
                                <IconText icon={StarOutlined} text="156" key="list-vertical-star-o"/>,
                                <IconText icon={LikeOutlined} text="156" key="list-vertical-like-o"/>,
                                <IconText icon={MessageOutlined} text="2" key="list-vertical-message"/>,
                            ]}
                            extra={
                                <img
                                    width={272}
                                    alt="post image"
                                    src={item.image}
                                />
                            }
                        >
                            <List.Item.Meta
                                avatar={<Avatar src={item.avatar}/>}
                                title={<a href={`/posts/${item.id}`}>{item.posted_by}</a>}
                                description={item.description}
                            />
                            <a href={`/posts/${item.id}`}>{item.content}</a>
                        </List.Item>
                    )}
                />
        }
        </div>
    )

}

export default Post



