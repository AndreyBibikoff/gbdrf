import React from 'react'


const TodoItem = ({todo}) => {
   return (
       <tr>
           <td>
               {todo.project.name}
           </td>
               {todo.text}
           <td>
               {todo.created}
           </td>
           <td>
               {todo.updated}
           </td>
           <td>
               {todo.is_active}
           </td>
           <td>
               {todo.user.username}
           </td>
       </tr>
   )
}
const ToDoList = ({todos}) => {
   return (
       <table border={1}>
           <th>
               Project
           </th>
           <th>
               Text
           </th>
           <th>
               Created
           </th>
           <th>
               Updated
           </th>
            <th>
               Active
           </th>
            <th>
               User
           </th>
           {todos.map((todo) => <TodoItem todo={todo} />)}
       </table>
   )
}


export default ToDoList
