class Login_Meli():
    
#Tipo de Autenticación ("Facebook" / "email" / "Ya tengo cuenta")
    btn_omitir_id = "000000"
    lbl_titulo_id = "com.mercadolibre:id/home_onboarding_register_title"
    btn_facebook_id = "com.mercadolibre:id/home_onboarding_facebook_register_button" # Facebook
    btn_facebook_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.Button[2]"
    btn_email_id = "com.mercadolibre:id/home_onboarding_email_register_button" # email
    btn_email_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.Button[1]"
    btn_already_id = "com.mercadolibre:id/home_onboarding_already_has_account_button" # ya tengo cuenta
    btn_already_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.view.ViewGroup/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.Button[3]"

#Ingresar Usuario
    lbl_titulo_login_id = "com.mercadolibre:id/login_username_text"
    txt_usuario_id = "com.mercadolibre:id/ui_text_field_input"
    txt_usuario_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/TextInputLayout"
    btn_continuar_id = "com.mercadolibre:id/login_continueButton"
    btn_continuar_xpath = "	/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.view.View/android.widget.ScrollView/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.Button"

#Ingresar Clave
    lbl_titulo_passw_id = "com.mercadolibre:id/login_password_text"
    txt_clave_id = "com.mercadolibre:id/ui_text_field_input"
    txt_clave_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.view.View/android.widget.ScrollView/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.EditText"
    btn_ingresar_id = "com.mercadolibre:id/login_ingresarButton"
    btn_ingresar_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.view.View/android.widget.ScrollView/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.Button[1]"
    btn_verClave_id = "com.mercadolibre:id/text_input_password_toggle"
    btn_verClave_xpath = "//android.widget.ImageButton[@content-desc='Toggle password visibility']"
    btn_verClave_accid = "Toggle password visibility"
    btn_noseclave_id = "com.mercadolibre:id/login_forgot_password"
    btn_noseclave_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.Button[2]"
    lbl_nosoy_id = "com.mercadolibre:id/login_change_user"

#Ingresar Captcha
    chk_Captcha_id = "recaptcha-anchor"
    chk_Captcha_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.view.View/android.widget.RelativeLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.widget.CheckBox"
    btn_ingresarCaptcha_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.view.View/android.widget.RelativeLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.widget.Button"
    

    
    
    
    
    
      
    
    
    
    