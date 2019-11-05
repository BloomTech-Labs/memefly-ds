function main() {
  console.log("main function");
  console.log("ajax request to the resource which will require cors enabled");
  $.ajax({
    dataType: "json",
    url: "http://127.0.0.1:8000/",
    success: function(data) {
      console.log("log response on success");
      console.log(data);
    }
  });
}
