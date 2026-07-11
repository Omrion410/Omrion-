# ZK - Splash Screen

## Purpose

The Splash Screen is the user's first impression of the ZK platform.
Its purpose is to create a premium feeling, strengthen brand identity, and smoothly prepare the application before entering the main experience.

---

# Duration

- Minimum: 2 seconds
- Maximum: 4 seconds
- Skip automatically after loading finishes.

---

# Background

Color:
Deep Space Black (#0B0F1A)

Background style:

- Soft radial gradient
- Very subtle animated particles
- Premium minimal appearance

---

# Logo

Display the official ZK logo in the exact center.

Logo animation:

- Fade In
- Scale from 90% to 100%
- Soft glow effect

Animation duration:

800ms

---

# Application Name

Display:

ZK

Below the logo.

Typography:

- Bold
- Large size
- White color

Subtitle:

Move Your Body
Inspire Your Life

Color:

Light Gray

---

# Loading Indicator

Bottom center.

Preferred style:

Animated progress line

Alternative:

Minimal circular loader.

Color:

Primary Blue

---

# Animation Sequence

0ms

Background appears.

300ms

Logo fades in.

800ms

Logo scales smoothly.

1200ms

Application name appears.

1600ms

Subtitle fades in.

2000ms

Loading animation starts.

When initialization finishes:

Fade to next screen.

---

# Initialization Tasks

While Splash Screen is visible:

- Load user session
- Load application settings
- Initialize local cache
- Check authentication
- Load theme
- Verify internet connection

---

# Navigation Logic

If first launch:

Go to Onboarding.

If authenticated:

Go to Home.

Otherwise:

Go to Login.

---

# Accessibility

Respect reduced motion settings.

Maintain high color contrast.

Support screen readers.

---

# Performance

Startup must remain under 3 seconds whenever possible.

Avoid heavy animations.

Keep memory usage minimal.

---

# Design Principles

Premium

Modern

Minimal

Elegant

Fast

Professional

Emotionally inspiring
