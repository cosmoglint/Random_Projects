function clickerFunction(){
  // alert("hi");
  let url = "https://api.chucknorris.io/jokes/random";
  const options = {
    method: 'GET'
  }
  fetch(url,options).then(response => response.json()).then(data => {alert(data.value); console.log(data)});
}
