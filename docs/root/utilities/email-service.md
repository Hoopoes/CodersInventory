The **EmailService** class provides both **synchronous** and **asynchronous** methods for sending emails, complete with support for **HTML templates** and **dynamic data rendering** using `chevron`. It supports **To**, **CC**, and **BCC** recipients, making it versatile for various use cases.

### ✉️ Email Service Class

!!! Dependencies

    - pip install chevron
    - pip install aiosmtplib

```python title="email_service.py"
import chevron
import smtplib
import aiosmtplib
from email.utils import formataddr
from email.mime.text import MIMEText
from typing import Any, Optional
from email.mime.multipart import MIMEMultipart

class EmailService:
    def __init__(self, display_name: str, email_sender: str, email_password: str) -> None:
        self.display_name = display_name
        self.email_sender = email_sender
        self._email_password = email_password

    def compile_email(self, 
            subject: str, 
            to: list[str], 
            html: str, data: Optional[dict[str, Any]] = None, 
            cc: Optional[list[str]] = None, 
            bcc: Optional[list[str]] = None):
        
        msg = MIMEMultipart('alternative')
        if self.display_name:
            msg['From'] = formataddr((self.display_name, self.email_sender))
        else:
            msg['From'] = self.email_sender

        # Handle To, CC, and BCC
        recipients = to[:]  # Start with the 'to' list
        if cc:
            msg['Cc'] = ", ".join(cc) #Comma separated for multiple CCs
            recipients.extend(cc)
        if bcc:
            msg['Bcc'] = ", ".join(bcc) #Comma separated for multiple BCCs
            recipients.extend(bcc)
        msg['To'] = ", ".join(to) #Comma separated for multiple TOs

        msg['Subject'] = subject

        if data is not None:
            html = chevron.render(template=html, data=data)
        
        part1 = MIMEText(html, 'html')
        msg.attach(part1)
        return recipients, msg
    
    def send_email(
            self, 
            subject: str, 
            to: list[str], 
            html: str, 
            data: Optional[dict[str, Any]] = None, 
            cc: Optional[list[str]] = None, 
            bcc: Optional[list[str]] = None):
        
        recipients, msg = self.compile_email(subject, to, html, data, cc, bcc)

        with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
            smtp.starttls() # Start TLS encryption
            smtp.login(self.email_sender, self._email_password)
            smtp.sendmail(self.email_sender, recipients, msg.as_string())

    async def send_email_async(
            self, 
            subject: str, 
            to: list[str], 
            html: str, 
            data: Optional[dict[str, Any]] = None, 
            cc: Optional[list[str]] = None, 
            bcc: Optional[list[str]] = None):
        
        recipients, msg = self.compile_email(subject, to, html, data, cc, bcc)
        
        async with aiosmtplib.SMTP(hostname='smtp.gmail.com', port=587, start_tls=True) as smtp:
            await smtp.login(self.email_sender, self._email_password)
            await smtp.sendmail(self.email_sender, recipients, msg.as_string())
```


## 📝 Usage Example  

### HTML Email Template  

```html title="template.html" hl_lines="4 5"
<!DOCTYPE html>
<html>
    <body style="font-family: Arial, sans-serif;">
        <p>Hello {{name}},</p>   <!--(1)!--> 
        <p>The issue you're experiencing is related to: <b>{{problem}}</b>.</p> <!--(2)!--> 
        <p>We are working on it and will get back to you shortly.</p>
        <p>Best regards,</p>

        <!-- Simple Contact Signature -->
        <p><b>Muhammad Umar Anzar</b><br>
           AI/ML Engineer<br>
           Hoopoes<br>
        </p>
    </body>
</html>
```
{ .annotate }

1. This placeholder will be replaced with the actual name during template rendering.
2. This placeholder will be replaced with the actual name during template rendering.


### Sending an Email

```python title="main.py" 
email_service = EmailService(
    display_name="Umar",
    email_sender="your@email.com",
    email_password="your app password",
)
```

=== "Synchronous" 

    ```python title="main.py" hl_lines="7"
    email_service.send_email(
        subject="Alert 🚨",
        to=["john.doe@email.com", "doe.john@email.com"],
        cc=["john.doe@email.com", "doe.john@email.com"],
        bcc=["john.doe@email.com", "doe.john@email.com"],
        html=html_email,
        data={"name": "John Doe", "problem": "Internet Service"},
    )
    ```

=== "Asynchronous"

    ```python title="main.py" hl_lines="7"
    await email_service.send_email_async(
        subject="Alert 🚨",
        to=["john.doe@email.com", "doe.john@email.com"],
        cc=["john.doe@email.com", "doe.john@email.com"],
        bcc=["john.doe@email.com", "doe.john@email.com"],
        html=html_email,
        data={"name": "John Doe", "problem": "Internet Service"},
    )
    ```


!!! tip
    - Use **environment variables** to store sensitive credentials like your email and password.  
    - Ensure **"Less secure app access"** is enabled in Gmail for SMTP to work.  
    - Use **app passwords** instead of your regular password for better security.  
    - Synchronous version may block the application during sending, whereas the asynchronous version provides non-blocking I/O.