(this.webpackJsonpclient=this.webpackJsonpclient||[]).push([[0],{32:function(e,t,r){},33:function(e,t,r){},34:function(e,t,r){"use strict";r.r(t);var n=r(1),s=r(17),c=r.n(s),a=r(8),i=r(0);function l(){return Object(i.jsxs)("div",{id:"nav-bar",children:[Object(i.jsx)("img",{id:"logo",alt:"lol",src:"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAIAAAAlC+aJAAAABmJLR0QA/wD/AP+gvaeTAAAENUlEQVRoge2awUs6QRTHZ9cgK4xqC1wJgjChYye9dXDdDhF2CjwU0qFLF92NDlkZldAhyo5dSoxwiSjq0EGNbmn4BwRBEF0sQsqioIX0d1hY1h21cTVXf/g5iDPOzL7vzHszb3fFPj4+QD2Dq21AuTQEqE1DgNo0BKjOh4RUKuVyufR6vdpG5YckSbfbnUqlpDbnCHC73Wob+TsMw0htxqQnsclkSiaT0WjUbDaraGIhYrEYTdMkSd7d3YmVOQJ0Oh0AoJaTC9jCug/ihoCyCYfD3d3dOgiaplG6qy8AwzAMw+D6WCyG0l19ATab7eXlRdgT397e7HZ7Sd2rIYDn+aWlpYGBAZPJtLy8zPN8oZYMw5ydnXV2dqIPXg0B6+vrfr//6ekpmUxub2/7fL68zTY2Nvb29lpaWo6OjtAHr4YAjuMAANFoNBwOAwBCoRDcJhAI+Hw+jUazv79vsVjQB6+SCwEAMplMNpsVvsgaXFxcuFwuAIDf7x8dHS1p8LIEIDq3MKM0TY+MjAAAXl9fg8Gg+Gs8Hnc6nT8/Px6Px+l0CpVarVar1SIZkZPZQTXFkSV/sjRL4Pj4GMdxHMd7enoIgrBarUJjq9Xa1dWl1+uF7GB6elra6+Tk5PT0FB4NtrCsXEhM/jKZDJxmAQDu7++Hh4fT6bTX652bmxMqDw4OXC6XdLmGhoaurq40Gs2vV6xwLiT6dF7n/vz8dDgc6XTabrezLCvWT05OChulGNaPj48o1udFuYBIJPL+/g4KOHc2m52Zmbm9vR0cHNzd3ZWdtTiOA4ny5uZmxWYoFBAIBCYmJr6+vsxmM0EQgnPzPD87Ozs+Pt7X19fb23t+ft7R0cFxXFtbm6y7w+EAEuVCURlNpXbIZrOrq6ubm5sAgPn5+cXFRXF2g8Gg2+2+vLwUG4+NjfX398ODeDweAEAoFMIwzOFwLCwsKDQf8YaG5/m1tTWO476/v41GYyKRaGpq2tnZmZqakrU0Go3Pz89iWBME8fDwoNg4GNhCpBUQcgHheyKRaG1tPTw8pCgKbllB50YEKQZkuUB7e3te64FS56YoCr4fsNlsKH1LiAFxXoVpzosy5765uYEr4/E4Sl+kGPB6vVtbW2KRZdmVlRWU0RGBr1vIEoUxUMFNo+L8+WMViqJgD7FYLJFIpMh10Vfgz9PpcvwbhZIPMmXAsyt8lo/6N/VlUtYK5PVvROA1UUZZK6DY+gpSwgoUmu/iu0elfL0QJaxALcw3TMkxUM3ZRaHud6E8J3HtU9WT+K/JEwOVzYUqC+wjdb8CxQRQFCW9LaqRooxi6XQNFv/Dt5TFDjKLxSJ9olYjRRn/14tukiQB8uvB6nN9fQ0AMBgMObXSZ+0Mw6hjWimwLJvzxkBaSKVSDMMI61CDGAwGlmVlf7fJiYF6pO630YYAtWkIUJuGALX5B4He8nkgOxTGAAAAAElFTkSuQmCC"}),Object(i.jsx)(a.b,{id:"main-link",to:"/",children:Object(i.jsx)("h3",{id:"nav-bar-header",children:"Amazon Product Analyzer"})}),Object(i.jsx)(a.b,{id:"about-link",to:"/about",children:"How does it work?"})]})}var o=r(2),d=r(15),j=r.n(d),u=r(19),b=r(10),h=r(20),O=r.n(h);function x(){return Object(i.jsx)("div",{id:"error-div",children:Object(i.jsx)("h3",{children:"Sorry, could not get results for that product."})})}r(32);function p(){var e=Object(n.useState)(""),t=Object(b.a)(e,2),r=t[0],s=t[1],c=Object(n.useState)(!1),a=Object(b.a)(c,2),l=a[0],o=a[1],d=Object(n.useState)(!1),h=Object(b.a)(d,2),p=h[0],A=h[1],v=Object(n.useState)({score:null,time:null,totalReviews:null,color:null}),m=Object(b.a)(v,2),f=m[0],w=m[1],g=function(){var e=Object(u.a)(j.a.mark((function e(t){var n,s,c,a;return j.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return t.preventDefault(),e.prev=1,A(!1),o(!0),w({score:null,time:null,totalReviews:null,color:null}),n={method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({url:r})},e.next=8,fetch("/analyze",n);case 8:if((s=e.sent).ok){e.next=13;break}return A(!0),o(!1),e.abrupt("return");case 13:return e.next=15,s.json();case 15:c=e.sent,i=c.score,a=i<65?"red":i<75?"orange":i<85?"green":"#64e764",o(!1),w({score:c.score,time:c.time_taken,totalReviews:c.reviews_scraped,color:a}),e.next=24;break;case 21:e.prev=21,e.t0=e.catch(1),console.log(e.t0);case 24:case"end":return e.stop()}var i}),e,null,[[1,21]])})));return function(t){return e.apply(this,arguments)}}();return Object(i.jsxs)("div",{id:"main",children:[Object(i.jsxs)("div",{id:"url-form",children:[Object(i.jsx)("h3",{id:"form-header",children:"Enter a product URL to analyze"}),Object(i.jsxs)("form",{id:"form",onSubmit:g,children:[Object(i.jsx)("input",{id:"url-input",type:"text",placeholder:"Enter Url...",onChange:function(e){return s(e.target.value)}}),Object(i.jsx)("br",{}),Object(i.jsx)("input",{id:"submit-button",type:"submit",value:"Get Analysis"})]})]}),Object(i.jsxs)("div",{id:"results-main-div",children:[p?Object(i.jsx)(x,{}):null,l?Object(i.jsxs)("div",{id:"loading-div",children:[Object(i.jsx)("h2",{id:"loading-header",children:"Analyzing Product..."}),Object(i.jsx)(O.a,{type:"bars",color:"#10c200"})]}):null,null==f.score?null:Object(i.jsxs)("div",{id:"results",children:[Object(i.jsxs)("div",{className:"result",id:"score-div",children:[Object(i.jsx)("h2",{children:"Total Score"}),f.score>=0?Object(i.jsxs)("span",{className:"result-span",style:{color:f.color},children:[" ",f.score,"%"]}):"No Score Available"]}),Object(i.jsxs)("div",{className:"result",id:"time-div",children:[Object(i.jsx)("h2",{children:"Time Taken"}),Object(i.jsxs)("span",{className:"result-span",children:[f.time," seconds"]})]}),Object(i.jsxs)("div",{className:"result",id:"total-reviews-div",children:[Object(i.jsx)("h2",{children:"Total Reviews Analyzed"}),Object(i.jsx)("span",{className:"result-span",children:f.totalReviews})]})]})]})]})}r(33);function A(){return Object(i.jsx)("div",{id:"about-main-div",children:Object(i.jsxs)("div",{id:"info",children:[Object(i.jsx)("h4",{children:"How do I use this app?"}),Object(i.jsxs)("ol",{children:[Object(i.jsx)("li",{children:"Click on a product on Amazon.com"}),Object(i.jsx)("li",{children:"Copy the full URL"}),Object(i.jsx)("li",{children:"Paste copied URL into the app and click analyze"})]}),Object(i.jsx)("h4",{children:"How are you getting the score?"}),Object(i.jsxs)("p",{children:["The score is based on a quick look at what people are actually saying about the product. The app looks at up to 150 reviews and calculates a value based on specific key words/phrases found. If you are a software developer (or just curious) you can take a deeper look at what's going on here: \xa0",Object(i.jsx)("a",{href:"https://github.com/AidanFarhi/Product-Sentiment/blob/master/server/page_analyzer/Analyzer.py",target:"blank",children:"Source Code"})]}),Object(i.jsx)("h4",{children:"Does this app work for other sites?"}),Object(i.jsx)("p",{children:"Unfortunately no. In the future, the developer may add support for other sites."})]})})}function v(){return Object(i.jsxs)(o.c,{children:[Object(i.jsx)(o.a,{exact:!0,path:"/",children:Object(i.jsx)(p,{})}),Object(i.jsx)(o.a,{exact:!0,path:"/about",children:Object(i.jsx)(A,{})})]})}function m(){return Object(i.jsxs)("div",{children:[Object(i.jsx)(l,{}),Object(i.jsx)(v,{})]})}c.a.render(Object(i.jsx)(a.a,{children:Object(i.jsx)(m,{})}),document.getElementById("root"))}},[[34,1,2]]]);
//# sourceMappingURL=main.c1aa9536.chunk.js.map