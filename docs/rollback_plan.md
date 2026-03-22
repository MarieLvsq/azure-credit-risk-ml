# Rollback Plan — German Credit Risk Endpoint

## Objective
Provide a basic rollback procedure for controlled deployment demonstrations.

## Rollback Triggers
- Endpoint returns invalid predictions
- Schema mismatch detected
- Unexpected scoring errors
- Governance documentation found incomplete
- Smoke test failure after deployment

## Rollback Actions
1. Disable or remove the active deployment
2. Revert to the last known approved model artifact
3. Re-run smoke test against reverted deployment
4. Record issue in release notes / incident log
5. Review root cause before re-release

## Recovery Principle
No promotion to wider use without successful validation and documentation review.
