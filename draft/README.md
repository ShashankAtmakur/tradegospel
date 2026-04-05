# Admin Analytics Dashboard 🎯

A comprehensive, production-ready admin dashboard built with **Next.js 15**, **TypeScript**, **MongoDB**, and **ShadCN UI** for managing a CV/Resume analysis platform.

![Dashboard Preview](https://img.shields.io/badge/Next.js-15-black)
![TypeScript](https://img.shields.io/badge/TypeScript-5.0-blue)
![MongoDB](https://img.shields.io/badge/MongoDB-Latest-green)
![License](https://img.shields.io/badge/license-MIT-blue)

## 🌟 Features

### Core Functionality
- ✅ **Role-Based Authentication** - Admin and User roles with JWT
- ✅ **Real-time Analytics** - Platform-wide statistics and insights
- ✅ **Interactive Charts** - Recharts integration for data visualization
- ✅ **Responsive Design** - Mobile, tablet, and desktop support
- ✅ **Server-Side Rendering** - Optimized performance with Next.js SSR
- ✅ **Type Safety** - Full TypeScript implementation

### Dashboard Sections
1. **User Demographics** - Country-wise distribution visualization
2. **CV Analysis Metrics** - Track analyses count and average scores
3. **Feedback Analytics** - User satisfaction and ratings
4. **User Segmentation** - Paid vs Free users with growth trends
5. **Top Performers** - Leaderboard of highest CV scorers
6. **Career Stage Breakdown** - Fresher, Graduate, Experienced distribution

## 🚀 Quick Start

### Prerequisites
- Node.js 18+ and npm
- MongoDB Atlas account (or local MongoDB)
- Git

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/admin-analytics-dashboard.git
cd admin-analytics-dashboard

# 2. Install dependencies
npm install

# 3. Set up environment variables
cp .env.example .env.local
# Edit .env.local with your MongoDB URI and JWT secret

# 4. Run development server
npm run dev

# 5. Open browser
# Navigate to http://localhost:3000
```

## 📋 Environment Variables

Create `.env.local` in the root directory:

```env
# MongoDB Connection String
MONGODB_URI=mongodb+srv://username:password@cluster.mongodb.net/cv-analytics

# JWT Secret (min 32 characters)
JWT_SECRET=your-super-secret-jwt-key-change-this-in-production

# Application URL
NEXT_PUBLIC_APP_URL=http://localhost:3000

# Node Environment
NODE_ENV=development
```

## 🔐 Demo Credentials

### Admin Account
- **Email:** admin@dashboard.com
- **Password:** Admin@123
- **Access:** Full dashboard with all analytics

### User Account
- **Email:** user@dashboard.com
- **Password:** User@123
- **Access:** Limited to user profile

## 🛠️ Tech Stack

| Technology | Purpose | Documentation |
|------------|---------|---------------|
| **Next.js 15** | React framework with SSR | [Docs](https://nextjs.org/docs) |
| **TypeScript** | Type-safe JavaScript | [Docs](https://www.typescriptlang.org) |
| **MongoDB** | NoSQL database | [Docs](https://www.mongodb.com/docs) |
| **Mongoose** | MongoDB ODM | [Docs](https://mongoosejs.com) |
| **ShadCN UI** | Component library | [Docs](https://ui.shadcn.com) |
| **Tailwind CSS** | Utility-first CSS | [Docs](https://tailwindcss.com) |
| **Recharts** | React charting library | [Docs](https://recharts.org) |
| **JWT** | Authentication tokens | [Docs](https://jwt.io) |

## 📁 Project Structure

```
admin-analytics-dashboard/
├── src/
│   ├── app/                      # Next.js App Router
│   │   ├── (auth)/              # Authentication pages
│   │   ├── (dashboard)/         # Dashboard pages
│   │   └── api/                 # API routes
│   ├── components/              # React components
│   │   ├── ui/                  # ShadCN UI components
│   │   └── dashboard/           # Dashboard-specific components
│   ├── lib/                     # Utilities and configs
│   │   ├── db/                  # Database models and connection
│   │   └── auth/                # Authentication utilities
│   └── middleware.ts            # Next.js middleware for auth
├── public/                      # Static assets
├── .env.local                   # Environment variables (create this)
└── package.json                 # Dependencies
```

## 📊 Key Components

### KPI Cards
Display key performance indicators:
- Total Users
- Total CV Analyses
- Average CV Score
- Feedback Count

### Charts
1. **Bar Chart** - Users by country
2. **Line Chart** - CV analysis trends over time
3. **Donut Chart** - Paid vs Free users
4. **Bar Chart** - Career stage distribution
5. **Rating Chart** - Feedback analytics

### Data Tables
- Top users leaderboard with CV scores
- Sortable and paginated tables

## 🔒 Security Features

- **JWT Authentication** - Secure token-based auth
- **Password Hashing** - bcrypt with salt rounds
- **Protected Routes** - Middleware-based route protection
- **Role-Based Access Control** - Admin and User permissions
- **Environment Variables** - Sensitive data protection
- **CORS Protection** - Secure API endpoints

## 🎨 UI/UX Features

- **Dark Mode Support** - Theme toggle (bonus feature)
- **Responsive Design** - Mobile-first approach
- **Loading States** - Skeleton loaders
- **Error Handling** - User-friendly error messages
- **Accessible Components** - WCAG compliant
- **Smooth Animations** - Framer Motion integration

## 📈 API Endpoints

### Authentication
- `POST /api/auth/register` - User registration
- `POST /api/auth/login` - User login
- `GET /api/auth/me` - Get current user

### Analytics
- `GET /api/analytics/users` - User demographics
- `GET /api/analytics/cv-analysis` - CV analysis metrics
- `GET /api/analytics/feedback` - Feedback statistics
- `GET /api/analytics/top-users` - Leaderboard data

### Utility
- `POST /api/seed` - Seed sample data (development only)

## 🧪 Testing

```bash
# Run tests (if implemented)
npm test

# Type checking
npm run type-check

# Linting
npm run lint
```

## 🚢 Deployment

### Vercel (Recommended)

1. Push your code to GitHub
2. Visit [vercel.com](https://vercel.com)
3. Import your repository
4. Add environment variables
5. Deploy!

```bash
# Or use Vercel CLI
npm i -g vercel
vercel
```

### Other Platforms
- **Netlify** - Supports Next.js
- **Railway** - Easy MongoDB + Next.js
- **Render** - Free tier available

## 📚 Documentation

- **Complete Implementation Guide** - See `Admin-Dashboard-Guide.pdf`
- **MongoDB Schema Reference** - See `mongodb_schema_reference.csv`
- **Technology Comparison** - See `technology_stack_comparison.csv`
- **Project Timeline** - See implementation checklist

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Next.js](https://nextjs.org) - The React framework
- [Vercel](https://vercel.com) - Hosting and deployment
- [ShadCN](https://ui.shadcn.com) - Beautiful UI components
- [MongoDB](https://mongodb.com) - Database platform
- [Recharts](https://recharts.org) - Charting library

## 📞 Support

For questions or issues:
- **Email:** support@dashboard.com
- **GitHub Issues:** [Create an issue](https://github.com/yourusername/admin-dashboard/issues)
- **Documentation:** See PDF guide included

---

**Built with ❤️ by Shashank Atmakur**

*Last Updated: November 2025*
