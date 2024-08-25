// Initiate the delete button

//take the note id that we passed and it's going to send a post request to the delete
//note endpoint then after it gets a response from the get request specifically so 
//window.location.href equals slash just means redirect us to the home page which in 
//turn will just redirect the page all or in other words refresh the page

function deleteNote(noteId) {
    //send request to server to delete-note
    fetch("/delete-note", {
      method: "POST", //want to send a post request
      body: JSON.stringify({ noteId: noteId }),
    }).then((_res) => {
      window.location.href = "/";
    });
  }