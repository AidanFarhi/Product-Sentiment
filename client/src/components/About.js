import React from 'react'
import '../styles/About.css'

export default function About() {
    return (
        <div id='about-main-div'>
            <div id='info'>
                <h4>
                    How do I use this app?
                </h4>
                <ol>
                    <li>Click on a product on Amazon.com</li>
                    <li>Copy the full URL</li>
                    <li>Paste copied URL into the app and click analyze</li>
                </ol>
                <h4>
                    How are you getting the score?
                </h4>
                <p>
                    The score is based on a quick look at what people are actually saying
                    about the product. The app looks at up to 150 reviews and calculates
                    a value based on specific key words found. If you are a software developer
                    (or just curious) you can take a deeper look at what's going on here: &nbsp;
                    <a href='https://github.com/AidanFarhi/Product-Sentiment/blob/master/server/page_analyzer/Analyzer.py' target='blank'>
                        Source Code
                    </a>
                </p>
                <h4>
                    Does this app work for other sites?
                </h4>
                <p>
                    Unfortunately no. In the future, the developer may add support for other sites.
                </p>
            </div>
        </div>
    )
}