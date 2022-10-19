#!/usr/bin/node
/* displays the status code of a GET request */

function makeRequest() {
  fetch(process.argv.slice(2)[0])
    .then(response => {
      console.log('response.status: ', response.status); 
      console.log(response);
    })
    .catch(err => {
      console.log(err);
    });
}
