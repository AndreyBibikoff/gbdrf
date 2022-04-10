import React from 'react';
import logo from './logo.svg';
import './App.css';
import axios from 'axios'
import UserList from "./components/User";
import ProjectList from "./components/Projects";
import ToDoList from "./components/ToDo";
import {HashRouter, Route, Link} from 'react-router-dom'
import LoginForm from "./components/Auth";
import Cookies from 'universal-cookie';


class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'users': [],
            'projects': [],
            'todos': [],
            'token': ''
        }
    }

    set_token(token) {
        const cookies = new Cookies()
        cookies.set('token', token)
        this.setState({'token': token})
    }

    is_authenticated() {
        return this.state.token !== ''
    }

    logout() {
        this.set_token('')
    }

    get_token_from_cookie() {
        const cookies = new Cookies()
        const token = cookies.get('token')
        this.setState({'token': token})
    }
    get_token(username, password) {
        axios.post('http://127.0.0.1:8000/api-token-auth/', {username: username, password: password})
            .then(response => {
                this.set_token(response.data['token'])
    }   ).catch(error => alert('Неверный логин или пароль'))
    }

    load_data() {
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

    componentDidMount() {
        this.get_token_from_cookie()
        this.load_data()
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
                            <li>
                                {this.is_authenticated() ? <button onClick={()=>this.logout()}>Logout</button> : <Link to='/login'>Login</Link>}
                            </li>
                        </ul>
                    </nav>
                    <Route exact path='/' component={() => <UserList users={this.state.users}/>}/>
                    <Route exact path='/projects' component={() => <ProjectList projects={this.state.projects}/>}/>
                    <Route exact path='/todo' component={() => <ToDoList todos={this.state.todos}/>}/>
                    <Route exact path='/login' component={() => <LoginForm get_token={(username, password) => this.get_token(username, password)} />} />
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
