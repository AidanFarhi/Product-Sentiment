import React from 'react'
import { Link } from 'react-router-dom'
import logo from '../styles/analyze.png'

export default function NavBar() {
    return (
        <div id='nav-bar'>
            <img id='logo' alt='lol' src={logo}/>
            <Link id='main-link' to='/'>
                <h3 id='nav-bar-header'>Amazon Product Analyzer</h3>
            </Link>
            <Link id='about-link' to='/about'>How does it work?</Link>
        </div>
    )
}