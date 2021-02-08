import React, { useState } from 'react'
import ReactLoading from 'react-loading'
import '../src/styles/App.css'

export default function App() {

    const [url, setUrl] = useState('')
    const [loading, setLoading] = useState(false)
    const [results, setResults] = useState(
        {
            score: null,
            time: null,
            totalReviews: null,
            color: null
        }
    )

    const handleChange = ev => setUrl(ev.target.value)

    const calculateColor = score => {
        let color = ''
        if (score < 65) color = 'red'
        else if (score < 75) color = 'orange'
        else if (score < 85) color = 'green'
        else color = 'light-green'
        return color
    }

    const handleSubmit = async(ev) => {
        ev.preventDefault()
        try {
            setLoading(true)
            // This is where we will send the url to the server and wait for analysis
            const requestOptions = {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({url: url})
            }
            const res = await fetch('/analyze', requestOptions)
            const data = await res.json()
            const color = calculateColor(data.score)
            setLoading(false)
            setResults(
                {
                    score: data.score,
                    time: data.time_taken,
                    totalReviews: data.reviews_scraped,
                    color: color
                }
            )
            console.log(data)
        } catch(er) { console.log(er) }
    }

    return (
        <div id='main'> 
            <div id='url-form'>
            <h3 id='header'>Enter A Product URL</h3>
                <form onSubmit={handleSubmit}>
                    <input id='url-input' type="text" placeholder="Enter Url..." onChange={handleChange} />
                    <br></br>
                    <input type="submit" value="Get Analysis"></input>
                </form>
            </div>
            <div id='results-main-div'>
                <div id='loading-div'>
                    {loading ? "Analyzing Product..." : null}
                    {loading ? <ReactLoading type={'bars'} color={'grey'} /> : null}
                </div>
                {  // Conditionally show this div when results have been fetched successfully
                results.score == null ? null : 
                <div id='results'>
                    <h2>Total Score:<span style={{color: results.color}}> {results.score}%</span></h2>
                    <h2>Time Taken: {results.time} seconds</h2>
                    <h2>Total Reviews Analyzed: {results.totalReviews}</h2>
                </div>
                }
            </div>
        </div>
    )
}