import React from 'react'
import { List, Avatar, Space } from 'antd'

const Recipe = (props)=>{

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
                extra={
                  <img width={272} alt="recipe image" src={item.recipe_image}/>
               }
              >
                <List.Item.Meta
                  avatar={<Avatar src={item.avatar} />}
                  title={<a href={`/recipes/${item.id}`}>{item.name}</a>}
                  description={item.description}
                />
                  Type: {item.type}  Category: {item.category} Ingredients: {item.ingredients} Prep Time: {item.prep_time}
              </List.Item>
            )}
        />
        </div>)
}

export default Recipe