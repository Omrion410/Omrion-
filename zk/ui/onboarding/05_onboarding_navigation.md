# ZK - Onboarding Navigation

## Purpose

This document defines the navigation flow for the onboarding experience.

---

# Navigation Flow

Splash Screen

↓

Onboarding Page 1

↓

Onboarding Page 2

↓

Onboarding Page 3

↓

Onboarding Page 4

↓

Authentication

---

# Swipe Navigation

Users can swipe horizontally.

Previous pages remain accessible.

Smooth gesture support.

---

# Skip Button

Visible on every page except the last.

Position:

Top Right

Action:

Jump directly to Authentication.

---

# Next Button

Appears on Pages 1–3.

Moves to the next onboarding page.

---

# Get Started Button

Visible only on the last page.

Action:

Navigate to Login Screen.

---

# Progress Indicator

Four dots.

Current page highlighted.

Animated transitions.

---

# Back Navigation

Android Back:

Return to previous onboarding page.

From Page 1:

Exit application confirmation.

---

# Navigation Animation

Horizontal Slide

Duration:

350ms

Curve:

Ease In Out

---

# State Saving

If onboarding is completed once:

Do not show onboarding again.

Navigate directly to Splash then Login.

---

# Accessibility

Support screen readers.

Large touch targets.

Keyboard navigation support.

---

# Performance

Instant page switching.

No unnecessary loading.

Maintain 60 FPS.
