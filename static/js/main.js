// Question Upvote
$(document).ready(function () {
  $(".voting").click(function (e) {
    var questionid = $(this).data("question");
    var button = $(this).attr("value");
    // console.log(questionid, button);
    e.preventDefault();
    $.ajax({
      url: VOTE_URL,
      type: "POST",
      data: {
        questionid: questionid,
        button: button,
        csrfmiddlewaretoken: CSRF_TOKEN,
        action: "voting",
      },
      success: function (json) {
        document.getElementById("votes").innerHTML = json["vote"];
      },
      error: function (xhr, errmsg, err) {},
    });
  });
});
