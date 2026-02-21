from djoser import email


class ActivationEmail(email.ActivationEmail):
    template_name = 'auth_api/activation.html'


class ConfirmationEmail(email.ConfirmationEmail):
    template_name = 'auth_api/confirmation.html'


class PasswordResetEmail(email.PasswordResetEmail):
    template_name = 'auth_api/password_reset.html'


class PasswordChangedConfirmationEmail(email.PasswordChangedConfirmationEmail):
    template_name = 'auth_api/password_changed_confirmation.html'