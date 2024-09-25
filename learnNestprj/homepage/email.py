

def send_confirmation_email(user):
    try:
        token = token_generator.make_token(user)
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        link = reverse('confirm_email', kwargs={'uidb64': uid, 'token': token})
        print("Below is the image link")
        print(link)
        full_link = f'http://127.0.0.1:8000{link}'

        send_mail(
            'Confirm your email',
            f'Click the link to confirm your email: {full_link}',
            'rombo.f2@gmail.com',
            [user.email],
            fail_silently=False,
        )
        print("Send email link...")
        print(send_mail)
    except smtplib.SMTPException as e:
        print(f"SMTP error occurred: {e}")


def confirm_email(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = get_user_model().objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, get_user_model().DoesNotExist):
        user = None

    if user is not None and token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect('login')
    else:
        return render(request, 'email_confirmation_invalid.html')

