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

const Article = (props)=> {

    return (
        <div>

        {
            useSelector(state =>state.article.articleLoading) ?
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

                        >
                            <List.Item.Meta
                                avatar={<Avatar src={item.avatar}/>}
                                title={<a href={`/articles/${item.id}`}>{item.title}</a>}
                                description={item.content}
                            />

                        </List.Item>
                    )}
                />
        }
        </div>
    )

}


export default Article



