 var lenght=0;var letter=0;var capital=0;var number=0;var space=0; var b=1;
    $(document).ready(function(){
        
        $('#inputnNewpwd').keyup(function() {
            var pswd = $(this).val();
            
            //validate the length
            if ( pswd.length < 8 ) {
                $('#length').removeClass('valid').addClass('invalid');
                lenght=1;
            } else {
                $('#length').removeClass('invalid').addClass('valid');
                lenght=0;
            }
            
            //validate letter
            if ( pswd.match(/[a-z]/) ) {
                $('#letter').removeClass('invalid').addClass('valid');
                letter=0;
            } else {
                $('#letter').removeClass('valid').addClass('invalid');
                letter=1;
            }

            //validate capital letter
            if ( pswd.match(/[A-Z]/) ) {
                $('#capital').removeClass('invalid').addClass('valid');
                capital=0;
            } else {
                $('#capital').removeClass('valid').addClass('invalid');
                capital=1;
            }

            //validate number
            if ( pswd.match(/\d/) ) {
                $('#number').removeClass('invalid').addClass('valid');
                var number=0;
            } else {
                $('#number').removeClass('valid').addClass('invalid');
                var number=1;
            }
            
            //validate space
            if ( pswd.match(/[^a-zA-Z0-9]/) ) {
                $('#space').removeClass('invalid').addClass('valid');
                space=0;
            } else {
                $('#space').removeClass('valid').addClass('invalid');
                space=1;
            }
            if (lenght==0 && letter==0 && capital==0 && number==0 && space==0){
                $('#inputnNewpwd_error').text("");
            }
            else{
               $('#inputnNewpwd_error').text("Password does not meet the criteria");
               event.preventdefault();
            }
            
        }).focus(function() {
            $('#pswd_info').show();
        }).blur(function() {
            $('#pswd_info').hide();
        });
        
    });

    $('#inputOldpwd').keyup(function(){
      if(!$('#inputOldpwd').val()){
        $('#inputOldpwd_error').text("Please enter current password");
      }
      else{
        $('#inputOldpwd_error').text("");
      }
    }); 

    $('#inputnConpwd').keyup(function(){
        if(!$('#inputnConpwd').val()){
          $('#inputnConpwd_error').text("Please enter confirm password");
        }
        else{
          if($("#inputnNewpwd").val() == $("#inputnConpwd").val()){
            $('#inputnConpwd_error').text("");
          }
          else{
            $('#inputnConpwd_error').text("Password does not match");
            return false;
          }
        }
    }); 

$("#pwd_update").click(function(e){

  if(!$('#inputOldpwd').val()){
    $('#inputOldpwd_error').text("Please enter current password");
  }
  else{
    $('#inputOldpwd_error').text("");
  }

  if(!$('#inputnNewpwd').val()){
    $('#inputnNewpwd_error').text("Please enter new  password");
  }
  else{
    var pswd = $('#inputnNewpwd').val();
            
            //validate the length
            if ( pswd.length < 8 ) {
                $('#length').removeClass('valid').addClass('invalid');
                lenght=1;
            } else {
                $('#length').removeClass('invalid').addClass('valid');
                lenght=0;
            }
            
            //validate letter
            if ( pswd.match(/[a-z]/) ) {
                $('#letter').removeClass('invalid').addClass('valid');
                letter=0;
            } else {
                $('#letter').removeClass('valid').addClass('invalid');
                letter=1;
            }

            //validate capital letter
            if ( pswd.match(/[A-Z]/) ) {
                $('#capital').removeClass('invalid').addClass('valid');
                capital=0;
            } else {
                $('#capital').removeClass('valid').addClass('invalid');
                capital=1;
            }

            //validate number
            if ( pswd.match(/\d/) ) {
                $('#number').removeClass('invalid').addClass('valid');
                var number=0;
            } else {
                $('#number').removeClass('valid').addClass('invalid');
                var number=1;
            }
            
            //validate space
            if ( pswd.match(/[^a-zA-Z0-9]/) ) {
                $('#space').removeClass('invalid').addClass('valid');
                space=0;
            } else {
                $('#space').removeClass('valid').addClass('invalid');
                space=1;
            }

            if (lenght==0 && letter==0 && capital==0 && number==0 && space==0){
                $('#inputnNewpwd_error').text("");
            }
            else{
               $('#inputnNewpwd_error').text("Password does not meet the criteria");
               return false;
               event.preventdefault();
            }

  }

  if(!$('#inputnConpwd').val()){
    $('#inputnConpwd_error').text("Please enter confirm password");
  }
  else{
    if($("#inputnNewpwd").val() == $("#inputnConpwd").val()){
      $('#inputnConpwd_error').text("");
    }
    else{
      $('#inputnConpwd_error').text("Password does not match");
      return false;
  }
}

  if ($('#inputOldpwd').val() && $('#inputnNewpwd').val() && $('#inputnConpwd').val()){
    
  }
  else{
     return false;
    event.preventdefault();
  }
});





 var lenghtr=0;var letterr=0;var capitalr=0;var numberr=0;var spacer=0; var br=1;
    $(document).ready(function(){
        
        $('#inputNewpwd').keyup(function() {
            var pswd = $(this).val();
            
            //validate the length
            if ( pswd.length < 8 ) {
                $('#lengthrp').removeClass('valid').addClass('invalid');
                lenghtr=1;
            } else {
                $('#lengthrp').removeClass('invalid').addClass('valid');
                lenghtr=0;
            }
            
            //validate letter
            if ( pswd.match(/[a-z]/) ) {
                $('#letterrp').removeClass('invalid').addClass('valid');
                letterr=0;
            } else {
                $('#letterrp').removeClass('valid').addClass('invalid');
                letterr=1;
            }

            //validate capital letter
            if ( pswd.match(/[A-Z]/) ) {
                $('#capitalrp').removeClass('invalid').addClass('valid');
                capitalr=0;
            } else {
                $('#capitalrp').removeClass('valid').addClass('invalid');
                capitalr=1;
            }

            //validate number
            if ( pswd.match(/\d/) ) {
                $('#numberrp').removeClass('invalid').addClass('valid');
                var numberr=0;
            } else {
                $('#numberrp').removeClass('valid').addClass('invalid');
                var numberr=1;
            }
            
            //validate space
            if ( pswd.match(/[^a-zA-Z0-9]/) ) {
                $('#spacerp').removeClass('invalid').addClass('valid');
                spacer=0;
            } else {
                $('#spacerp').removeClass('valid').addClass('invalid');
                spacer=1;
            }
            if (lenghtr==0 && letterr==0 && capitalr==0 && numberr==0 && spacer==0){
                $('#inputNewpwd_error').text("");
            }
            else{
               $('#inputNewpwd_error').text("Password does not meet the criteria");
               event.preventdefault();
            }
            
        }).focus(function() {
            $('#pswd_infor').show();
        }).blur(function() {
            $('#pswd_infor').hide();
        });
        
    });

    
    $('#inputConpwd').keyup(function(){
        if(!$('#inputConpwd').val()){
          $('#inputConpwd_error').text("Please enter confirm password");
        }
        else{
          if($("#inputNewpwd").val() == $("#inputConpwd").val()){
            $('#inputConpwd_error').text("");
          }
          else{
            $('#inputConpwd_error').text("Password does not match");
            return false;
          }
        }
    }); 

$("#cpwd_btrn").click(function(e){

  if(!$('#inputNewpwd').val()){
    $('#inputNewpwd_error').text("Please enter new  password");
  }
  else{
    var pswd = $('#inputNewpwd').val();
            
            //validate the length
            if ( pswd.length < 8 ) {
                $('#length').removeClass('valid').addClass('invalid');
                lenghtr=1;
            } else {
                $('#length').removeClass('invalid').addClass('valid');
                lenghtr=0;
            }
            
            //validate letter
            if ( pswd.match(/[a-z]/) ) {
                $('#letter').removeClass('invalid').addClass('valid');
                letterr=0;
            } else {
                $('#letter').removeClass('valid').addClass('invalid');
                letterr=1;
            }

            //validate capital letter
            if ( pswd.match(/[A-Z]/) ) {
                $('#capital').removeClass('invalid').addClass('valid');
                capitalr=0;
            } else {
                $('#capital').removeClass('valid').addClass('invalid');
                capitalr=1;
            }

            //validate number
            if ( pswd.match(/\d/) ) {
                $('#number').removeClass('invalid').addClass('valid');
                var numberr=0;
            } else {
                $('#number').removeClass('valid').addClass('invalid');
                var numberr=1;
            }
            
            //validate space
            if ( pswd.match(/[^a-zA-Z0-9]/) ) {
                $('#space').removeClass('invalid').addClass('valid');
                spacer=0;
            } else {
                $('#space').removeClass('valid').addClass('invalid');
                spacer=1;
            }

            if (lenghtr==0 && letterr==0 && capitalr==0 && numberr==0 && spacer==0){
                $('#inputNewpwd_error').text("");
            }
            else{
               $('#inputNewpwd_error').text("Password does not meet the criteria");
               return false;
               event.preventdefault();
            }

  }

  if(!$('#inputConpwd').val()){
    $('#inputConpwd_error').text("Please enter confirm password");
  }
  else{
    if($("#inputNewpwd").val() == $("#inputConpwd").val()){
      $('#inputConpwd_error').text("");
    }
    else{
      $('#inputConpwd_error').text("Password does not match");
      return false;
  }
}

  if ( $('#inputNewpwd').val() && $('#inputConpwd').val()){
    
  }
  else{
     return false;
    event.preventdefault();
  }
});
