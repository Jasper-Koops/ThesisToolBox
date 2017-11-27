import React from 'react';

class BookCreate extends React.Component {

    constructor(props) {
        super(props);

        this.state = {
          post_url: '/api/v1/books/create/',
          title_text: '',
          title: '',
          book_info : {
            'titlee': '',
            'publication_date': '',
            'source_type': '',
            'publisher_name': '',
            'publisher_city': '',
            'user': '',
          }
        };

        this.SubmitBook = this.SubmitBook.bind(this);
        this.changeTitle = this.changeTitle.bind(this);
    }


    changeTitle(e) {
      this.setState({title_text: e.target.value });
    }


    SubmitBook (e) {

        e.preventDefault();

        if (!this.state.title_text.length) {
            return;
        }
        const title = this.state.title_text;

        this.setState(prevState => ({
            title: title
        }));

        function getCookie(name) {
            if (!document.cookie) {
              return null;
            }
            const token = document.cookie.split(';')
              .map(c => c.trim())
              .filter(c => c.startsWith(name + '='));

            if (token.length === 0) {
              return null;
            }
            return decodeURIComponent(token[0].split('=')[1]);
          }

        const csrftoken = getCookie('csrftoken')
        console.log(csrftoken)


        fetch(this.state.post_url, {
            credentials: 'include',
            method: 'POST',
            mode: 'same-origin',
            headers: {
              'Accept': 'application/json',
              'Content-Type': 'application/json',
              'X-CSRFToken': csrftoken
            },
            body: JSON.stringify({
              title: title,
              notes: 1,
              publication_date: '1800-01-01',
              publisher_city: 'amsterdam',
              publisher_name: 'fred',


            })
           })

    }


    render () {

        return (
            <div>
                <form onSubmit={ this.SubmitBook }>
                    <input onChange={this.changeTitle} />
                    <button>Add Book</button>
                </form>
            </div>
        )
    }


}

export default BookCreate