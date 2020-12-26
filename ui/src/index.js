import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import './styles/index.css';
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import Home from './views/Home';

function App () {
    return (
        <div className="app">
            <Router>
                <Switch>
                    <Route exact path="/" component={Home} />
                </Switch>
            </ Router>
        </div>
    );
}

ReactDOM.render(<App />, document.getElementById('root'));