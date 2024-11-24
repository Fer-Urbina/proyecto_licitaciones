from django.core.mail import send_mail

def notify_proveedor(licitacion):
    send_mail(
        subject="Actualización de Licitación",
        message=f"La licitación {licitacion.titulo} ha cambiado de estado a {licitacion.estado}.",
        from_email="your_email@example.com",
        recipient_list=["proveedor@example.com"],
    )