import React from 'react';
import Fetch from 'react-fetch';

const divStyle = {
    color: 'purple',
    backgroundImage: 'url(https://static.brusheezy.com/system/resources/previews/000/047/667/non_2x/fireball-explosion-psd-photoshop-psds.jpg)',
    height: '200px',
};


class Welcome extends React.Component {

    constructor(props) {
        super(props);
        this.state = {book_list: ['']};
    }

    componentDidMount() {
        fetch("http://127.0.0.1:8000/api/v1/books")
          .then(res => res.json())
          .then(result =>
            this.setState({
              book_list: result
            })
          )
    }

  render() {

      let boeken_lijst = [];

      for (var i = 0, len = this.state.book_list.length; i < len; ++i) {
              boeken_lijst.push(this.state.book_list[i])

      }
      console.log(boeken_lijst)



      return (
          <div>
              <h1 style={divStyle}>Yo ik ben React en ik Render dit </h1>
              <ul>
                  {this.state.book_list.map(book =>
                      <li key={book.id}>
                      ID: {book.id}<br/>
                      Title: {book.title}<br/>
                      Publisher_city: {book.publisher_city}<br/>
                  </li>)}
              </ul>
          </div>
      )
  }
}

export default Welcome




