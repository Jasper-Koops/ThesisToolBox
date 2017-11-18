import React from 'react';
import Fetch from 'react-fetch';

const divStyle = {
    color: 'purple',
    backgroundImage: 'url(https://static.brusheezy.com/system/resources/previews/000/047/667/non_2x/fireball-explosion-psd-photoshop-psds.jpg)',
    height: '200px',
};


let list = <Fetch url='http://127.0.0.1:8000/api/v1/books' />;
class Welcome extends React.Component {

  render() {
      return (
          <div>
              <h1 style={divStyle}>Yo ik ben React en ik Render dit </h1>
              <p>{JSON.stringify(list)}</p>
          </div>
      )
  }
}

export default Welcome