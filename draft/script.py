
import json

# Create comprehensive sample data structure for the admin dashboard
dashboard_data = {
    "users": {
        "total": 5420,
        "active": 4890,
        "inactive": 530,
        "paid": 1240,
        "free": 4180,
        "byCountry": [
            {"country": "United States", "count": 1850, "percentage": 34.1},
            {"country": "India", "count": 1320, "percentage": 24.4},
            {"country": "United Kingdom", "count": 680, "percentage": 12.5},
            {"country": "Canada", "count": 520, "percentage": 9.6},
            {"country": "Germany", "count": 410, "percentage": 7.6},
            {"country": "Australia", "count": 340, "percentage": 6.3},
            {"country": "Others", "count": 300, "percentage": 5.5}
        ],
        "byCareerStage": [
            {"stage": "Fresher", "count": 2180, "percentage": 40.2},
            {"stage": "Graduate", "count": 1630, "percentage": 30.1},
            {"stage": "Experienced", "count": 1610, "percentage": 29.7}
        ]
    },
    "cvAnalysis": {
        "totalAnalyses": 12450,
        "averageScore": 72.5,
        "monthlyTrend": [
            {"month": "Jan", "analyses": 980, "avgScore": 68.2},
            {"month": "Feb", "analyses": 1120, "avgScore": 70.1},
            {"month": "Mar", "analyses": 1280, "avgScore": 71.8},
            {"month": "Apr", "analyses": 1450, "avgScore": 72.5},
            {"month": "May", "analyses": 1620, "avgScore": 73.2},
            {"month": "Jun", "analyses": 1890, "avgScore": 74.1},
            {"month": "Jul", "analyses": 2110, "avgScore": 74.8},
            {"month": "Aug", "analyses": 2000, "avgScore": 72.9}
        ],
        "scoreDistribution": [
            {"range": "0-20", "count": 245},
            {"range": "21-40", "count": 890},
            {"range": "41-60", "count": 3120},
            {"range": "61-80", "count": 5680},
            {"range": "81-100", "count": 2515}
        ]
    },
    "feedback": {
        "totalResponses": 3240,
        "averageRating": 4.3,
        "satisfactionPercentage": 86,
        "ratings": [
            {"rating": 5, "count": 1620, "percentage": 50},
            {"rating": 4, "count": 1166, "percentage": 36},
            {"rating": 3, "count": 292, "percentage": 9},
            {"rating": 2, "count": 97, "percentage": 3},
            {"rating": 1, "count": 65, "percentage": 2}
        ],
        "categories": [
            {"category": "UI/UX", "avgRating": 4.5, "count": 2890},
            {"category": "Accuracy", "avgRating": 4.2, "count": 3100},
            {"category": "Speed", "avgRating": 4.4, "count": 2750},
            {"category": "Support", "avgRating": 4.1, "count": 1980}
        ]
    },
    "topUsers": [
        {"id": 1, "name": "Sarah Johnson", "email": "sarah.j@email.com", "cvScore": 94.5, "analyses": 15, "country": "USA"},
        {"id": 2, "name": "Raj Patel", "email": "raj.p@email.com", "cvScore": 93.2, "analyses": 12, "country": "India"},
        {"id": 3, "name": "Emma Williams", "email": "emma.w@email.com", "cvScore": 92.8, "analyses": 18, "country": "UK"},
        {"id": 4, "name": "Michael Chen", "email": "m.chen@email.com", "cvScore": 91.6, "analyses": 14, "country": "Canada"},
        {"id": 5, "name": "Lisa Schmidt", "email": "l.schmidt@email.com", "cvScore": 90.4, "analyses": 11, "country": "Germany"},
        {"id": 6, "name": "David Brown", "email": "d.brown@email.com", "cvScore": 89.7, "analyses": 13, "country": "Australia"},
        {"id": 7, "name": "Priya Sharma", "email": "p.sharma@email.com", "cvScore": 88.9, "analyses": 10, "country": "India"},
        {"id": 8, "name": "James Taylor", "email": "j.taylor@email.com", "cvScore": 88.3, "analyses": 16, "country": "USA"},
        {"id": 9, "name": "Sophie Martin", "email": "s.martin@email.com", "cvScore": 87.5, "analyses": 9, "country": "Canada"},
        {"id": 10, "name": "Ahmed Hassan", "email": "a.hassan@email.com", "cvScore": 86.8, "analyses": 12, "country": "UAE"}
    ],
    "paidVsFree": {
        "growth": [
            {"month": "Jan", "paid": 980, "free": 3120},
            {"month": "Feb", "paid": 1020, "free": 3280},
            {"month": "Mar", "paid": 1080, "free": 3450},
            {"month": "Apr", "paid": 1120, "free": 3620},
            {"month": "May", "paid": 1170, "free": 3840},
            {"month": "Jun", "paid": 1210, "free": 4050},
            {"month": "Jul", "paid": 1230, "free": 4150},
            {"month": "Aug", "paid": 1240, "free": 4180}
        ],
        "conversionRate": 22.9,
        "revenue": {
            "monthly": 37200,
            "avgPerUser": 30
        }
    }
}

# Save as JSON
with open('dashboard_sample_data.json', 'w') as f:
    json.dump(dashboard_data, f, indent=2)

print("Dashboard sample data created successfully!")
print(f"\nTotal Users: {dashboard_data['users']['total']}")
print(f"Total CV Analyses: {dashboard_data['cvAnalysis']['totalAnalyses']}")
print(f"Average CV Score: {dashboard_data['cvAnalysis']['averageScore']}")
print(f"Total Feedback Responses: {dashboard_data['feedback']['totalResponses']}")
print(f"Paid Users: {dashboard_data['users']['paid']}")
print(f"Free Users: {dashboard_data['users']['free']}")
