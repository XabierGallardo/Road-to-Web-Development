# Email Deliverability
In order to improve email deliverability, **the records SPF, DKIM and DMARC** become significantly relevant.
The mailbox providers, due to the significant increase in email marketing activities, filter everyday all the messages we sent and that have to be sent to a recipient.

- **SPF - Sender Policy Framework**: Prevents spammers from sending messages with forged from addresses at your domain
- **DKIM - Domain Keys Identified Mail**: Helps you protect your company from email spamming and phishing attempts.
- **DMARC**: Empowers SPF and DKIM

After the config, your email would go directly to inbox and mailbox providers would pass your host for authentication and also declare you a trusted sender, as there are many other reasons to going mail to spam.

Another config to do is to authenticate the domain with G Suite, Microsoft 365, Ontraport, Zoho, SendGrid, Mailchimp, MailGun, Aweber, GetResponse, Sendinblue, Moosend, ConvertKit, ActiveCampaign, Klaviyo, Privy, Amazon SES and others.

## What factors affect email deliverability?
Many factors can affect deliverability, including
- Having a good sending reputation
- Properly authenticating your mail through SPF and DKIM
- Having strong permission practices
- The health of the message infrastructure
- What's in the message & who's sending it
- Receiving system's availability

## What is a SPF protocol?
The SPF protocol, which is based on the DNS of your domain name, can certify that the issuing IP has the right to send emails.
This protocol is used to prevent fraudulent use of your domain name and prevent 3rd parties from pretending to be you.

## What is a DKIM protocol?
The DKIM protocol is a cryptographic protocol based on the use of public keys that are published in your DNS.
The protocol allows you to sign your email with your domain name.
The recipient of your email will then be sure that the email he or she received has been written by you

## What is a DMARC protocol?
Both DKIM and SPF protocols are complementary and respond to different types of fraud. However, they have the disadvantage of not giving acting instructions in case of an attack.
The DMARC protocol overcomes this deficiency and provides indications in case there is an attack.

## Do all mail servers support all the three security features?
No, some mail servers don't support all SPF, DKIM and DMARC. Some support all three while others don't.

## What do you need to get started?
- The name of the company or website hosting the emails (G-suite, Office365 mail, Cpanel, zoho mail)
- Access to the domain DNS hosting
- Access to the email server
