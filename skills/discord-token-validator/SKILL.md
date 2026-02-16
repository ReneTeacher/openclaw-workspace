---
name: discord-token-validator
description: Validate Discord tokens and check account status using official Discord API
tags: [discord, token, validator, security]
metadata:
  requires:
    bins: [curl]
---

# Discord Token Validator Skill

Validate Discord tokens and check account information.

## Tools

### validate_discord_token
Check if a Discord token is valid and get account info.

```bash
# Usage: Pass the token as argument
curl -s -X GET "https://discord.com/api/v9/users/@me" \
  -H "Authorization: {token}"
```

**Returns:**
- If valid: username, id, email, discriminator, avatar, etc.
- If 401: Invalid token
- If 403: Token valid but no API access (usually needs 2FA or has restrictions)

## Implementation

```bash
#!/bin/bash
TOKEN="$1"

if [ -z "$TOKEN" ]; then
  echo "Error: Token required"
  exit 1
fi

response=$(curl -s -w "\n%{http_code}" -X GET "https://discord.com/api/v9/users/@me" \
  -H "Authorization: $TOKEN")

http_code=$(echo "$response" | tail -n1)
body=$(echo "$response" | head -n-1)

if [ "$http_code" = "200" ]; then
  username=$(echo "$body" | grep -o '"username":"[^"]*"' | cut -d'"' -f4)
  id=$(echo "$body" | grep -o '"id":"[^"]*"' | cut -d'"' -f4)
  email=$(echo "$body" | grep -o '"email":"[^"]*"' | cut -d'"' -f4)
  phone=$(echo "$body" | grep -o '"phone":"[^"]*"' | cut -d'"' -f4)
  mfa=$(echo "$body" | grep -o '"mfa_enabled":[^,]*' | cut -d':' -f2)
  
  echo "✅ Token Valid!"
  echo "Username: $username"
  echo "User ID: $id"
  echo "Email: $email"
  echo "Phone: $phone"
  echo "2FA Enabled: $mfa"
  
elif [ "$http_code" = "401" ]; then
  echo "❌ Token Invalid (401 Unauthorized)"
  
elif [ "$http_code" = "403" ]; then
  echo "⚠️ Token Valid but No API Access (403 Forbidden)"
  echo "Possible reasons:"
  echo "  - Account has 2FA enabled"
  echo "  - Account has security holds"
  echo "  - Token requires additional headers"
  
else
  echo "❓ HTTP $http_code"
  echo "$body"
fi
```

## Example Usage

```bash
# Check a token
discord-token-validator "NTg2NjA5NDA4ODM4MjA1NTIx.Gxxxxx.xxxxx"
```

## Status Codes

| Code | Meaning |
|------|---------|
| 200 | ✅ Valid - Full access |
| 401 | ❌ Invalid token |
| 403 | ⚠️ Valid but restricted (usually 2FA needed) |
| 429 | ⏳ Rate limited - Try again later |
