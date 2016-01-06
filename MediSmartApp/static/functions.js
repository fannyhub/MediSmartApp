var questions = ['how many moons does Saturn have?', 'What is the longest river on Earth?'];
var answers = [31, 'Nile'];

function quizEm(questions, answers) {
    var score = 0;
    for(var i=0; i<questions.length; i++){
        if(prompt(questions[i]) == answers[i]) {
            alert('good!');
            score ++;}
        else alert('booo');

    }
    document.write('your score is ' + score);
}

function showDate() {
    today = new Date();
    return today.toDateString();
}


////////////////////////////////////////

function fnShowAllPatients() {
    $('#selected_patients').html('');
    $('#all_patients_table').fadeIn(1000);
}

function fnHideAllPatients() {
    $('#all_patients_table').hide();
}

function fnClickAllPatientsBtn() {

$("#all_patients_btn").click(function() {
    fnShowAllPatients();
});
}

function fnClickSearchBtn() {
    $("#search_btn").click(function() {
        fnHideAllPatients();
        $("#selected_patients").html('');
        var last_name = $("#search_form").val().toLowerCase();
        $('#all_patients_table td:not(:has(a))').each(function() {
            if($(this).text().toLowerCase().search(last_name)>-1) {
            $("#selected_patients").append($(this).parent().clone());
            }
        });

    });
}

$(document).ready(function() {
    fnHideAllPatients();
    fnClickSearchBtn();
    fnClickAllPatientsBtn();

});