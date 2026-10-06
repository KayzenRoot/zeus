# Zeus Security

## Public-repository policy
The owner explicitly authorizes temporary PUBLIC visibility for CI. This does not authorize publishing secrets or confidential configuration.

Never commit:
- API keys or bearer tokens;
- ChatGPT/OpenAI, DeepSeek, Meta or other provider credentials;
- private endpoints containing credentials;
- local machine secrets;
- signing keys;
- production datasets containing sensitive data.

## Rebrand security requirements
- Environment-variable rename must not introduce hard-coded credentials.
- Docker examples must use placeholders.
- No destructive Git history rewrite.
- Historical provenance remains immutable.
- Dependency behavior must remain unchanged in the identity-only increment.

## High-assurance boundary
Authentication, signing, money, trading, privileged actions and irreversible operations require separate HIGH_ASSURANCE Work Orders.
