let socket;

function addMessage(message) {
  let d = new Date();
  $("#chat").val(
    $("#chat").val() + `[${d.toLocaleTimeString()}] ${message}\n`
  );
  $("#chat").scrollTop($("#chat")[0].scrollHeight);
}

function sendMessage() {
  text = $("#text").val();
  $("#text").val("");
  socket.emit("text", { msg: text });
  addMessage("User: " + text);
}

$(document).ready(function () {
  socket = io.connect(
    "http://" + document.domain + ":" + location.port + "/chat"
  );
  console.warn("http://" + document.domain + ":" + location.port + "/chat")
  socket.on("connect", function () {
    socket.emit("joined", {});
  });
  socket.on("message", function (data) {
    addMessage(data.msg);
  });
  socket.on("sendAlert", function (data) {
    console.log("alert received", data);
    alert(data.msg);
  });
  socket.on("connect_error", function (err) {
    console.error("Connection error:", err);
  });

  $("#text").keypress(function (e) {
    const code = e.keyCode || e.which;
    if (code == 13) {
      sendMessage();
    }
  });
  $("#submitButton").click(function () {
    sendMessage();
  });

  $("#clearPdfListButton").click(function () {
    // call /deletePdfList route as DELETE
    const confirmation = confirm("Are you sure you want to clear the list?");
    if (!confirmation) {
      return;
    }
    $.ajax({
      url: "/deletePdfList",
      type: "DELETE",
      success: function (result) {
        window.location.reload();
      },
    });
  });

  // $("#pdfSendFile").change(function () {
  //   const file = document.getElementById("pdfSendFile").files[0];
  //   const reader = new FileReader();
  //   reader.onload = function (e) {
  //     socket.emit("pdf", { pdf: e.target.result });
  //   };
  //   reader.readAsDataURL(file);
  //   canSend = true;
  // });
});
function leave_room() {
  socket.emit("left", {}, function () {
    socket.disconnect();
  });
}
