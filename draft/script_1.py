
import csv

# Create MongoDB Schema Reference Guide
mongodb_schemas = {
    "User Schema": {
        "fields": [
            {"name": "_id", "type": "ObjectId", "required": True, "description": "Auto-generated unique identifier"},
            {"name": "name", "type": "String", "required": True, "description": "User's full name"},
            {"name": "email", "type": "String", "required": True, "description": "Unique email address"},
            {"name": "password", "type": "String", "required": True, "description": "Hashed password"},
            {"name": "role", "type": "String", "required": True, "description": "User role: 'admin' or 'user'"},
            {"name": "country", "type": "String", "required": True, "description": "User's country"},
            {"name": "careerStage", "type": "String", "required": True, "description": "Fresher, Graduate, or Experienced"},
            {"name": "subscriptionType", "type": "String", "required": True, "description": "paid or free"},
            {"name": "createdAt", "type": "Date", "required": True, "description": "Account creation timestamp"},
            {"name": "updatedAt", "type": "Date", "required": True, "description": "Last update timestamp"}
        ]
    },
    "CV Analysis Schema": {
        "fields": [
            {"name": "_id", "type": "ObjectId", "required": True, "description": "Auto-generated unique identifier"},
            {"name": "userId", "type": "ObjectId (ref: User)", "required": True, "description": "Reference to User"},
            {"name": "cvScore", "type": "Number", "required": True, "description": "Score 0-100"},
            {"name": "analysisDate", "type": "Date", "required": True, "description": "Analysis timestamp"},
            {"name": "skills", "type": "Array<String>", "required": False, "description": "Extracted skills"},
            {"name": "experience", "type": "Number", "required": False, "description": "Years of experience"},
            {"name": "education", "type": "String", "required": False, "description": "Education level"},
            {"name": "sections", "type": "Object", "required": False, "description": "Score breakdown by section"}
        ]
    },
    "Feedback Schema": {
        "fields": [
            {"name": "_id", "type": "ObjectId", "required": True, "description": "Auto-generated unique identifier"},
            {"name": "userId", "type": "ObjectId (ref: User)", "required": True, "description": "Reference to User"},
            {"name": "rating", "type": "Number", "required": True, "description": "Rating 1-5"},
            {"name": "category", "type": "String", "required": True, "description": "UI/UX, Accuracy, Speed, Support"},
            {"name": "comment", "type": "String", "required": False, "description": "User feedback comment"},
            {"name": "createdAt", "type": "Date", "required": True, "description": "Feedback timestamp"}
        ]
    }
}

# Save schema reference as CSV
with open('mongodb_schema_reference.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Schema', 'Field Name', 'Type', 'Required', 'Description'])
    
    for schema_name, schema_info in mongodb_schemas.items():
        for field in schema_info['fields']:
            writer.writerow([
                schema_name,
                field['name'],
                field['type'],
                'Yes' if field['required'] else 'No',
                field['description']
            ])

print("MongoDB Schema Reference CSV created successfully!")
print("\nSchemas defined:")
for schema_name in mongodb_schemas.keys():
    print(f"  - {schema_name}")
