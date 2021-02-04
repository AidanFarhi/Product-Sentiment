import React, { useState } from 'react'

export default function App() {

    const [url, setUrl] = useState('')

    const handleChange = ev => setUrl(ev.target.value)

    const handleSubmit = async(ev) => {
        ev.preventDefault()
        try {
            // This is where we will send the url to the server and wait for analysis
            console.log(url)
        } catch(er) { console.log(er) }
    }

    return (
        <div>
            <h3>Enter A Product URL</h3>
            <form onSubmit={handleSubmit}>
                <input type="text" placeholder="Enter Url..." onChange={handleChange} />
                <br></br>
                <input type="submit" value="Get Analysis"></input>
            </form>
            <h2>{url}</h2>
        </div>
    )
}