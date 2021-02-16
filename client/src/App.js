import React, { useState } from 'react'
import ReactLoading from 'react-loading'
import '../src/styles/App.css'
import logo from '../src/styles/analyze.png'

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
        else color = '#64e764'
        return color
    }

    const handleSubmit = async(ev) => {
        ev.preventDefault()
        try {
            setLoading(true)
            setResults({score: null, time: null, totalReviews: null, color: null})
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
            <div id='nav-bar'>
                <img id='logo' alt='lol' src={logo}/>
                <h3 id='nav-bar-header'>Amazon Product Analyzer</h3>
            </div>
            <div id='url-form'>
                <h3 id='form-header'>Enter a product URL to analyze</h3>
                <form id='form' onSubmit={handleSubmit}>
                    <input id='url-input' type="text" placeholder="Enter Url..." onChange={handleChange} />
                    <br></br>
                    <input id='submit-button' type="submit" value="Get Analysis"></input>
                </form>
            </div>
            <div id='results-main-div'>
                {loading ? 
                    <div id='loading-div'>
                        <h2 id='loading-header'>Analyzing Product...</h2>
                        <ReactLoading type={'bars'} color={'#10c200'} />
                    </div>
                : null
                }
                {// Conditionally show this div when results have been fetched successfully
                results.score == null ? null : 
                <div id='results'>
                    <div className='result' id='score-div'>
                        <h2>Total Score</h2>
                        <span className='result-span' style={{color: results.color}}> {results.score}%</span>
                    </div>
                    <div className='result' id='time-div'>
                        <h2>Time Taken</h2>
                        <span className='result-span'>{results.time} seconds</span>
                    </div>
                    <div className='result' id='total-reviews-div'>
                        <h2>Total Reviews Analyzed</h2> 
                        <span className='result-span'>{results.totalReviews}</span>
                    </div>
                </div>
                }
            </div>
        </div>
    )
}