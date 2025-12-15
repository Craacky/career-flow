# LinkedIn Job Scout + AI Resume Optimizer

## 🚀 Project Overview

LinkedIn Job Scout is a comprehensive job search platform that helps users find the best IT vacancies on LinkedIn and hh.ru. The platform combines advanced web scraping technology with AI-powered resume optimization to connect talented professionals with great companies.

### 📌 Core Features

1. **LinkedIn/hh.ru Job Scraping**: Automated daily scraping of IT job listings using Botasaurus to bypass anti-bot protections
2. **React Web Interface**: User-friendly job search interface with customizable filters for subscribers
3. **AI Resume Optimizer**: AI-powered analysis of PDF resumes with improvement recommendations
4. **Telegram Bot**: Automated job matching and notifications based on user preferences and resume content

---

## 🧱 Tech Stack

### Backend & Data
- **Scraping**: Botasaurus (Python) - powerful web scraping environment with anti-bot protection bypass
- **Backend Framework**: FastAPI/Litestar (Python)
- **Database**: PostgreSQL (jobs, users, resumes, filters)
- **Caching & Queues**: Redis
- **Task Queue**: Celery or RQ for background scraping

### Frontend (React)
- **Framework**: React 18
- **Language**: TypeScript
- **State Management**: Zustand
- **Styling**: CSS
- **API Queries**: React Query
- **Forms**: React Hook Form
- **Routing**: React Router DOM v6

### AI & Integrations
- **AI API**: OpenRouter
- **PDF Processing**: PyPDF2
- **Telegram Bot**: aiogram
- **Payments**: Stripe API

---

## 📋 Functional Requirements

### 1. LinkedIn/hh.ru Scraping System (Botasaurus)
#### General Settings:
- **Tool**: Botasaurus
- **Sources**: LinkedIn Jobs / hh.ru
- **Frequency**: Every 12 hours
- **Basic Filters**:
  - Level: Junior, Mid, Senior
  - Format: Remote, Hybrid, Office

#### Data Fields to Collect:
- Job title
- Company name
- Location
- Description
- Requirements and technology stack
- Salary range
- Job link
- Publication date
- Experience level
- Employment type

---

## 🗂️ Project Structure

### Frontend Directories

**📁 src/components/**
- **📁 ui/** - Basic UI components
- **📁 layout/** - Layout components
- **📁 jobs/** - Job-related components
- **📁 filters/** - Filter components
- **📁 auth/** - Authentication components
- **📁 profile/** - Profile components
- **📁 common/** - Common components

**📁 src/pages/** - Application pages
**📁 src/hooks/** - Custom React hooks
**📁 src/store/** - Zustand stores
**📁 src/services/** - API and services
**📁 src/utils/** - Utility functions
**📁 src/types/** - TypeScript type definitions
**📁 src/styles/** - Style files
**📁 src/assets/** - Asset files

---

## 🎨 Key Pages

### 1. Home Page (HomePage)
- Hero section
- Top jobs of the day
- Service benefits
- Quick filters

### 2. Jobs Page (JobsPage)
- Search and filters
- Job list
- Pagination
- Sorting

### 3. Job Details Page (JobDetailsPage)
- Full job information
- Similar jobs
- Save job button
- Apply button

### 4. Profile Page (ProfilePage)
- User information
- Favorite jobs
- Filter settings
- Subscription status

### 5. Subscription Page (SubscriptionPage)
- Free/Pro plans
- Payment form
- Pro benefits

### 6. Admin Panel (AdminPage)
- Statistics
- Scraping management
- Users
- Logs

---

## 🔧 Pro Filter Components

### Salary Filter
- Salary range slider
- Currency selection
- "Any salary" option

### Level Filter
- Level checkboxes
- Junior, Middle, Senior, Lead
- Multi-select

### Tech Filter
- Multi-select technology filters
- Technology search
- Popular technologies

### Work Format Filter
- Remote, Hybrid, Office
- Multi-select enabled
- Selection indicators

---

## 📱 UI/UX Features

### Desktop:
- Sidebar with filters
- Tabular job view
- Detailed cards

### Mobile:
- Hamburger menu
- Modal filters
- Card-based view

### General:
- Dark/light theme support
- Responsive design
- Lazy loading
- Loading skeletons

---

## 🚀 Development Plan

### Week 1-2: Basic Components
- Project setup (Vite + TypeScript)
- Basic UI components
- Routing
- Global styles

### Week 3-4: Job Pages
- Homepage
- Job list page
- Job details page
- Pagination and filters

### Week 5-6: User Features
- Authentication
- User dashboard
- Favorites
- Settings

### Week 7-8: Pro Features
- Pro filters
- Subscription system
- Admin panel
- Optimization

---

## 🛠️ Getting Started

### Prerequisites
- Node.js (v16 or higher)
- npm or yarn
- Python (for backend)
- PostgreSQL (for database)

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd career-flow
```

2. Install frontend dependencies:
```bash
cd frontend
npm install
```

3. Start the development server:
```bash
npm run dev
```

### Environment Variables

Create a `.env` file in the root of your frontend directory with the following variables:

```env
VITE_API_BASE_URL=http://localhost:8000/api
```

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 📞 Support

If you have any questions or need help, please contact us at [support-email].