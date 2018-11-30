
"###########################################################"
"#####                   NOMENCLATURA                   ###"
" TIPO DE CONTROL + NOMBRE DEL OBJETO + SELENIUM ELEMENT"
"########################################################"
# Label = lbl
# text = txt
# dropdown = dpd
# boton = btn
# checkbox= chk
# option buton = opt


class Login_oldelval:
    
    lbl_Titulo_xpath = "//*[@class='login-box-xxx']"
    
    txt_user_xpath = "//*[@id='txtUserttt']"
    
    txt_pass_xpath = "//*[@id='txtPassword']"
    
    btn_ingresar_xpath = "//*[@id='btnLoguearse']"
    
    ############ Mensajes de Error ###########
    msj_NoLogin_xpath = "//*[contains(@class, 'alert alert-danger ng-binding')]"
    #Usuario o Contraseña inválidos.
    #Usuario o password incorrecto.
    #Usuario bloqueado.

    