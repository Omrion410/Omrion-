# ZK - Chat Layout

---

# Purpose

This document defines the layout structure of the Chat Screen.

The layout should provide a distraction-free messaging experience while keeping all communication tools easily accessible.

---

# Layout Philosophy

The Chat layout should feel:

* Clean
* Comfortable
* Modern
* Responsive
* Familiar

The conversation should always remain the primary focus.

---

# Screen Structure

Top to Bottom:

* Safe Area
* Chat Header
* Conversation Area
* Typing Indicator
* Message Composer
* Bottom Safe Area

---

# Header Layout

The header contains:

* Back Button
* User Avatar
* User Name
* Online Status
* Voice Call Button (Future)
* Video Call Button (Future)
* More Options

---

# Conversation Layout

Messages are displayed vertically.

Older messages appear at the top.

Newest messages appear at the bottom.

Automatically scroll to the newest unread message.

---

# Message Bubble Layout

Each message contains:

* Message Content
* Timestamp
* Delivery Status
* Read Status

Outgoing messages appear on the right.

Incoming messages appear on the left.

---

# Message Grouping

Consecutive messages from the same sender should be visually grouped.

Display the avatar only on the first message of a group.

---

# Date Separator

Insert separators between days.

Examples:

* Today
* Yesterday
* Monday
* 15 July 2026

---

# Typing Indicator

Display above the message composer.

Hide automatically when typing stops.

---

# Message Composer Layout

The composer contains:

* Emoji Button
* Attachment Button
* Camera Button
* Text Input
* Send Button

The text field expands vertically as the message grows.

---

# Responsive Design

Phones:

Full-width conversation.

Tablets:

Centered conversation with adaptive width.

Landscape mode should maximize usable space.

---

# Accessibility

Support:

* Screen Readers
* Large Text
* High Contrast
* Reduced Motion

Touch targets should be at least 48 × 48 px.

---

# Performance

The layout should:

* Render efficiently.
* Support thousands of messages.
* Preserve scroll position.
* Minimize unnecessary redraws.

---

# Future Expansion

The layout should support:

* Threaded Replies
* Pinned Messages
* Voice Messages
* Shared Files
* Polls
* AI Chat Assistant

without requiring structural redesign.

---

# Design Principles

The Chat layout should always be:

* Clean
* Fast
* Comfortable
* Accessible
* Scalable
* Future Ready

---

End of document.

