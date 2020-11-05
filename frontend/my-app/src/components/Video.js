import React from 'react'
import { List, Avatar, Space } from 'antd'


const Video= (props)=>{

    return (
        <div>

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
                extra={<a href={item.link}>
                  <img
                    width={272}
                    alt="post image"
                    src={item.thumbnail}
                  />
                </a>}
              >
                <List.Item.Meta
                  avatar={<Avatar src={item.avatar} />}
                  title={<a href={`/videos/${item.id}`}>{item.title}</a>}
                  description={item.description}
                />
                  {item.type}
              </List.Item>
            )}
        />
        </div>)
}

/*<h3>{video.title}</h3>
            <div>Description {video.description}</div>
            <div>Type: {video.type}</div>
            <div> <img src={video.thumbnail} /></div>
            <div> {video.link}</div>*/
export default Video