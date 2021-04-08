# Appstore Connect APİ
Simple python JWT implementation of app store connect api, to communicate with the App Store Connect API need to authorize with JWT.  

## Overview
JSON Web Token (JWT) is an open standard (RFC 7519) that defines a way to securely transmit information. The App Store Connect API requires JWTs to authorize each API request. You create the token, signing it with the private key you downloaded from App Store Connect.

To generate a signed JWT:

1. Create the JWT header.
2. Create the JWT payload.
3. Sign the JWT.
Include the signed JWT in the authorization header of each App Store Connect API request.

## Credentials

1. kid
To get your key ID, copy it from App Store Connect by logging in to App Store Connect, then:

Select Users and Access, then select the API Keys tab.

The key IDs appear in a column under the Active heading. Hover the cursor next to a key ID to display the Copy Key ID link.

Click Copy Key ID.

If you have more than one API key, use the key ID of the same private key that you use to sign the JWT.

2. issuer id
To get your issuer ID, log in to App Store Connect and:

Select Users and Access, then Select the API Keys tab.

The issuer ID appears near the top of the page. To copy the issuer ID, click Copy next to the ID.

3. private key
AuthKey.p8 file 

