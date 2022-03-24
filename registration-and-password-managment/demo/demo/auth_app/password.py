# touching django api for password encryption is pointless
# it is as secure as it can be
# managing forgotten passwords
# 1. changing password and sending email with new password
# new_password = random_generate_password()
# user = getUser(username)
# user.set_password(new password)
# user.should_change_password = True
# user.save()
# send_mail(new password)
# at login
# def form_valid(self,form):
#   if self.object_should_change_password:
#          change_password()
# 2. send email with change password link
# we have built in password reset views and forms
