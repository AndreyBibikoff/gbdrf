import React from 'react';
import logo from './logo.svg';
import './App.css';
import axios from 'axios'
import UserList from "./components/User";
import ProjectList from "./components/Projects";
import ToDoList from "./components/ToDo";
import {HashRouter, Route, Link} from 'react-router-dom'


class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'users': [],
            'projects': [],
            'todos': []
        }
    }


    componentDidMount() {
        axios.get('http://127.0.0.1:8000/api/users/')
            .then(response => {
                const users = response.data.results
                this.setState(
                    {
                        'users': users,
                    }
                )
            }).catch(error => console.log(error))
        axios.get('http://127.0.0.1:8000/api/project/')
            .then(response => {
                const projects = response.data.results
                this.setState(
                    {
                        'projects': projects,
                    }
                )
            }).catch(error => console.log(error))

        axios.get('http://127.0.0.1:8000/api/todo/')
            .then(response => {
                const todos = response.data.results
                this.setState(
                    {
                        'todos': todos,
                    }
                )
            }).catch(error => console.log(error))
    }

    render() {
        return (
            <div className="App">
                <HashRouter>
                    <nav>
                        <ul>
                            <li>
                                <Link to='/'>Users</Link>
                            </li>
                            <li>
                                <Link to='/projects'>Projects</Link>
                            </li>
                            <li>
                                <Link to='/todo'>ToDo's</Link>
                            </li>
                        </ul>
                    </nav>
                    <Route exact path='/' component={() => <UserList users={this.state.users}/>}/>
                    <Route exact path='/projects' component={() => <ProjectList projects={this.state.projects}/>}/>
                    <Route exact path='/todo' component={() => <ToDoList todos={this.state.todos}/>}/>
                </HashRouter>
            </div>
        )
    }
}
export default App;
//        return (
//            <div>
//                <UserList users={this.state.users} />
//                <ProjectList projects={this.state.projects}/>
//                <ToDoList todos={this.state.todos}/>
//            </div>
//
//
//        )
//    }
// }


// import logo from './logo.svg';
// import './App.css';
//
// function App() {
//   return (
//     <div className="App">
//       <header className="App-header">
//         <img src={logo} className="App-logo" alt="logo" />
//         <p>
//           Edit <code>src/App.js</code> and save to reload.
//         </p>
//         <a
//           className="App-link"
//           href="https://reactjs.org"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           Learn React
//         </a>
//       </header>
//     </div>
//   );
// }
//
//
