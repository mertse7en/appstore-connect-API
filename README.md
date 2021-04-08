# Appstore Connect APİ
Simple python JWT implementation of app store connect api, to communicate with the App Store Connect API must be authorized with JWT.  

## Overview
JSON Web Token (JWT) is an open standard (RFC 7519) that defines a way to securely transmit information. The App Store Connect API requires JWTs to authorize each API request. You create the token, signing it with the private key you downloaded from App Store Connect.

To generate a signed JWT:

1- Create the JWT header.
2- Create the JWT payload.
3- Sign the JWT.
Include the signed JWT in the authorization header of each App Store Connect API request.
