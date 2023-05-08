function imageSubmit() {

    let imageInputVal = $('#image')[0];
    let formData = new FormData();
    formData.append('image', imageInputVal.files[0]);
    $.ajax({
        type: 'POST',
        url: '/change_profile',
        data: formData,
        processData: false,
        contentType: false,
        success: function(result){

            $('#imageInput').attr('class', 'mt-2 d-none');
            let fname = 'http://127.0.0.1:5000/static/data/profile.png?q=' + result;

            $('#profile_img').attr('src',  fname);
//            $('#profile_img').attr('src', 'static/data/profile.png');
        }
    });
}

function changeProfile(){
    $('#imageInput').attr('class', 'mt-2');
}


function addrSubmit() {
    $('#addrInput').attr('class', 'mt-2 d-none');   // input box가 안 보이게
    let addr = $('#addrInputTag').val();
    $.ajax({
        type : 'GET',
        url : '/change_addr',
        data : {addr: addr},
        success: function(msg) {
            $('#addr').html(msg);
        }
    });
};

// 주소 변경 input show
function changeAddr(){
    $('#addrInput').attr('class', 'mt-2');          // input box가 보이게
};

// 명언 변경
function changeQuote(){
    $.ajax({
        type: 'GET', 
        url: '/change_quote',
        data: ' ',  // 서버로 전달할 데이터
        success: function(msg){     // msg: 서버로부터 받은 데이터
            $('#quoteMsg').html(msg);
        }
    });

};


$(document).ready(function(){

    $('#p_weather').on('click', function(){

        let addr = $('#addr').text()

        $.ajax({
            type: 'GET',
            url: '/get_weather',
            data: {addr: addr},
            success: function(result) {
                $('.res_weather').html(result);
            }
        });        
    });
    
});