import React from 'react'
import {Route, Switch} from 'react-router-dom'
import Main from './components/Main'
import About from './components/About'

export default function Routes() {
    return (
        <Switch>
            <Route exact path='/'>
                <Main />
            </Route>
            <Route exact path='/about'>
                <About />
            </Route>
        </Switch>
    )
}