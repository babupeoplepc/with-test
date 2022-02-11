function setDateBox(){
    var today = new Date();
    var year = today.getFullYear();
    var month = today.getMonth()+1;
    var day = today.getDate();
    for(var y = 0; y< 60; y++)
    {
        $('.year_select').append("<option value='" + (year-y) + "'>" + (year-y) + " 년" + "</option>" );
    }
    for(var m=1; m< 13; m++)
    {
        $('.month_select').append("<option value='" + m + "'>" + m + " 월" + "</option>" );
    }
    for(var d=1; d< 32; d++)
    {
        $('.day_select').append("<option value='" + d + "'>" + d + " 일" + "</option>" );
    }

    $('.year_select').val(year);
    $('.month_select').val(month);
    $('.day_select').val(day);
};

function openZipSearch() {
	new daum.Postcode({
		oncomplete: function(data) {
			$('[name=student_home_address_number]').val(data.zonecode); // 우편번호 (5자리)
			$('[name=student_home_address]').val(data.address);			
		}
	}).open();
}
