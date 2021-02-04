import React, { useState, useEffect } from 'react'

export default function App() {
    const [greeting, setGreeting] = useState('')

    const getHello = async() => {
        try {
            const res = await fetch('/hello')
            const data = await res.json()
            setGreeting(data.res)
        } catch(er) { console.log(er) }
    }

    useEffect (() => {
        getHello()
    }, [])

    return (
        <div>
            {greeting == '' ? 'getting greeting...' : greeting}
        </div>
    )
}