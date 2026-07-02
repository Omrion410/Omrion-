# Zk App Structure

## Authentication
- Splash Screen
- Welcome
- Login
- Register
- Forgot Password

## Main Navigation
- Home
- Services
- Community
- Messages
- Profile

## Services
- Sports
- Health
- Education
- Jobs
- Volunteering
- Business
- Travel

## User
- Notifications
- Settings
- Wallet
- Achievements
---

# User Roles

## 1. Guest
- Browse public services.
- Search for opportunities.
- View opportunity details.
- Create a new account.

## 2. User
- Create and edit profile.
- Apply for opportunities.
- Save favorites.
- Send and receive messages.
- Create posts and interact with the community.
- Receive notifications.
- Manage subscriptions.

## 3. Service Provider
- Publish services.
- Edit services.
- Manage requests.
- View analytics.
- Communicate with users.

## 4. Administrator
- Manage all users.
- Review and approve services.
- Handle reports.
- Manage advertisements.
- Manage subscriptions.
- Manage platform content.
- View complete analytics.

---

# Core Modules

- Authentication
- Home
- Services
- Community
- Messages
- Notifications
- Search
- Favorites
- Profile
- Settings
- Subscription
- Admin Dashboard
---

# Navigation Flow

## Authentication
Splash Screen
    ↓
Welcome
    ↓
Login / Register
    ↓
Home

---

## Main Navigation

Home
├── Services
│   ├── Sports
│   ├── Health
│   ├── Jobs
│   ├── Scholarships
│   ├── Volunteering
│   ├── Travel
│   ├── Education
│   └── Business
│
├── Community
│
├── Messages
│
├── Notifications
│
├── Favorites
│
├── Search
│
├── Profile
│   ├── Personal Information
│   ├── Activity
│   ├── Achievements
│   ├── Settings
│   └── Subscription
│
└── Admin Dashboard
---

# Database Structure

## Users
- user_id
- full_name
- email
- password_hash
- country
- profile_photo
- role
- subscription_plan
- created_at

---

## Services
- service_id
- title
- description
- category
- provider_id
- country
- status
- created_at

---

## Applications
- application_id
- user_id
- service_id
- status
- created_at

---

## Messages
- message_id
- sender_id
- receiver_id
- content
- created_at

---

## Notifications
- notification_id
- user_id
- title
- content
- is_read
- created_at

---

## Community Posts
- post_id
- author_id
- content
- media_url
- likes_count
- comments_count
- created_at

---

## Premium Subscriptions
- subscription_id
- user_id
- plan_name
- start_date
- end_date
- status

---

## Rewards
- reward_id
- user_id
- points
- level
- updated_at
