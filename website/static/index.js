//delete note in javascript
/*
    going to take the nateId to be passed and going to send to the deleteNote endpoint
    after it gets the request, it is going to reload the window
*/
function deleteNote(noteId){
    fetch ("/delete-note", { //fetch to make a post request
        method: "POST",
        body: JSON.stringify({noteId: noteId}), //convert object into string format
    }) .then((_res)=>{
        window.location.href = "/"; //reload the window, rederect to the homepagec
    });

}